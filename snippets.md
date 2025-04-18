---
layout: default
title: Snippets
---

# Snippets

<div class="snippets-container">
    {% for post in site.posts %}
    <article class="snippet-preview">
        <div class="snippet-content">
            <h2><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h2>
            <div class="snippet-meta">
                <time class="snippet-date">{{ post.date | date: "%B %-d, %Y" }}</time>
                {% if post.tags.size > 0 %}
                <div class="snippet-tags">
                    {% for tag in post.tags %}
                    <a href="/snippets?tag={{ tag | slugify }}" class="tag-button">{{ tag }}</a>
                    {% endfor %}
                </div>
                {% endif %}
            </div>
            {% if post.excerpt %}
            <p class="snippet-excerpt">{{ post.excerpt }}</p>
            {% endif %}
        </div>
        {% if post.image %}
        <div class="snippet-image">
            <a href="{{ post.url | relative_url }}">
                <img src="{{ post.image | relative_url }}" alt="{{ post.title }}" />
            </a>
        </div>
        {% endif %}
    </article>
    {% endfor %}
</div>

<style>
.snippets-container {
    max-width: 1000px;
    margin: 0 auto;
    padding: 2rem 1rem;
}

.snippet-preview {
    display: grid;
    grid-template-columns: 1fr 300px;
    gap: 2rem;
    margin-bottom: 2rem;
    padding-bottom: 2rem;
    border-bottom: 1px solid var(--nav-border);
    transition: transform 0.2s ease;
}

.snippet-preview:hover {
    transform: translateX(5px);
}

.snippet-content {
    display: flex;
    flex-direction: column;
}

.snippet-preview h2 {
    margin-bottom: 0.5rem;
    font-size: 1.5rem;
}

.snippet-preview h2 a {
    color: var(--text-color);
    text-decoration: none;
    transition: color 0.2s ease;
}

.snippet-preview h2 a:hover {
    color: var(--primary-color);
}

.snippet-meta {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    gap: 1rem;
    margin-bottom: 0.75rem;
}

.snippet-date {
    color: var(--text-light);
    font-size: 0.9rem;
}

.snippet-tags {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
}

.tag-button {
    display: inline-block;
    padding: 0.25rem 0.75rem;
    background: var(--nav-bg);
    color: var(--text-color);
    text-decoration: none;
    border-radius: var(--radius-sm);
    font-size: 0.85rem;
    transition: all var(--transition-fast);
}

.tag-button:hover {
    background: var(--nav-hover);
    color: var(--primary-color);
}

.snippet-excerpt {
    color: var(--text-color);
    line-height: 1.6;
    font-size: 1rem;
    margin-top: 0.5rem;
}

.snippet-image {
    border-radius: var(--radius-md);
    overflow: hidden;
    box-shadow: var(--shadow-md);
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.snippet-image:hover {
    transform: translateY(-2px);
    box-shadow: var(--shadow-lg);
}

.snippet-image img {
    width: 100%;
    height: 200px;
    object-fit: cover;
    display: block;
}

@media (max-width: 768px) {
    .snippets-container {
        padding: 1rem;
    }
    
    .snippet-preview {
        grid-template-columns: 1fr;
        gap: 1rem;
        margin-bottom: 1.5rem;
        padding-bottom: 1.5rem;
    }
    
    .snippet-image {
        order: -1;
    }
    
    .snippet-image img {
        height: 180px;
    }
}
</style>
