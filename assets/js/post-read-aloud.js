(function () {
    function initReadAloud() {
        const toolbar = document.getElementById('post-read-aloud');
        const content = document.querySelector('.post-content');
        if (!toolbar || !content) return;

        if (!window.speechSynthesis || !window.SpeechSynthesisUtterance) {
            toolbar.hidden = true;
            return;
        }

        const playBtn = document.getElementById('read-aloud-play');
        const pauseBtn = document.getElementById('read-aloud-pause');
        const stopBtn = document.getElementById('read-aloud-stop');
        const statusEl = document.getElementById('read-aloud-status');
        const speechLang = toolbar.dataset.speechLang || document.documentElement.lang || 'en';
        const voiceNeedle = (toolbar.dataset.voiceName || '').trim().toLowerCase();
        const speechRate = parseFloat(toolbar.dataset.rate) || 1;
        const speechPitch = parseFloat(toolbar.dataset.pitch) || 1;

        let utterance = null;
        let playing = false;
        let paused = false;

        function setStatus(message) {
            statusEl.textContent = message;
        }

        function setControls({ playLabel, pauseEnabled, stopEnabled }) {
            if (playLabel) playBtn.setAttribute('aria-label', playLabel);
            pauseBtn.disabled = !pauseEnabled;
            stopBtn.disabled = !stopEnabled;
        }

        function extractReadableText(root) {
            const clone = root.cloneNode(true);
            clone.querySelectorAll(
                'script, style, pre, code, svg, [aria-hidden="true"], [data-read-aloud-exclude], .post-read-aloud'
            ).forEach((node) => node.remove());
            clone.querySelectorAll('img[alt]').forEach((img) => {
                const alt = img.getAttribute('alt');
                if (alt && alt.trim()) {
                    img.replaceWith(document.createTextNode(alt.trim() + '. '));
                } else {
                    img.remove();
                }
            });
            return clone.textContent.replace(/\s+/g, ' ').trim();
        }

        function langPrefix(lang) {
            return lang.toLowerCase().split('-')[0];
        }

        function resolveVoice() {
            const voices = window.speechSynthesis.getVoices();
            if (!voices.length) return null;

            if (voiceNeedle) {
                const byName = voices.find((v) => v.name.toLowerCase().includes(voiceNeedle));
                if (byName) return byName;
            }

            const prefix = langPrefix(speechLang);
            return (
                voices.find((v) => v.lang && v.lang.toLowerCase() === speechLang.toLowerCase()) ||
                voices.find((v) => v.lang && v.lang.toLowerCase().startsWith(prefix)) ||
                null
            );
        }

        function resetSpeech() {
            window.speechSynthesis.cancel();
            utterance = null;
            playing = false;
            paused = false;
            setControls({
                playLabel: toolbar.dataset.labelPlay,
                pauseEnabled: false,
                stopEnabled: false,
            });
            pauseBtn.setAttribute('aria-label', toolbar.dataset.labelPause);
        }

        function speak() {
            const body = extractReadableText(content);
            const title = (toolbar.dataset.articleTitle || '').trim();
            const text = [title, body].filter(Boolean).join('. ');
            if (!text) return;

            window.speechSynthesis.cancel();
            utterance = new SpeechSynthesisUtterance(text);
            utterance.lang = speechLang;
            utterance.rate = speechRate;
            utterance.pitch = speechPitch;
            const voice = resolveVoice();
            if (voice) utterance.voice = voice;

            utterance.onstart = () => {
                playing = true;
                paused = false;
                setControls({
                    playLabel: toolbar.dataset.labelPlay,
                    pauseEnabled: true,
                    stopEnabled: true,
                });
                setStatus(toolbar.dataset.statusPlaying);
            };

            utterance.onend = () => {
                resetSpeech();
                setStatus(toolbar.dataset.statusDone);
            };

            utterance.onerror = () => {
                resetSpeech();
                setStatus(toolbar.dataset.statusStopped);
            };

            window.speechSynthesis.speak(utterance);
        }

        playBtn.addEventListener('click', () => {
            if (paused && playing) {
                window.speechSynthesis.resume();
                paused = false;
                playBtn.setAttribute('aria-label', toolbar.dataset.labelPlay);
                pauseBtn.setAttribute('aria-label', toolbar.dataset.labelPause);
                setStatus(toolbar.dataset.statusPlaying);
                return;
            }
            if (playing) return;
            speak();
        });

        pauseBtn.addEventListener('click', () => {
            if (!playing || paused) return;
            if (typeof window.speechSynthesis.pause !== 'function') {
                window.speechSynthesis.cancel();
                playing = false;
                paused = false;
                setControls({
                    playLabel: toolbar.dataset.labelPlay,
                    pauseEnabled: false,
                    stopEnabled: false,
                });
                setStatus(toolbar.dataset.statusStopped);
                return;
            }
            window.speechSynthesis.pause();
            paused = true;
            playBtn.setAttribute('aria-label', toolbar.dataset.labelResume);
            setStatus(toolbar.dataset.statusPaused);
        });

        stopBtn.addEventListener('click', () => {
            resetSpeech();
            setStatus(toolbar.dataset.statusStopped);
        });

        window.speechSynthesis.addEventListener('voiceschanged', () => {});

        document.addEventListener('visibilitychange', () => {
            if (document.hidden && playing) {
                resetSpeech();
                setStatus(toolbar.dataset.statusStopped);
            }
        });
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initReadAloud);
    } else {
        initReadAloud();
    }
})();
