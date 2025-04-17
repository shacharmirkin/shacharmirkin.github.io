---
layout: default # Or another layout provided by your theme (e.g., home)
title: Home # Optional: Sets the page title
---

# Shachar Mirkin's page

I'm a data scientist / applied researcher with extensive hands-on experience in Natural Language Processing & Machine Learning, in both academic and industry, including 6 years as a data science team leader.

[View my blog posts](/blog.html){:target="\_blank"}

My PhD thesis addressed employing context for natural language inference, and during my postdoc I've mostly worked on multilingual tasks, notably machine translation. I've published multiple academic articles at top-tier venues as well as several patents ([Google Scholar](https://scholar.google.com/citations?user=shacharmirkin)).

Among the many tasks I've been working on along the years are machine translation, sentiment analysis, information extraction, object detection, location classification, automatic punctuation and text classification over different languages and types of texts, including spoken and user generated data.
That, using various approaches, from rules, through classic machine learning, and up to deep learning, with real-time inference in production.

Currently, I'm mostly interested in developing practical ML solutions for real-world tasks, choosing the right solution for the product, depending on its specific characteristics and constraints.

[My Linkedin profile](https://www.linkedin.com/in/shacharmirkin)

---

## Academic research interests

### Computational argumentation and debating

**Selected publications:**

- Noam Slonim et al. [An autonomous debating system](https://doi.org/10.1038/s41586-021-03215-w). **Nature** 591, 379–384 (2021).

- Shachar Mirkin, Guy Moshkowich, Matan Orbach, Lili Kotlerman, Yoav Kantor, Tamar Lavee, Michal Jacovi, Yonatan Bilu, Ranit Aharonov and Noam Slonim.
  [Listening Comprehension over Argumentative Content](https://www.aclweb.org/anthology/D18-1078/). EMNLP 2018.  
  _This paper is among IBM Research AI [10 noteworthy publications from 2018](https://www.research.ibm.com/artificial-intelligence/publications/2018/)_

- Shachar Mirkin, Michal Jacovi, Tamar Lavee, Hong-Kwang Kuo, Samuel Thomas, Leslie Sager, Lili Kotlerman, Elad Venezian, Noam Slonim.
  [A Recorded Debating Dataset](http://www.lrec-conf.org/proceedings/lrec2018/pdf/66.pdf). LREC 2018

- Vardaan Pahuja, Anirban Laha, Shachar Mirkin, Vikas Raykar, Lili Kotlerman, Guy Lev. InterSpeech 2017.
  [Joint Learning of Correlated Sequence Labelling Tasks Using Bidirectional Recurrent Neural Networks](https://www.isca-speech.org/archive/Interspeech_2017/pdfs/1247.PDF). [Code and data](https://github.com/vardaan123/Corr-seq-labeling)

**Datasets:**

- [Recorded debating dataset](https://www.research.ibm.com/haifa/dept/vst/debating_data.shtml#Debate%20Speech%20Analysis)
  (debate speeches: audio + transcripts)

- [Listening comprehension over argumentative content](https://www.research.ibm.com/haifa/dept/vst/debating_data.shtml#Debate%20Speech%20Analysis)
  (speeches + annotation of arguments)

- [Mention detection (entity linking, wikification) over Wikipedia and speech text](https://paperswithcode.com/dataset/ibm-debater-mention-detection-benchmark)

### Personalized Machine Translation (PMT)

Machine Translation has advanced in recent years to produce better translations for clients' specific domains, and sophisticated tools allow translators to obtain translations according to their prior edits. We suggest that MT should be further personalized to the end-user level – the receiver or the author of the text – as done in other applications. Language use is known to be influenced by personality traits as well as by demographic characteristics such as age or mother tongue. As a result, it is possible to automatically identify these traits of the author from her texts. To provide the most faithful translation and to allow user modeling based on translations, we posit that machine translation should be personalized. PMT for the readers of the translations can take into account the reader's translational preferences, as reflected e.g. in complexity or style.

**Selected publications:**

- Ella Rabinovich, Shachar Mirkin, Raj Nath Patel, Lucia Specia and Shuly Wintner. [Personalized Machine Translation Preserving Original Author Traits](https://www.aclweb.org/anthology/E17-1101/). EACL 2017

- Shachar Mirkin and Jean-Luc Meunier. [Personalized machine translation: Predicting translational preferences](https://www.aclweb.org/anthology/D15-1238/). EMNLP 2015.

- Shachar Mirkin, Scott Nowson, Caroline Brun and Julien Perez. [Motivating Personality-aware Machine Translation](https://www.aclweb.org/anthology/D15-1130/). EMNLP 2015.

**Datasets:**

- [Bilingual Europarl corpora annotated with gender and age](http://cl.haifa.ac.il/projects/pmt/index.shtml) \[en-fr, en-de\]

- [TED talks annotated with gender](https://github.com/shacharmirkin/pmt) \[en-fr\]

### Model-aware improvement of source translatability for MT

Some source texts are more difficult to translate than others. One way to handle such texts is to modify them prior to translation (aka pre-editing). A prominent factor that is often overlooked is the source translatability with respect to the specific translation system and the specific model that are being used. Our research aims to improve source translatability either automatically, or through interactive tools which enable monolingual speakers of the source language to obtain better translation.

**Selected publications:**

- Shachar Mirkin, Sriram Venkatapathy and Marc Dymetman. 2013. [Confidence-driven Rewriting for Improved Translation](https://www.researchgate.net/publication/251231328_Confidence-driven_Rewriting_for_Improved_Translation). In Proceedings of MT Summit.

- Sriram Venkatapathy and Shachar Mirkin. [An SMT-driven Authoring Tool](http://www.aclweb.org/anthology/C12-3058). COLING 2012.

- Shachar Mirkin, Lucia Specia, Nicola Cancedda, Ido Dagan, Marc Dymetman and Idan Szpektor. [Source-Language Entailment Modeling for Translating Unknown Terms](http://www.aclweb.org/anthology/P09-1089). ACL-IJCNLP 2009.

### Semantic inference / Textual entailment

Textual Entailment (TE) is a popular paradigm for modeling semantic inference. The core TE task, Textual Entailment recognition, is to determine whether the meaning of one text can be inferred (or entailed) from another. My textual entailment research mostly focused around understanding entailment in context, to deal with either lexical ambiguity or discourse-based interpretation, but also addressed acquisition of lexical entailment relationships and the application of TE to different applications (e.g. SMT, as in several of the above works).

**Selected publications:**

- Shachar Mirkin, Jonathan Berant, Ido Dagan and Eyal Shnarch. [Recognising Entailment within Discourse](http://aclweb.org/anthology/C10-1087). COLING 2010.

- Shachar Mirkin, Ido Dagan, Lili Kotlerman and Idan Szpektor. [Classification-based Contextual Preferences](http://www.aclweb.org/anthology/W11-2403). TextInfer 2011.

- Shachar Mirkin, Ido Dagan and Sebastian Padó. [Assessing the Role of Discourse References in Entailment Inference](http://www.aclweb.org/anthology/P10-1123). ACL 2010.

- Shachar Mirkin, Ido Dagan, Maayan Geffet. 2006. [Integrating Pattern-Based and Distributional Similarity Methods for Lexical Entailment Acquisition](https://www.aclweb.org/anthology/P06-2075/). COLING-ACL 2006.

### SMT domain adaptation

Data selection is a common technique for adapting statistical translation models for a specific domain, which has been shown to both improve translation quality and to reduce model size. Selection often relies on in-domain data, of the same domain of the texts expected to be translated, selecting the sentence-pairs that are most similar to the in-domain data from a pool of parallel texts; yet, this approach holds the risk of resulting in a limited coverage, when necessary n-grams that do appear in the pool are less similar to in-domain data that is available in advance. Our research aims to find ways to bridge these two potentially contradicting considerations, while producing compact translation models.

**Selected publications:**

- Shachar Mirkin and Laurent Besacier. [Data Selection for Compact Adapted SMT Models](https://www.researchgate.net/publication/265207975_Data_Selection_for_Compact_Adapted_SMT_Models).
  AMTA 2014. [See Section 6 for a simple and very effective method for data selection / domain adaptation for machine translation]

---

## Academic service

**Program committee member / reviewer:**

W-NUT 2022 // ARR April 2022 / ACL 2022 (ARR) // W-NUT 2021 // EMNLP 2021 // EACL 2021 // COLING 2020 // *SEM 2020 // EMNLP 2020 // ACL 2020 // LREC 2020 // W-NUT 2019 // ACL 2019 // NLP+CSS 2019 // COLING 2018 // ACL 2018 // NAACL 2018 // EMNLP 2017 // *SEM 2017 // ACL 2017 // Journal of Natural Language Engineering (JNLE) 2016 // COLING 2016 // LREC 2016 // EMNLP 2016 // *SEM 2016 // EMNLP 2015 // *SEM 2015 // CICLING 2015 // Journal of Language Resources and Evaluation (LREV) 2014 //EMNLP 2014 // COLING 2014 // WMT 2014 // LREC 2014 // WMT 2013 // Journal of Language Resources and Evaluation (LREV) 2013 // IJCNLP 2013 // \*SEM 2013 // Journal of Computer Science and Technology (JCST) 2013 // WMT 2012 // EACL 2012 // LREC 2012 // ACM TIST Journal, Special Issue on Paraphrasing 2011 // EMNLP 2011 // TextInfer 2011 // COLING 2010 // EMNLP 2009 // AAAI 2008

---

## Contact

[LinkedIn](https://www.linkedin.com/public-profile/in/shacharmirkin)

[Twitter](https://twitter.com/shacharmirkin)
