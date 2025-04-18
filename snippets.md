---
layout: default
title: Snippets
permalink: /snippets/
---

# Snippets

{% assign selected_tag = page.url | split: '/' | last %}
{% if selected_tag != 'snippets' %}

<div class="tag-filter">
<p>Showing posts tagged with: <strong>{{ selected_tag }}</strong></p>
<a href="/snippets" class="clear-filter">Clear filter</a>
</div>
{% endif %}

<div class="snippets-container">
    {% for post in site.posts %}
        {% if selected_tag == 'snippets' or post.tags contains selected_tag %}
        <article class="snippet-preview">
            <div class="snippet-content">
                <h2><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h2>
                {% if post.excerpt %}
                <p class="snippet-excerpt">{{ post.excerpt }}</p>
                {% endif %}
                <div class="snippet-meta">
                    <span class="snippet-date">
                        <i class="fas fa-calendar"></i>
                        {{ post.date | date: "%B %-d, %Y" }}
                    </span>
                    {% if post.tags.size > 0 %}
                    <div class="snippet-tags">
                        {% for tag in post.tags %}
                        <span class="tag-button">{{ tag }}</span>
                        {% endfor %}
                    </div>
                    {% endif %}
                </div>
            </div>
            {% if post.image %}
            <div class="snippet-image">
                <a href="{{ post.url | relative_url }}">
                    <img src="{{ post.image | relative_url }}" alt="{{ post.title }}" />
                </a>
            </div>
            {% endif %}
        </article>
        {% endif %}
    {% endfor %}
</div>
