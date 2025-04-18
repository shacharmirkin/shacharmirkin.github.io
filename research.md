---
layout: default
title: Academic Research
permalink: /research
---

# Academic Research

<div class="research-container">
    <div class="research-intro">
        <h2>Research Interests</h2>
        <p>My research focuses on natural language processing, with particular emphasis on computational argumentation, machine translation, and semantic inference.</p>
    </div>

    <div class="research-areas">
        <div class="research-area">
            <h3>Computational Argumentation and Debating</h3>
            <p>Research in computational argumentation focuses on understanding and generating arguments, with applications in debating systems and listening comprehension.</p>
            <div class="publications">
                <h4>Selected Publications</h4>
                <ul>
                    <li>Noam Slonim et al. <a href="https://doi.org/10.1038/s41586-021-03215-w" target="_blank">An autonomous debating system</a>. <strong>Nature</strong> 591, 379–384 (2021).</li>
                    <li>Shachar Mirkin et al. <a href="https://www.aclweb.org/anthology/D18-1078/" target="_blank">Listening Comprehension over Argumentative Content</a>. EMNLP 2018.</li>
                    <li>Shachar Mirkin et al. <a href="http://www.lrec-conf.org/proceedings/lrec2018/pdf/66.pdf" target="_blank">A Recorded Debating Dataset</a>. LREC 2018.</li>
                </ul>
            </div>
        </div>

        <div class="research-area">
            <h3>Personalized Machine Translation</h3>
            <p>Research in personalized machine translation aims to adapt translation systems to individual users' preferences and characteristics.</p>
            <div class="publications">
                <h4>Selected Publications</h4>
                <ul>
                    <li>Ella Rabinovich et al. <a href="https://www.aclweb.org/anthology/E17-1101/" target="_blank">Personalized Machine Translation Preserving Original Author Traits</a>. EACL 2017.</li>
                    <li>Shachar Mirkin and Jean-Luc Meunier. <a href="https://www.aclweb.org/anthology/D15-1238/" target="_blank">Personalized machine translation: Predicting translational preferences</a>. EMNLP 2015.</li>
                </ul>
            </div>
        </div>

        <div class="research-area">
            <h3>Model-aware Improvement of Source Translatability</h3>
            <p>Research in improving source translatability focuses on modifying source texts to enhance translation quality.</p>
            <div class="publications">
                <h4>Selected Publications</h4>
                <ul>
                    <li>Shachar Mirkin et al. <a href="https://www.researchgate.net/publication/251231328_Confidence-driven_Rewriting_for_Improved_Translation" target="_blank">Confidence-driven Rewriting for Improved Translation</a>. MT Summit 2013.</li>
                    <li>Sriram Venkatapathy and Shachar Mirkin. <a href="http://www.aclweb.org/anthology/C12-3058" target="_blank">An SMT-driven Authoring Tool</a>. COLING 2012.</li>
                </ul>
            </div>
        </div>
    </div>

    <div class="all-publications">
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
                    <h4>{{ pub.title }}</h4>
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
                    {% if pub.doi or pub.pdf or pub.code %}
                        <div class="links">
                            {% if pub.doi %}
                                <a href="{{ pub.doi }}" target="_blank">DOI</a>
                            {% endif %}
                            {% if pub.pdf %}
                                <a href="{{ pub.pdf }}" target="_blank">PDF</a>
                            {% endif %}
                            {% if pub.code %}
                                <a href="{{ pub.code }}" target="_blank">Code</a>
                            {% endif %}
                        </div>
                    {% endif %}
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

<style>
.research-container {
    max-width: 1000px;
    margin: 0 auto;
    padding: 2rem 1rem;
}

.research-intro {
    margin-bottom: 3rem;
}

.research-intro h2 {
    font-size: 1.75rem;
    margin-bottom: 1.5rem;
    color: var(--text-color);
    border-bottom: 2px solid var(--nav-border);
    padding-bottom: 0.5rem;
}

.research-areas {
    display: grid;
    gap: 3rem;
    margin-bottom: 4rem;
}

.research-area h3 {
    font-size: 1.5rem;
    margin-bottom: 1rem;
    color: var(--text-color);
}

.research-area p {
    margin-bottom: 1.5rem;
    color: var(--text-color);
}

.publications h4 {
    font-size: 1.25rem;
    margin-bottom: 1rem;
    color: var(--text-color);
}

.publications ul {
    list-style-type: none;
    padding: 0;
}

.publications li {
    margin-bottom: 1rem;
    color: var(--text-color);
}

.year-section {
    margin-bottom: 2rem;
}

.year-section h3 {
    color: var(--text-color);
    border-bottom: 2px solid var(--nav-border);
    padding-bottom: 0.5rem;
    margin-bottom: 1.5rem;
}

.publication {
    background: var(--nav-bg);
    padding: 1.5rem;
    margin-bottom: 1.5rem;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.publication:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 8px rgba(0,0,0,0.15);
}

.publication h4 {
    color: var(--text-color);
    margin: 0 0 0.5rem 0;
    font-size: 1.2rem;
}

.authors {
    color: var(--text-color);
    font-style: italic;
    margin: 0.5rem 0;
}

.venue {
    color: var(--text-color);
    margin: 0.5rem 0;
}

.links {
    margin-top: 1rem;
}

.links a {
    display: inline-block;
    margin-right: 1rem;
    color: var(--link-color);
    text-decoration: none;
    padding: 0.25rem 0.5rem;
    border-radius: 4px;
    background: var(--nav-bg);
    transition: background-color 0.3s ease;
}

.links a:hover {
    background: var(--nav-hover);
}

@media (max-width: 768px) {
    .research-container {
        padding: 1rem;
    }
    
    .publication {
        padding: 1rem;
    }
    
    .publication h4 {
        font-size: 1.1rem;
    }
}
</style>
