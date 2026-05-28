---
layout: post
title: "Alpine Ibex Vision Test"
date: 2026-04-30 09:00:00 +0200
categories: [ai]
tags: [llm, vision, vlm, prompting, capabilities, evaluation]
excerpt: "My anecdotal vision test, and a lesson about triggering the right capabilities"
image: /assets/images/ibex.jpeg
image_alt: "Herd of alpine ibex on a rocky mountainside, difficult to spot"
---

Here's an image of a herd of ibex I took in August 2024 in the [Vercors mountain range](https://vercors.fr/) in France. There are over 20 of them, but yes, they're really hard to see. I even had a hard time spotting them just a few hours after I saw them, so I was curious whether AI could do it. I asked some models whether they could spot any animals in the photo.

Back then, nearly all state-of-the-art models [failed miserably](https://x.com/shacharmirkin/status/1827401718604116224), typically detecting only a single ibex, but I did get some [funny responses](http://x.com/shacharmirkin/status/1827751629053149346).

In April 2026, I tried it again, and this time I got some much better results, with Gemini 3.1 Pro detecting up to 10 ibex.

Possibly the most interesting result came when I asked Gemini to annotate them. It said it couldn’t.
But when I instead asked it to regenerate the image with the animals painted in blue, it produced the image below.
The capability was there all along. It was just a matter of framing the task differently to trigger it.

<figure class="post-lightbox">
  <button type="button" class="post-lightbox__trigger">
    <img
      src="/assets/images/blue-ibex.jpeg"
      alt="Same mountain scene with ibex highlighted in blue by the model"
      width="400"
    />
  </button>
  <figcaption>Annotated image (select to enlarge)</figcaption>
</figure>

<dialog id="blue-ibex-lightbox" class="post-lightbox__dialog" aria-label="Enlarged annotated ibex image">
  <button type="button" class="post-lightbox__close" aria-label="Close">×</button>
  <img src="/assets/images/blue-ibex.jpeg" alt="Enlarged view of ibex highlighted in blue" />
</dialog>

<script>
  (function () {
    const trigger = document.querySelector(".post-lightbox__trigger");
    const dialog = document.getElementById("blue-ibex-lightbox");
    const closeBtn = dialog && dialog.querySelector(".post-lightbox__close");
    if (!trigger || !dialog || typeof dialog.showModal !== "function") return;

    const openDialog = () => dialog.showModal();
    const closeDialog = () => dialog.close();

    trigger.addEventListener("click", openDialog);
    closeBtn && closeBtn.addEventListener("click", closeDialog);
    dialog.addEventListener("click", (event) => {
      if (event.target === dialog) closeDialog();
    });
    dialog.addEventListener("cancel", closeDialog);
  })();
</script>
