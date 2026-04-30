---
layout: post
title: "Alpine Ibex Vision Test"
date: 2026-04-30 09:00:00 +0200
categories: [ai]
tags: [llm, vision, vlm, prompting, capabilities, evaluation]
excerpt: "My anecdotal vision test, and a lesson about triggering the right capabilities"
image: /assets/images/ibex.jpeg
---

Here's an image of a herd of ibex I took in August 2024 in the [Vercors mountain range](https://vercors.fr/) in France. There are over 20 of them, but yes, they're really hard to see. I even had a hard time spotting them just a few hours after I saw them, so I was curious whether AI could do it. I asked some models whether they could spot any animals in the photo

Back then, nearly all state-of-the-art models [failed miserably](https://x.com/shacharmirkin/status/1827401718604116224), typically detecting only a single ibex, but I did get some [funny responses](http://x.com/shacharmirkin/status/1827751629053149346).

In April 2026, I tried it again, and this time I got some much better results, with Gemini 3.1 Pro detecting up to 10 ibex.

Possibly the most interesting result came when I asked Gemini to annotate them. It said it couldn’t.
But when I instead asked it to regenerate the image with the animals painted in blue, it produced the image below.
The capability was there all along. It was just a matter of framing the task differently to trigger it.


<div style="text-align:center;">
  <img
    id="blue-ibex-preview"
    src="/assets/images/blue-ibex.jpeg"
    alt="Blue ibex (click to enlarge)"
    title="Click to enlarge"
    width="400"
    style="cursor:zoom-in;"
    tabindex="0"
    role="button"
    aria-label="Open enlarged blue ibex image"
  />
</div>

<dialog id="blue-ibex-lightbox" style="padding:0; border:none; background:transparent; max-width:none; width:100vw; height:100vh; margin:0;">
  <div style="width:100%; height:100%; display:flex; align-items:center; justify-content:center;">
    <img src="/assets/images/blue-ibex.jpeg" alt="Blue ibex enlarged" style="max-width:92vw; max-height:92vh; display:block;" />
  </div>
</dialog>

<script>
  (function () {
    const preview = document.getElementById("blue-ibex-preview");
    const dialog = document.getElementById("blue-ibex-lightbox");
    if (!preview || !dialog || typeof dialog.showModal !== "function") return;

    const openDialog = () => dialog.showModal();
    const closeDialog = () => dialog.close();

    preview.addEventListener("click", openDialog);
    preview.addEventListener("keydown", (event) => {
      if (event.key === "Enter") openDialog();
    });

    dialog.addEventListener("click", (event) => {
      if (event.target === dialog) closeDialog();
    });

    dialog.addEventListener("keydown", (event) => {
      if (event.key === "Escape" || event.key === "Enter") closeDialog();
    });
  })();
</script>


