---
title: "Residual cyclegan for robust domain transformation of histopathological tissue slides."
date: 2021-05-01
publishDate: 2021-06-09T08:35:55.630403Z
authors: ["T. de Bel", "J. Bokhorst", "J. van der Laak", "G. Litjens"]
publication_types: ["3"]
abstract: "Variation between stains in histopathology is commonplace across different medical centers. This can have a significant effect on the reliability of machine learning algorithms. In this paper, we propose to reduce performance variability by using -consistent generative adversarial (CycleGAN) networks to remove staining variation. We improve upon the regular CycleGAN by incorporating residual learning. We comprehensively evaluate the performance of our stain transformation method and compare its usefulness in addition to extensive data augmentation to enhance the robustness of tissue segmentation algorithms. Our steps are as follows: first, we train a model to perform segmentation on tissue slides from a single source center, while heavily applying augmentations to increase robustness to unseen data. Second, we evaluate and compare the segmentation performance on data from other centers, both with and without applying our CycleGAN stain transformation. We compare segmentation performances in a colon tissue segmentation and kidney tissue segmentation task, covering data from 6 different centers. We show that our transformation method improves the overall Dice coefficient by 9% over the non-normalized target data and by 4% over traditional stain transformation in our colon tissue segmentation task. For kidney segmentation, our residual CycleGAN increases performance by 10% over no transformation and around 2% compared to the non-residual CycleGAN."
featured: false
publication: "*Med Image Anal*"
tags: ["Adversarial networks; Histopathology; Stain normalization; Structure segmentation"]
doi: "10.1016/j.media.2021.102004"
---

