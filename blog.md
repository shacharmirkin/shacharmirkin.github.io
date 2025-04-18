---
layout: default
title: Blog
---

# Blog Posts

<div class="blog-container">
    {% for post in site.posts %}
    <article class="post-preview">
        <h2><a href="{{ post.url }}">{{ post.title }}</a></h2>
        <time class="post-date">{{ post.date | date: "%B %-d, %Y" }}</time>
        {% if post.excerpt %}
        <p class="post-excerpt">{{ post.excerpt }}</p>
        {% endif %}
    </article>
    {% endfor %}
</div>

<style>
.blog-container {
    max-width: 800px;
    margin: 0 auto;
    padding: 1.5rem 1rem;
}

.post-preview {
    margin-bottom: 1.5rem;
    padding-bottom: 1.5rem;
    border-bottom: 1px solid var(--nav-border);
    transition: transform 0.2s ease;
}

.post-preview:hover {
    transform: translateX(5px);
}

.post-preview h2 {
    margin-bottom: 0.25rem;
    font-size: 1.25rem;
}

.post-preview h2 a {
    color: var(--text-color);
    text-decoration: none;
    transition: color 0.2s ease;
}

.post-preview h2 a:hover {
    color: var(--primary-color);
}

.post-date {
    color: #6b7280;
    font-size: 0.85rem;
    margin-bottom: 0.5rem;
    display: block;
}

.post-excerpt {
    color: #4b5563;
    line-height: 1.5;
    font-size: 0.95rem;
    margin-top: 0.5rem;
}

@media (max-width: 768px) {
    .blog-container {
        padding: 1rem;
    }
    
    .post-preview {
        margin-bottom: 1rem;
        padding-bottom: 1rem;
    }
}
</style>
