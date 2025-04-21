---
layout: post
title: "Invalid Jupyter notebooks on GitHub"
date: 2025-04-16 12:00:00 +0200
categories: [introduction]
tags: [GitHub, Jupyter, Google Colab]
excerpt: "Workarounds for dealing with Invalid Notebook error on GitHub"
image: /assets/images/github-invalid-notebook.png
---

## The Problem

When trying to view Jupyter notebooks on GitHub, we sometimes see the above 'Invalid Notebook' message.
This often happens with notebooks created in _Google Colab_ as it structures notebook metadata differently than what GitHub's renderer expects.

In this [gist](https://gist.github.com/shacharmirkin/7f608c51f5d1c159d5c5791081eb5c6d) I describe different solutions (workarounds) for this issue, including a description of automating a fix as a pre-commit hook.
