---
layout: post
title: "vLLM on Google Colab"
date: 2025-04-26 12:00:00 +0200
categories: []
tags: [vLLM, LiteLLM, LLMs, Google Colab]
excerpt: "Running a vLLM server on Google Colab"
image: /assets/images/vllm-on-colab.png
---

## Motivation

[vllm](https://github.com/vllm-project/vllm) is a popular library for fast LLM serving.

I needed to test my code with vLLM but didn't have access to the actual server.
I couldn't run in locally with a GPU (Apple Silicon is not yet supported), so I set up a vLLM server on Google Colab.

This [gist](https://gist.github.com/shacharmirkin/60d3403909ea5a540f7e17f2c3f2581a) show how it's done.
