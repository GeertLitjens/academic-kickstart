---
title: "Efficient Out-of-Distribution Detection in Digital Pathology Using Multi-Head Convolutional Neural Networks"
date: 2020-01-01
publishDate: 2020-10-20T20:31:23.706608Z
authors: ["J. Linmans", "J. van der Laak", "G. Litjens"]
publication_types: ["2"]
abstract: "Successful clinical implementation of deep learning in medical imaging depends, in part, on the reliability of the predictions. Specifically, the system should be accurate for classes seen during training while providing calibrated estimates of uncertainty for abnormalities and unseen classes. To efficiently estimate predictive uncertainty, we propose the use of multi-head CNNs (M-heads). We compare its performance to related and more prevalent approaches, such as deep ensembles, on the task of out-of-distribution (OOD) detection. To this end, we evaluate models trained to discriminate normal lymph node tissue from breast cancer metastases, on lymph nodes containing lymphoma. We show the ability to discriminate between in-distribution lymph node tissue and lymphoma by evaluating the AUROC based on the uncertainty signal. Here, the best performing multi-head CNN (91.7) outperforms both Monte Carlo dropout (88.3) and deep ensembles (86.8). Furthermore, we show that the meta-loss function of M-heads improves OOD detection in terms of AUROC."
featured: false
publication: "*Medical Imaging with Deep Learning*"
url_pdf: "https://openreview.net/forum?id=hRwB2BTRNu"
---

