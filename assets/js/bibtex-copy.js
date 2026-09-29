(function () {
    const COPIED_MS = 2000;

    function copyText(text) {
        if (navigator.clipboard && window.isSecureContext) {
            return navigator.clipboard.writeText(text);
        }
        const ta = document.createElement("textarea");
        ta.value = text;
        ta.setAttribute("readonly", "");
        ta.style.position = "fixed";
        ta.style.left = "-9999px";
        document.body.appendChild(ta);
        ta.select();
        try {
            document.execCommand("copy");
            return Promise.resolve();
        } finally {
            document.body.removeChild(ta);
        }
    }

    function setCopied(button, statusEl) {
        const prev = button.textContent;
        button.textContent = "Copied!";
        button.disabled = true;
        if (statusEl) {
            statusEl.hidden = false;
            statusEl.textContent = "BibTeX copied to clipboard.";
        }
        window.setTimeout(() => {
            button.textContent = prev;
            button.disabled = false;
            if (statusEl) {
                statusEl.hidden = true;
                statusEl.textContent = "";
            }
        }, COPIED_MS);
    }

    document.addEventListener("click", (event) => {
        const button = event.target.closest(".bibtex-copy");
        if (!button) return;

        event.preventDefault();
        const panel = button.closest(".bibtex-panel");
        const code = panel && panel.querySelector(".bibtex-code code");
        if (!code) return;

        const statusEl = panel.querySelector(".bibtex-copy-status");
        copyText(code.textContent).then(
            () => setCopied(button, statusEl),
            () => {
                if (statusEl) {
                    statusEl.hidden = false;
                    statusEl.textContent = "Copy failed. Select the BibTeX and copy manually.";
                }
            }
        );
    });
})();
