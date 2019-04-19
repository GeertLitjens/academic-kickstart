+++
title = "CAMELYON"
date = 2016-01-22T22:00:35+01:00
draft = false
share = false

# Tags: can be used for filtering projects.
# Example: `tags = ["machine-learning", "deep-learning"]`
tags = ["Active", "Challenge", "Lymph Nodes", "Metastases", "Machine Learning"]

# Project summary to display on homepage.
summary = "Detection of breast cancer metastases in lymph nodes."

# Slides (optional).
#   Associate this page with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references 
#   `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
slides = ""

# Optional external URL for project (replaces project detail page).
external_link = ""

# Links (optional).
url_pdf = ""
url_code = ""
url_dataset = "http://www.gigadb.org/dataset/100439"
url_slides = ""
url_video = ""
url_poster = ""

# Custom links (optional).
#   Uncomment line below to enable. For multiple links, use the form `[{...}, {...}, {...}]`.
# url_custom = [{icon_pack = "fab", icon="twitter", name="Follow", url = "https://twitter.com"}]

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder. 
[image]
  # Caption (optional)
  caption = "Detection of breast cancer metastases in lymph nodes."

  # Focal point (optional)
  # Options: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight
  focal_point = "Smart"
  
  preview_only = true
+++

## Overview

Built on the success of its predecessor, CAMELYON17 is the second grand challenge in pathology organised by the Diagnostic Image Analysis Group (DIAG) and Department of Pathology of the Radboud University Medical Center (Radboudumc) in Nijmegen, The Netherlands.

The goal of this challenge is to evaluate new and existing algorithms for automated detection and classification of breast cancer metastases in whole-slide images of histological lymph node sections. This task has high clinical relevance and would normally require extensive microscopic assessment by pathologists. The presence of metastases in lymph nodes has therapeutic implications for breast cancer patients. Therefore, an automated solution would hold great promise to reduce the workload of pathologists while at the same time reduce the subjectivity in diagnosis.

{{< figure src="featured.png" title="Detection of breast cancer metastases in lymph nodes." width="50%">}}

## Task

The TNM system is an internationally accepted means to classify the extent of cancer spread in patients with a solid tumour. It is one of the most important tools for clinicians to help them select a suitable treatment option and to obtain an indication of prognosis. Since the histological assessment of lymph node metastases is an essential part of TNM classification, CAMELYON17 will focus on the pathologic N-stage, in short: pN-stage.

In clinical practice several lymph nodes are surgically removed after which these nodes are processed in the pathology laboratory. In this challenge we forged **artificial patients**, with 5 slides provided for each patient where each slide corresponds to exactly one lymph node.

The task in this challenge is to **determine a pN-stage for every patient in the test dataset**. To compose a pN-stage, the number of positive lymph nodes (i.e. nodes with a metastasis) are counted. For the evaluation of the results we use five class quadratic weighted kappa where the classes are the pN-stages.

## Website

Further information, registration, and the results are available on the [challenge website](https://camelyon17.grand-challenge.org).