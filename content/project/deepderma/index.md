+++
# Project title.
title = "DeepDerma"

# Date this page was created.
date = 2020-05-11T00:00:00

share = false

# Project summary to display on homepage.
summary = "Improving efficiency and accuracy of skin cancer diagnostics."

# Tags: can be used for filtering projects.
# Example: `tags = ["machine-learning", "deep-learning"]`
tags = ["Active", "Machine Learning", "Skin Cancer", "Computational Pathology"]

authors = ["geert"]

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
  caption = "Annotation of a Basal Cell Carcinoma, a skin cancer with, typically, good prognosis."
  
  # Focal point (optional)
  # Options: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight
  focal_point = "BottomRight"

  preview_only = true
+++

Due to the tripling of skin cancer incidence over the past two decades, more skin biopsies and resections are performed than ever before. This has led to an enormous increase in workload for pathologists, who perform the microscopic diagnostics of skin samples.
Most of microscopic skin analysis is not professionally challenging, but it is time consuming and can lead to reduced time for more complex diagnostics and increased wait time for patients. Machine learning and specifically deep learning offers a path to automating the diagnoses of skin samples, which would reduce the pressure on pathologists and the cost of diagnosis, both in time and money.

{{< figure src="featured.png" title="Annotation of a Basal Cell Carcinoma, a skin cancer with, typically, good prognosis." width="50%">}}

We propose not just to develop an algorithm which can perform skin diagnostics at the level of an expert pathologist, but also explicitly identify the most fruitful way of integrating these algorithms into the routine workflow. This project is exceedingly timely, as by the end of 2019 all histopathological diagnostics in the Radboud University Medical Center will be done digitally.

The project consists of four work packages. In work package 1, we will collect a large retrospective cohort of annotated and labeled skin biopsies and resections from multiple centers. The focus of work package 2 is on development of algorithms for segmentation of different skin tissue classes, subtyping of basal cell carcinoma, and identification of rare incidental findings. Work package 3 and 4 cover the development and prospective evaluation of the optimal algorithm-integrated workflow in a real world clinical setting.

After completion, we will have the world’s first prospectively evaluated algorithm-supported workflow for digital pathology, and a valuable, expert labeled, retrospective dataset of skin specimens; both excellent targets for valorization. Last, it will increase the time of pathologists for complex diagnostics and reduce the wait time for patients.