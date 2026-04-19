---
layout: post
title: "Universal NER v2 paper"
date: 2026-03-18 9:00:00 +0200
categories: []
tags: [NLP, NER, LREC, Research, Benchmarks, Multilingual]
excerpt: "Universal NER v2 was accepted to LREC 2026."
image: /assets/images/uner.png
---


I'm happy to share that our [paper](https://arxiv.org/pdf/2604.12744), **Universal NER v2**, was accepted to [LREC 2026](https://lrec2026.info/).

In this paper we present Universal NER (UNER) v2, a substantial extension of the dataset introduced in 2024. UNER is a collaborative resource for multilingual named-entity annotation, designed to support cross-lingual NER research.

UNER v2 adds 11 datasets covering 10 typologically diverse languages, including several aligned evaluation benchmarks, while preserving consistent annotation guidelines and high inter-annotator agreement. We provide detailed dataset statistics and benchmark performance using both encoder-based models and LLMs.

We compared human annotation with LLM-based annotation under the same guidelines. Our results show that LLMs still lag behind human annotators,and analyze the typical mistakes they make. While performance could likely be improved through more elaborate instructions or via agentic workflows, LLMs are not yet dependable annotators. That said, they show promise not only for annotation, but also for identifying inconsistencies in human labels and weaknesses in the guidelines, which we plan to explore in future work.

_Terra Blevins, Stephen Mayhew, Marek Suppa, Hila Gonen, Shachar Mirkin, Vasile Pais, Kaja Dobrovoljc, Voula Giouli, Jun Kevin, Enes Yılandiloğlu, Eugene Jang, Eungseo Kim, Jeongyeon Seo, Xenophon Gialis and Yuval Pinter. [Universal NER v2: Towards a Massively Multilingual Named Entity Recognition Benchmark](https://arxiv.org/pdf/2604.12744). LREC 2026_.

*Last updated: April 19, 2026*
