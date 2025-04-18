---
layout: post
title: "GitHub Invalid Notebooks"
date: 2025-04-16 12:00:00 +0200
categories: [introduction]
tags: [blogging, jekyll]
excerpt: "Workarounds for dealing with Invalid Notebook error on GitHub"
image: /assets/images/github-invalid-notebook.png
---

## The Problem

When trying to view Jupyter notebooks on GitHub, we sometimes see an 'Invalid Notebook' message:

```text
"Invalid Notebook

There was an error rendering your Notebook: the 'state' key is missing from 'metadata.widgets'. Add 'state' to each, or remove 'metadata.widgets'.
```

![image](https://gist.github.com/user-attachments/assets/baacf996-4594-45b5-8d8d-0a21e3db37dd)

This often happens with notebooks created in _Google Colab_ as it structures notebook metadata differently than what GitHub's renderer expects.

## Jupyter Widgets

[Jupyter Widgets](https://ipywidgets.readthedocs.io/en/latest) are interactive browser controls for Jupyter notebooks, such as sliders, accordions, maps etc.
The notebook's json includes the state and version of each widget.

## Solutions (workarounds)

Here are several workarounds. I'll update this gist if I find (or anyone suggests) a more complete solution.

### Clearing cell's output

One [solution](https://github.com/orgs/community/discussions/155944#discussioncomment-12749143) is to clear the notebook outputs, or at least the outputs of cells which utilize widgets works. This is the easiest solution if you know which cells to clear, and you don't mind deleting their output.

### Deleting the widgets field

As suggested in the error message, in the notebook's underlying json, there's a `widgets` metadata field without a state. A simple solution is therefore to delete "widgets" from the json.

⚠️ When deleting widgets, you lose the widgets state, e.g. the position of a slider, and also its binding to the cell's output, which means that a slider will no longer control the output if moved.

This does not delete any cell output and to the best of my knowledge is reversible: if you run the notebook again they will be re-added.

#### Command-line

[Source](https://github.com/orgs/community/discussions/155944#discussioncomment-12845735)

```sh
# Create a backup first (optional but recommended)
cp notebook.ipynb notebook_backup.ipynb

# Use jq to delete the metadata.widgets key and save to a temporary file
jq 'del(.metadata.widgets)' notebook.ipynb > temp_notebook.ipynb

# Replace the original file with the fixed one
mv temp_notebook.ipynb notebook.ipynb
```

#### Python

```python
import os
import json
import sys


def clean_notebook(filepath):
    try:
        filepath = os.path.abspath(filepath)
        with open(filepath, "r", encoding="utf-8") as f:
            notebook = json.load(f)

        modified = False
        if "metadata" in notebook and "widgets" in notebook["metadata"]:
            del notebook["metadata"]["widgets"]
            modified = True

        if modified:
            with open(filepath, "w", encoding="utf-8") as f:
                json.dump(notebook, f, indent=2)
            print(f"Cleaned {filepath}")
            return True
        return False
    except Exception as e:
        print(f"Error processing {filepath}: {str(e)}", file=sys.stderr)
        return False

if __name__ == "__main__":
    for path in sys.argv[1:]:
        modified_notebook = clean_notebook(path)
        if modified_notebook:
            print(f"Modified {path}")
        else:
            print(f"No changes to {path}")
```

### Creating an HTML version of the notebook

A complementary solution is to convert the notebook to HTML using `nbconvert`.
This isn't a proper alternative because the conversion also fails if the json structure isn't fixed.
It can be added to the above script, thus proving feedback as to whether the cleaning succeeded.

Adding the HTML versions of the notebooks is a safe way to present the notebooks with its output without rendering issues (but the notebooks aren't interactive).

```python
# make sure to have nbconvert installed

import subprocess

subprocess.run(['jupyter', 'nbconvert', notebook_path, '--to', 'html'])
```

### Automation

The cleaning can be defined as a **pre-commit hook** or as a **GitHub Action**, to run automatically on the notebooks that are committed/pushed.

### Pre-commit hook

Pre-commit hooks are tests triggered by `git commit`, which abort the commit if they fail.
Here's an example of a pre-commit hook for deleting the widgets field from **staged** notebooks:

1. Prepare the file (do not use a different name):

   ```sh
   touch .git/hook/pre-commit
   chmod +x .git/hook/pre-commit
   ```

2. Copy the following content into `.git/hook/pre-commit`. Note that the major functionality is identical to the python script above.

```sh
#!/usr/bin/env bash

# uncomment the following line to get debug messages
# set -x

# Get staged notebooks (exclude checkpoints)
staged_notebooks=$(git diff --cached --name-only --diff-filter=ACM | grep '\.ipynb$' | grep -v '.ipynb_checkpoints')

if [ -z "$staged_notebooks" ]; then
    echo "No notebook files staged, skipping cleanup." >&2
    exit 0
fi

echo "Cleaning metadata from: $staged_notebooks" >&2

# Generate Python script
cat > /tmp/clean_notebooks.py << 'EOF'
import json
import sys
import os

def clean_notebook(filepath):
    try:
        filepath = os.path.abspath(filepath)
        with open(filepath, "r", encoding="utf-8") as f:
            notebook = json.load(f)

        modified = False
        if "metadata" in notebook and "widgets" in notebook["metadata"]:
            del notebook["metadata"]["widgets"]
            modified = True

        if modified:
            with open(filepath, "w", encoding="utf-8") as f:
                json.dump(notebook, f, indent=2)
            print(f"Cleaned {filepath}")
            return True
        return False
    except Exception as e:
        print(f"Error processing {filepath}: {str(e)}", file=sys.stderr)
        return False

for filepath in sys.argv[1:]:
    clean_notebook(filepath)
EOF

# Execute and re-add
python /tmp/clean_notebooks.py $staged_notebooks
git add $staged_notebooks
rm /tmp/clean_notebooks.py

exit 0
```
