---
layout: post
title: "When LLMs See What We Don’t"
date: 2026-03-13 10:00:00 +0200
categories: []
tags: [LLMs, AI, Hallucinations, Prompt Injection]
excerpt: "A local election story about how an LLM hallucinated a political alliance"
image: /assets/images/llm-sees.jpg
---

This weekend we have municipal elections here 🇫🇷, so a couple of weeks ago I asked a model about the candidates in our town. I was aware of three candidates, but the model said that two of them had formed an alliance to better challenge the current mayor, and it even provided supporting links. It kind of made sense politically, but when I followed the links, I couldn't find any of the supposed "proofs".

I confronted the model about it, but nothing I said helped convince it.
I had to get to the bottom of it, so I kept going back every day to see if it could find new information to support its claim. It just doubled down, sending me more evidence I couldn't see, along with "I understand your frustration". 🙄

I even made up a conversation I supposedly had with one of the candidates where they denied the alliance, but it said that's just what politicians do.

Eventually I checked the HTML source of one of the candidates' websites, and there it was: the name of the other candidate, with hidden tags (specifically, text inside `<span class="hide">` and a mention at the end of a long `<title>` tag, making the other candidate's name invisible).

Just a good old SEO trick, no prompt injection intended.

The LLM took that and built an entire story about an alliance that never existed, and was completely convinced it was right.

Sometimes we need to remind ourselves that what LLMs see isn't the same as what we do.

---
<div style="color: #666;">
<br>
  <ul>
    <li>We've all heard about prompt injection, where white text that includes LLM instructions and is invisible to humans is embedded in documents, but this is the first time I've encountered this kind of case.</li>
    <li>As far as I understand, the title-tag strategy is not ideal and may be penalized by Google Search due to signal incoherence.</li>
  </ul>
</div>
