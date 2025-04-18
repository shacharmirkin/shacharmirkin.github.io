---
layout: default
title: Academic Research
permalink: /research
---

# Academic Research

<div class="research-container">
    <div class="research-intro">
        <h2>Publications</h2>
        <p>Below is a list of my academic publications.</p>
    </div>

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

<style>
.research-container {
    max-width: 800px;
    margin: 0 auto;
    padding: 2rem;
}

.research-intro {
    margin-bottom: 3rem;
}

.year-section {
    margin-bottom: 2rem;
}

.year-section h3 {
    color: #2c3e50;
    border-bottom: 2px solid #eee;
    padding-bottom: 0.5rem;
    margin-bottom: 1.5rem;
}

.publication {
    background: #fff;
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
    color: #2c3e50;
    margin: 0 0 0.5rem 0;
    font-size: 1.2rem;
}

.authors {
    color: #666;
    font-style: italic;
    margin: 0.5rem 0;
}

.venue {
    color: #444;
    margin: 0.5rem 0;
}

.links {
    margin-top: 1rem;
}

.links a {
    display: inline-block;
    margin-right: 1rem;
    color: #3498db;
    text-decoration: none;
    padding: 0.25rem 0.5rem;
    border-radius: 4px;
    background: #f8f9fa;
    transition: background-color 0.2s ease;
}

.links a:hover {
    background: #e9ecef;
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
