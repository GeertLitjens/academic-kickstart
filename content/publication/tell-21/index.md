---
title: "Neural Image Compression for Gigapixel Histopathology Image Analysis."
date: 2021-02-01
publishDate: 2021-06-09T08:35:55.589373Z
authors: ["D. Tellez", "G. Litjens", "J. van der Laak", "F. Ciompi"]
publication_types: ["3"]
abstract: "We propose Neural Image Compression (NIC), a two-step method to build convolutional neural networks for gigapixel image analysis solely using weak image-level labels. First, gigapixel images are compressed using a neural network trained in an unsupervised fashion, retaining high-level information while suppressing pixel-level noise. Second, a convolutional neural network (CNN) is trained on these compressed image representations to predict image-level labels, avoiding the need for fine-grained manual annotations. We compared several encoding strategies, namely reconstruction error minimization, contrastive training and adversarial feature learning, and evaluated NIC on a synthetic task and two public histopathology datasets. We found that NIC can exploit visual cues associated with image-level labels successfully, integrating both global and local visual information. Furthermore, we visualized the regions of the input gigapixel images where the CNN attended to, and confirmed that they overlapped with annotations from human experts."
featured: false
publication: "*IEEE Trans Pattern Anal Mach Intell*"
doi: "10.1109/TPAMI.2019.2936841"
---

