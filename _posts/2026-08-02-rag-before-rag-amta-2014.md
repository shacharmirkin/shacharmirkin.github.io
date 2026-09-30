---
layout: post
title: "Doing RAG in 2014"
date: 2026-08-02 10:00:00 +0200
categories: []
tags: [RAG, MT, SMT, NLP, Research]
excerpt: "Looking back at our 2014 AMTA paper, the core mechanics of RAG were already there — years before the name."
image: /assets/publications/thumbnails/2014-data-selection-for-compact-adapted-smt-models.png
image_alt: "First page of the 2014 AMTA paper Data Selection for Compact Adapted SMT Models"
---
Everybody doing AI these days is well familiar with Retrieval Augmented Generation (RAG), a common method for adding relevant context to the LLM based on the user query.

Back in 2014, we were working on domain adaptation for statistical machine translation, arguably one of the best-studied **generation** tasks in NLP. The goal was to find techniques to make translation models best-adapted to target domains, while keeping them as small as possible.

One of the methods we proposed was taking the input text at test time, querying a large parallel corpus for relevant examples, and then training a customized translation model **augmented** with that **retrieved** data.

There you have it: RAG in 2014, way before the name was even coined.

Check out the details on our algorithm in Chapter 5 of the paper: 

_Shachar Mirkin and Laurent Besacier. [Data Selection for Compact Adapted SMT Models](https://aclanthology.org/2014.amta-researchers.23.pdf). AMTA 2014_.
