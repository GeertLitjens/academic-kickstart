+++
title = "Automated Analysis of Histopathological Clinical Trial Data"
date = 2015-04-01T12:16:34+02:00
draft = false

authors = ["geert"]

# Tags: can be used for filtering projects.
# Example: `tags = ["machine-learning", "deep-learning"]`
tags = []

# Project summary to display on homepage.
summary = "Machine learning methods were used to automatically extract and quantify biomarkers from histopathological clinical trial data."

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
  caption = ""

  # Focal point (optional)
  # Options: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight
  focal_point = ""
  preview_only = true
+++

To accuractely determine the outcome of clinical trials careful analysis of the biomarkers is required. In recent years this has become more and more complex due to quantity of biomarkers that has to be assessed in new clinical trials. Furthermore, as we move to more personalized therapy, we need to be able to measure even subtle changes in biomarker expression, putting a larger emphasis on accurate and precise biomarker quantification. These changes have made manual assessment of biomarker expression tedious, time-consuming, and, often, inaccurate. 

{{< figure src="featured.png" title="Quantification of CD3-positive cells inside (yellow) and outside (green) the invasive margin of prostate cancer (orange) specimens." width="50%">}}

Within this project, funded by the [Humboldt Foundation](https://www.humboldt-foundation.de/web/home.html), we set out to develop machine learning tools to automate the quantification and discovery of biomarkers in a variety of clinical trials. Specifically, we looked at applications in prostate cancer immunotherapy, lung cancer prognosis, and MAGE-expression in head and neck cancers. 
