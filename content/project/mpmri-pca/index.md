+++
title = "Computerized Detection of Prostate Cancer in Multi-Parametric MRI"
date = 2010-01-07T11:55:45+02:00
draft = false
authors = [""]

# Tags: can be used for filtering projects.
# Example: `tags = ["machine-learning", "deep-learning"]`
tags = []

# Project summary to display on homepage.
summary = "Automation of multi-parametric MRI diagnostics via traditional pattern recognition."

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
url_dataset = ""
url_slides = ""
url_video = ""
url_poster = ""

# Custom links (optional).
#   Uncomment line below to enable. For multiple links, use the form `[{...}, {...}, {...}]`.
# links = [{icon_pack = "fab", icon="twitter", name="Follow", url = "https://twitter.com"}]

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder. 
[image]
  # Caption (optional)
  caption = "Transversal slide through the prosate in a T2-weighted MRI sequence."

  # Focal point (optional)
  # Options: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight
  focal_point = ""
  preview_only = true
+++

Prostate cancer is the most commonly diagnosed malignancy and the second leading cause of cancer death among men in the Netherlands. Due to the shortcomings of the current diagnostic pathway for prostate cancer, especially with respect to assessing  cancer aggressiveness, alternative strategies are being investigated. Magnetic resonance imaging (MRI) has emerged as an important modality to assist and potentially replace (part of) the current diagnostic pathway. The high complexity of prostate MRI and the lack of sufficient expertise among the radiological community at large has opened the door for (semi-)automated analysis of prostate MRI by computer systems, with or without human intervention.

{{< figure src="featured.png" title="Transversal slide through the prosate in a T2-weighted MRI sequence." width="50%">}}

Within this project such as system was developed and evaluated. It consisted of several key components: segmentation of the prostate gland in MRI, discovering cancer-specific features, system development and evaluation. The results were reported through a number of publications which are listed below and summarized in my [PhD Thesis]({{< ref "/publication/litj-15-a/index.md" >}}).