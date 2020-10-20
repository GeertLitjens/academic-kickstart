---
title: "Streaming convolutional neural networks for end-to-end learning with multi-megapixel images"
date: 2020-08-01
publishDate: 2020-10-20T20:31:23.674944Z
authors: ["H. Pinckaers", "B. van Ginneken", "G. Litjens"]
publication_types: ["3"]
abstract: "Due to memory constraints on current hardware, most convolution neural networks (CNN) are trained on sub-megapixel images. For example, most popular datasets in computer vision contain images much less than a megapixel in size (0.09MP for ImageNet and 0.001MP for CIFAR-10). In some domains such as medical imaging, multi-megapixel images are needed to identify the presence of disease accurately. We propose a novel method to directly train CNNs using any input image size end-to-end. This method exploits the locality of most operations in modern CNNs by performing the forward and backward pass on smaller tiles of the image. In this work, we show a proof of concept using images of up to 66-megapixels (8192x8192), saving approximately 50GB of memory per image. Using two public challenge datasets, we demonstrate that CNNs can learn to extract relevant information from these large images and benefit from increasing resolution. We improved the area under the receiver-operating characteristic curve from 0.580 (4MP) to 0.706 (66MP) for metastasis detection in breast cancer (CAMELYON17). We also obtained a Spearman correlation metric approaching state-of-the-art performance on the TUPAC16 dataset, from 0.485 (1MP) to 0.570 (16MP). The code to reproduce a subset of the experiments is available at https://github.com/DIAGNijmegen/StreamingCNN."
featured: false
publication: "*IEEE Trans Pattern Anal Mach Intell*"
doi: "10.1109/TPAMI.2020.3019563"
---

