+++
title = "{{ replace .Name "-" " " | title }}"

# Air date.
date = {{ .Date }}

# Schedule page publish date (NOT talk date).
publishDate = {{ .Date }}

# Authors. Comma separated list, e.g. `["Bob Smith", "David Jones"]`.
authors = []

# Name of event and optional event URL.
media_type = "show"
media_name = ""
media_url = ""

# Abstract. What's the item about?
abstract = ""

# Is this a featured item? (true/false)
featured = false

# Tags (optional).
#   Set `tags = []` for no tags, or use the form `tags = ["A Tag", "Another Tag"]` for one or more tags.
tags = []

# Projects (optional).
#   Associate this talk with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["deep-learning"]` references 
#   `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects = []

# Links (optional).
url_pdf = ""
url_video = ""

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder. 
[image]
  # Caption (optional)
  caption = ""

  # Focal point (optional)
  # Options: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight
  focal_point = ""
+++
