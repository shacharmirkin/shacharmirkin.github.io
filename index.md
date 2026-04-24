---
layout: default
title: Home
---

<div class="home-container">
    <div class="profile-section">
        <img src="/assets/images/profile.jpg" alt="Shachar Mirkin" class="profile-image">
        <div class="profile-content">
            <h1>Shachar Mirkin</h1>
            <p class="tagline">Freelance Applied AI Researcher</p>
        </div>
    </div>

    <div class="content-section">
        <style>
            .lang-switcher {
                display: inline-flex;
                gap: 8px;
                margin-bottom: 14px;
                padding: 4px;
                border: 1px solid #d0d7de;
                border-radius: 999px;
                background: #f6f8fa;
            }

            .lang-switcher button {
                border: none;
                border-radius: 999px;
                padding: 8px 14px;
                font-size: 0.92rem;
                font-weight: 600;
                cursor: pointer;
                background: transparent;
                color: #57606a;
                transition: background-color 0.2s ease, color 0.2s ease, transform 0.1s ease;
            }

            .lang-switcher button:hover {
                background: #ffffff;
                color: #24292f;
            }

            .lang-switcher button:active {
                transform: translateY(1px);
            }

            .lang-switcher button.active {
                background: #0969da;
                color: #ffffff;
                box-shadow: 0 1px 2px rgba(9, 105, 218, 0.3);
            }
        </style>
        <div class="lang-switcher">
            <button id="lang-en" type="button" aria-pressed="true">English</button>
            <button id="lang-fr" type="button" aria-pressed="false">Français</button>
        </div>

        <div id="about-en">
            <h2>About Me</h2>
            <p>I am a freelance applied researcher (PhD) with 20+ years of hands-on expertise in NLP, Generative AI, and Machine Learning, spanning industry and academia.</p>

            <p>I have worked in research institutes (IBM Research AI, Xerox Research), startups, and corporations, successfully bringing AI projects from design to production across domains such as legal, finance, and healthcare/biomedical. I have nearly 10 years of experience as a manager and team leader, co-supervising graduate students and mentoring junior colleagues.</p>

            <p>I hold a PhD in Computer Science, specializing in NLP, and have completed 3.5 years of postdoctoral research. I am the author of multiple patents and around 40 academic publications in top-tier venues (<a href="https://scholar.google.com/citations?user=xsEZbOkAAAAJ&amp;hl=en">Google Scholar</a>: 4,500+ citations; h-index: 23).</p>

            <p>Based in France, I am open to short- or long-term remote projects as a freelancer via my registered company. <a href="/contact">Contact me</a> to discuss your project.</p>
        </div>

        <div id="about-fr" style="display: none;">
            <h2>À propos de moi</h2>
            <p>Chercheur appliqué et consultant indépendant (PhD) avec plus de 20 ans d’expertise en NLP, IA générative et Machine Learning, j’interviens à la frontière entre le monde académique et l’industrie.</p>

            <p>Mon parcours au sein de centres de recherche (IBM Research AI, Xerox Research), de startups et de grands groupes m’a permis de mener avec succès des projets IA de la conception à la mise en production, notamment dans les secteurs juridique, financier et médical. J’ai près de 10 ans d’expérience en management et direction d’équipe, incluant la co-supervision de doctorants et le mentorat de profils juniors.</p>

            <p>Titulaire d’un doctorat en informatique, spécialisé en NLP, et fort de 3,5 ans de recherche postdoctorale, je suis l’auteur de plusieurs brevets et d’environ 40 publications académiques (<a href="https://scholar.google.com/citations?user=xsEZbOkAAAAJ&amp;hl=en">Google Scholar</a> : 4500+ citations ; h-index : 23).</p>

            <p>Basé à Grenoble, je propose mes services en freelance (via ma société) pour des missions à distance, à court ou long terme. <a href="/contact">Contactez-moi</a> pour échanger sur votre projet.</p>
        </div>

        <div id="recent-work-en">
            <h2>Recent Work</h2>
            <p>I can't share much about my clients' projects, but you can check out my <a href="/research">academic research</a> and these short <a href="/snippets">snippets</a> to learn more about my other activities.</p>
        </div>
        <div id="recent-work-fr" style="display: none;">
            <h2>Activité récente</h2>
            <p>Je ne peux pas partager grand-chose sur les projets de mes clients, mais vous pouvez consulter mes <a href="/research">travaux de recherche</a> ainsi que ces courts <a href="/snippets">extraits</a> pour en savoir plus sur mes autres activités.</p>
        </div>
    </div>

</div>

<script>
    (function () {
        const aboutEn = document.getElementById("about-en");
        const aboutFr = document.getElementById("about-fr");
        const recentEn = document.getElementById("recent-work-en");
        const recentFr = document.getElementById("recent-work-fr");
        const btnEn = document.getElementById("lang-en");
        const btnFr = document.getElementById("lang-fr");

        function setLanguage(lang) {
            const isEnglish = lang === "en";
            aboutEn.style.display = isEnglish ? "block" : "none";
            aboutFr.style.display = isEnglish ? "none" : "block";
            recentEn.style.display = isEnglish ? "block" : "none";
            recentFr.style.display = isEnglish ? "none" : "block";
            btnEn.classList.toggle("active", isEnglish);
            btnFr.classList.toggle("active", !isEnglish);
            btnEn.setAttribute("aria-pressed", String(isEnglish));
            btnFr.setAttribute("aria-pressed", String(!isEnglish));
        }

        btnEn.addEventListener("click", function () { setLanguage("en"); });
        btnFr.addEventListener("click", function () { setLanguage("fr"); });
        setLanguage("en");
    })();
</script>
