---
layout: default
nav_title: Research
title: "Academic research"
description: "Highlights of academic work in NLP, personalized machine translation, computational argumentation, and a full publication list."
permalink: /research
---

# Academic Research

<div class="research-container">
    <div class="research-intro">
        <p>Here are some highlights of my academic interests.
        See the complete list of my publications <a href="#all-publications">below</a> or on <a href="https://scholar.google.com/citations?user=xsEZbOkAAAAJ&amp;hl=en">Google Scholar</a>.</p>
        {% if site.data.scholar.citations %}
        <p class="scholar-badge">
            <a href="https://scholar.google.com/citations?user=xsEZbOkAAAAJ&amp;hl=en">
                <img src="https://img.shields.io/badge/citations-{{ site.data.scholar.citations }}-4285F4?style=flat&amp;logo=google-scholar&amp;logoColor=white" alt="Google Scholar: {{ site.data.scholar.citations }} citations" loading="lazy">
            </a>
        </p>
        {% endif %}
    </div>

    <div class="research-areas">
        <div class="research-area">
            <h2>Computational Argumentation and Debating</h2>
            <p>Research in computational argumentation focuses on understanding and generating arguments, with applications in debating systems and listening comprehension.</p>
            <div class="publications">
                <h3>Selected Publications</h3>
                <ul>
                    <li>Noam Slonim et al. <a href="https://doi.org/10.1038/s41586-021-03215-w" target="_blank" rel="noopener noreferrer">An autonomous debating system</a>. <strong>Nature</strong> 591, 379–384 (2021).</li>
                    <li>Shachar Mirkin et al. <a href="https://www.aclweb.org/anthology/D18-1078/" target="_blank" rel="noopener noreferrer">Listening Comprehension over Argumentative Content</a>. EMNLP 2018.</li>
                    <li>Shachar Mirkin et al. <a href="http://www.lrec-conf.org/proceedings/lrec2018/pdf/66.pdf" target="_blank" rel="noopener noreferrer">A Recorded Debating Dataset</a>. LREC 2018.</li>
                </ul>
            </div>
        </div>

        <div class="research-area">
            <h2>Personalized Machine Translation</h2>
            <p>We proposed personalizing machine translation systems in order to adapt automatic translation systems from 2 different perspectives:
                <ul>
                    <li>For Individual users' preferences</li>
                    <li>For preserving authors' styles through translation</li>
                </ul>
            </p>
            <div class="publications">
                <h3>Selected Publications</h3>
                <ul>
                    <li>Ella Rabinovich, Shachar Mirkin, Raj Nath Patel, Lucia Specia and Shuly Wintner <a href="https://www.aclweb.org/anthology/E17-1101/" target="_blank" rel="noopener noreferrer">Personalized Machine Translation Preserving Original Author Traits</a>. EACL 2017.</li>
                    <li>Shachar Mirkin and Jean-Luc Meunier. <a href="https://www.aclweb.org/anthology/D15-1238/" target="_blank" rel="noopener noreferrer">Personalized machine translation: Predicting translational preferences</a>. EMNLP 2015.</li>
                    <li>Shachar Mirkin, Scott Nowson, Scott, Caroline Brun, Julien Perez. <a href="https://aclanthology.org/D15-1130/" target="_blank" rel="noopener noreferrer">Motivating Personality-aware Machine Translation</a>. EMNLP 2015.</li>
                </ul>
            </div>
        </div>

        <div class="research-area">
            <h2>Model-aware Improvement of Source Translatability</h2>
            <p>Research in improving source translatability focuses on modifying source texts to enhance translation quality.</p>
            <div class="publications">
                <h3>Selected Publications</h3>
                <ul>
                    <li>Shachar Mirkin et al. <a href="https://www.researchgate.net/publication/251231328_Confidence-driven_Rewriting_for_Improved_Translation" target="_blank" rel="noopener noreferrer">Confidence-driven Rewriting for Improved Translation</a>. MT Summit 2013.</li>
                    <li>Sriram Venkatapathy and Shachar Mirkin. <a href="http://www.aclweb.org/anthology/C12-3058" target="_blank" rel="noopener noreferrer">An SMT-driven Authoring Tool</a>. COLING 2012.</li>
                </ul>
            </div>
        </div>
    </div>

    <div class="academic-service">
        <h2>Academic Service</h2>
        <h3>Program Committee Member</h3>
        <p>W-NUT 2026 (expected) //ACL 2024 (Area Chair) // W-NUT 2022 // ARR April 2022 / ACL 2022 (ARR) // W-NUT 2021 // EMNLP 2021 // EACL 2021 // COLING 2020 // *SEM 2020 // EMNLP 2020 // ACL 2020 // LREC 2020 // W-NUT 2019 // ACL 2019 // NLP+CSS 2019 // COLING 2018 // ACL 2018 // NAACL 2018 // EMNLP 2017 // *SEM 2017 // ACL 2017 // Journal of Natural Language Engineering (JNLE) 2016 // COLING 2016 // LREC 2016 // EMNLP 2016 // *SEM 2016 // EMNLP 2015 // *SEM 2015 // CICLING 2015 // Journal of Language Resources and Evaluation (LREV) 2014 //EMNLP 2014 // COLING 2014 // WMT 2014 // LREC 2014 // WMT 2013 // Journal of Language Resources and Evaluation (LREV) 2013 // IJCNLP 2013 // *SEM 2013 // Journal of Computer Science and Technology (JCST) 2013 // WMT 2012 // EACL 2012 // LREC 2012 // ACM TIST Journal, Special Issue on Paraphrasing 2011 // EMNLP 2011 // TextInfer 2011 // COLING 2010 // EMNLP 2009 // AAAI 2008</p>
    </div>

    <div class="all-publications" id="all-publications">
        <h2>All Publications</h2>

        {% if site.data.citations and site.data.citations.size > 0 %}
            {% assign sorted_pubs = site.data.citations | sort: "year" | reverse %}
            {% assign current_year = nil %}

            {% for pub in sorted_pubs %}
                {% if pub.year != current_year %}
                    {% if current_year %}
                        </div>
                    {% endif %}
                    <div class="year-section">
                    <h3>{{ pub.year }}</h3>
                    {% assign current_year = pub.year %}
                {% endif %}

                <div class="publication">
                    <details>
                        <summary class="paper-title">{{ pub.title }}</summary>
                        <p class="authors">{{ pub.authors }}</p>
                        {% if pub.publication %}
                            <p class="venue">
                                {{ pub.publication }}
                                {% if pub.volume %}
                                    , Volume {{ pub.volume }}
                                {% endif %}
                                {% if pub.number %}
                                    ({{ pub.number }})
                                {% endif %}
                                {% if pub.pages %}
                                    , pp. {{ pub.pages }}
                                {% endif %}
                            </p>
                        {% endif %}
                        <p class="abstract">
                            {% if pub.abstract %}
                                {{ pub.abstract }}
                            {% else %}
                                Abstract not available.
                            {% endif %}
                        </p>
                        <div class="links">
                            {% if pub.url %}
                                <a href="{{ pub.url }}" target="_blank" rel="noopener noreferrer">Paper</a>
                            {% endif %}
                            {% if pub.doi %}
                                <a href="{{ pub.doi }}" target="_blank" rel="noopener noreferrer">DOI</a>
                            {% endif %}
                            {% if pub.pdf %}
                                <a href="{{ pub.pdf }}" target="_blank" rel="noopener noreferrer">PDF</a>
                            {% endif %}
                            {% if pub.code %}
                                <a href="{{ pub.code }}" target="_blank" rel="noopener noreferrer">Code</a>
                            {% endif %}
                        </div>
                    </details>
                </div>
            {% endfor %}

            {% if current_year %}
                </div>
            {% endif %}
        {% else %}
            <p>No publications available.</p>
        {% endif %}
    </div>

</div>
