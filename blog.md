---
layout: default
title: Blog
---

# Blog Posts

{% for post in site.posts %}

<div class="post-preview">
    <h2><a href="{{ post.url }}" target="_blank">{{ post.title }}</a></h2>
    <p class="post-date">{{ post.date | date: "%B %-d, %Y" }}</p>
    {% if post.excerpt %}
    <p class="post-excerpt">{{ post.excerpt }}</p>
    {% endif %}
</div>
{% endfor %}

<style>
.post-preview {
    margin-bottom: 2rem;
    padding-bottom: 1rem;
    border-bottom: 1px solid #eee;
}
.post-date {
    color: #666;
    font-size: 0.9em;
}
.post-excerpt {
    margin-top: 0.5rem;
}
</style>
