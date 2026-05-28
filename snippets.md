---
layout: default
nav_title: Snippets
title: "Snippets — side projects and notes"
description: "Short posts on side projects, experiments, and informal notes on NLP, LLMs, and data science."
permalink: /snippets/
---

# Snippets

This page is a collection of random (not always too serious) side projects, experiments, and thoughts.

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
        {% if post.pinned == true %}
        <article class="snippet-preview">
            <div class="snippet-content">
                <h2><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h2>
                {% if post.excerpt %}
                <p class="snippet-excerpt">{{ post.excerpt }}</p>
                {% endif %}
                <div class="snippet-meta">
                    <time class="snippet-date" datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%B %-d, %Y" }}</time>
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
                <a href="{{ post.url | relative_url }}" aria-label="View article: {{ post.title | xml_escape }}">
                    <img src="{{ post.image | relative_url }}" alt="" />
                </a>
            </div>
            {% endif %}
        </article>
        {% endif %}
        {% endif %}
    {% endfor %}

    {% for post in site.posts %}
        {% if selected_tag == 'snippets' or post.tags contains selected_tag %}
        {% if post.pinned != true %}
        <article class="snippet-preview">
            <div class="snippet-content">
                <h2><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h2>
                {% if post.excerpt %}
                <p class="snippet-excerpt">{{ post.excerpt }}</p>
                {% endif %}
                <div class="snippet-meta">
                    <time class="snippet-date" datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%B %-d, %Y" }}</time>
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
                <a href="{{ post.url | relative_url }}" aria-label="View article: {{ post.title | xml_escape }}">
                    <img src="{{ post.image | relative_url }}" alt="" />
                </a>
            </div>
            {% endif %}
        </article>
        {% endif %}
        {% endif %}
    {% endfor %}
</div>
