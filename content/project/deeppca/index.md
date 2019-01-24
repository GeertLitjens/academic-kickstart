+++
# Project title.
title = "Deep PCa"

# Date this page was created.
date = 2018-01-22T00:00:00

share = false

# Project summary to display on homepage.
summary = "Less unnecessary surgery and adjuvant therapy for prostate cancer patients through digital pathology and deep learning."

# Tags: can be used for filtering projects.
# Example: `tags = ["machine-learning", "deep-learning"]`
tags = ["Deep Learning", "Prostate Cancer", "Computational Pathology"]

# Optional external URL for project (replaces project detail page).
external_link = ""

# Slides (optional).
#   Associate this project with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references 
#   `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
slides = ""

# Links (optional).
url_pdf = ""
url_slides = ""
url_video = ""
url_code = ""

# Custom links (optional).
#   Uncomment line below to enable. For multiple links, use the form `[{...}, {...}, {...}]`.
# url_custom = [{icon_pack = "fab", icon="twitter", name="Follow", url = "https://twitter.com/georgecushen"}]

# Featured image
# To use, add an image named `featured.jpg/png` to your project's folder. 
[image]
  # Caption (optional)
  caption = "Result of prostate cancer segmentation using convolutional neural networks."
  
  # Focal point (optional)
  # Options: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight
  focal_point = "BottomRight"

  preview_only = true
+++

Most men die with, not because of prostate cancer. This high incidence-to-mortality ratio sounds like a positive trait, but comes with its own share of problems: high risk of overdiagnosis and overtreatment with significant patient morbidity. To combat overtreatment, several models have been developed to assign patients to risk categories with differing treatment regimes. Although these models show good correlation with patient outcome on the group level, their benefit for the individual patient remains limited.

{{< figure src="featured.png" title="Prostate cancer segmentation using convolutional neural networks." width="90%">}}

Several groups have shown that quantifying the tumour and its micro-environment at the cellular level can result in biomarkers with strong prognostic potential, for example tumour/stroma ratio, the presence and composition of immune infiltrates or the amount of proliferating (Ki67-positive) cells. However, these findings have not translated to clinical practice due to the cumbersome and subjective manual extraction of these biomarkers from tissue slides.

Recent years have seen the more widespread introduction of whole-slide imaging systems, which for the first time allow computerized processing of tissue slides. Automated extraction of aforementioned quantitative biomarkers through image analysis can achieve the required accuracy and robustness to impact clinical practice. In tandem with these developments, computer vision has seen a machine learning revolution over the past decade due to the advent of deep learning.

In this project, we will combine deep learning and digitized whole-slide imaging of prostate cancer for reproducible extraction of quantitative biomarkers. Furthermore, due to the ability of deep learning systems to learn relevant features without human intervention, we expect to identify novel biomarkers which allow us to further improve the current risk models.

The aim of this project is to prevent unnecessary surgery and adjuvant therapy for individual patients by improving currently established risk models. Risk models will be enhanced through the addition of pre- and post-operative quantitative biomarkers obtained via image analysis and deep learning. We will focus both on the accurate and objective quantification of biomarkers already identified in literature and the discovery of novel biomarkers.
