---
layout: post
title: "Vibe Coding a chess app"
date: 2024-09-25 12:00:00 +0200
categories: []
tags: [Vibe Coding, Cursor, Streamlit, Chess]
excerpt: "Creating a little chess app using (almost) only Cursor"
image: /assets/images/chess-openings.jpg
---

When I saw that Lichess openings dataset was shared on Hugging Face, I thought I’d use AI to create an app within 45 minutes (like everyone else says they do) to help my daughter practice openings.

Since my front-end skills are quite limited, Cursor was crucial, but I ended up spending much more time than planned, frequently consulting various LLMs, fixing code myself and reverting changes quite often (lesson learned: when using such tools, commit all the time!)

The result is a little [Streamlit](https://streamlit.io/) app for practicing chess openings, and my first project where AI wrote more code than I did.

You can try it [on Hugging Face](https://huggingface.co/spaces/shachar/chess-openings) (completely free of course), or check out the code [here](https://huggingface.co/spaces/shachar/chess-openings/tree/main).
