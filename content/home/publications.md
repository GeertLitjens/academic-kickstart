+++
# Recent Publications widget.
# This widget displays recent publications from `content/publication/`.
widget = "pages"
active = true
date = 2016-04-20T00:00:00
headless = true

title = "Recent Publications"
subtitle = ""

# Order that this section will appear in.
weight = 4

[content]
# Number of publications to list.
count = 5
offset = 0
page_type = "publication"
order = "desc"

# Filter posts by a taxonomy term.
  [content.filters]
    tag = ""
    category = ""
    exclude_featured = false
    
    # Filter by publication type.
    # -1: Any
    #  0: Uncategorized
    #  1: Conference proceedings
    #  2: Journal
    #  3: Work in progress
    #  4: Technical report
    #  5: Book
    #  6: Book chapter
    
    publication_type = ""


[design]
  # Toggle between the various page layout types.
  #   1 = List
  #   2 = Compact
  #   3 = Card
  #   4 = Citation (publication only)
  view = 4

[design.background]
  # Apply a background color, gradient, or image.
  #   Uncomment (by removing `#`) an option to apply it.
  #   Choose a light or dark text color by setting `text_color_light`.
  #   Any HTML color name or Hex value is valid.
    
  # Background color.
  # color = "navy"
  
  # Background gradient.
  # gradient_start = "DeepSkyBlue"
  # gradient_end = "SkyBlue"
  
  # Background image.
  # image = "background.jpg"  # Name of image in `static/img/`.
  # image_darken = 0.6  # Darken the image? Range 0-1 where 0 is transparent and 1 is opaque.

  # Text color (true=light or false=dark).
  # text_color_light = true  
  
[advanced]
 # Custom CSS. 
 css_style = ""
 
 # CSS class.
 css_class = ""
+++

