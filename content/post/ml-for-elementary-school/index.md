+++
title = "CAMELYON for Elementary School"
subtitle = ""

# Add a summary to display on homepage (optional).
summary = "In 2018 Jeroen van der Laak and I were nominated and eventually won a Radboud Science Award for our work with the CAMELYON challenge. One part of the prize was the oppertunity to turn our research into an educational program for elementary schools, specifically ages 9 till 12. This post is a summary of my experience going through this process and showcases the things we developed."

date = 2019-04-19T13:41:14+02:00
draft = false

# Authors. Comma separated list, e.g. `["Bob Smith", "David Jones"]`.
authors = ["Geert Litjens"]

# Is this a featured post? (true/false)
featured = false

# Tags and categories
# For example, use `tags = []` for no tags, or the form `tags = ["A Tag", "Another Tag"]` for one or more tags.
tags = ["teaching", "radboud science award", "elementary school"]
categories = []

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["deep-learning"]` references 
#   `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
# projects = ["internal-project"]

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

In 2018 [Jeroen van der Laak](https://www.computationalpathologygroup.eu/members/jeroen-van-der-laak/) and I were nominated and eventually won a Radboud Science Award for our work with the CAMELYON challenge. One part of the prize was the oppertunity to turn our research into an educational program for elementary schools, specifically ages 9 till 12. This post is a summary of my experience going through this process and showcases the things we developed. Luckily, we were not in this alone and we got great support from the [Radboud Wetenschapsknooppunt](https://www.ru.nl/wetenschapsknooppunt/) and two of our PhD students: [Meyke Hermsen](https://www.computationalpathologygroup.eu/members/meyke-hermsen/) and [Maschenka Balkenhol](https://www.computationalpathologygroup.eu/members/maschenka-balkenhol/). In addition, the kids from the elemantary schools also made a great introductory for us:

{{<youtube UHsXJe_fXgY>}}

An 'educational program' might sound a bit vague, so I'll dive into some specifics. The idea was to develop in total six activities which the children could do under supervision of their teachers (and partly by themselves) which would guide them through the background and the different steps of our research. These activities would take place over the course of several weeks in which there would be lessons to prepare, execute, present, and provide feedback on the activities. In the end the children need to define their own research questions in relation to the activities and execute it. The biggest challenge was to build these activities in such a way that they stay true to our research results but are also understandable for children of varying ages.

We quickly decided to split our research into two separate components with separate activities which would come together in the final activity. The two components were: histopathological diagnostics and artificial intelligence. In the end we came up with these six activities:

1. When are computers intelligent?
2. What are applications of artifical intelligence you encounter?
3. How do you train a smart computer?
4. What is a diagnosis and how do you perform one?
5. How does a pathologist do diagnoses?
6. Diagnosing cancer with artificially intelligent computers.

The fist two activities were aimed at getting a discussion going in the classroom on what the definition of intelligence is. Think along the lines of: Is a calculator intelligent? Or a navigation system? Secondly, the children were asked to discuss this at home and find examples of devices in their own house which they think were intelligent. In the end we would provide them with what we, within this project, mean with artificial intelligence: a computer program which automatically learns by example and can generalize what is learned this to unknown situations; similarly to the way they learn new skills.

The third activity was the first real hands-on activity for which I adapted the excellent webapp [Teachable Machine](https://teachablemachine.withgoogle.com/) by Google. I translated the app to Dutch and made some fixes for tablets and phones so it would be easier to use in the classroom. My adaptation can be found [here](https://geertlitjens.github.io/teachable-machine/), with the source code [here](https://github.com/GeertLitjens/teachable-machine). This webapp allows you to train a three-class classifier with your webcam. One fun application is to turn hand-gestures into instruments, as depicted in the video below.

{{<youtube oP8-_0ZyY3U>}}

The idea of this activity was that children can figure out what a computer can easily learn and what is more difficult. For example, if you teach it to react to your face, will it also react to your friend's face? Can it discriminate between your left and right hand? And if it doesn't, what do you need to do to make it learn the difference. Many challenges that actually appear in machine learning, like bias, can be explored this way in a playful manner. 

The next two activities completely moved away from artifical intelligence and focused on a key job of a doctor: obtaining a diagnosis. In activity 4 we developed several disease scenarios and the children had to identify what questions you need to ask to figure out what disease the person has. Specifically, we had a scenario where a child was either suffering from food poisoning or the flu. This activity intends to show how the process of a diagnosis works and how, by asking the right questions, you can narrow down your options and eventually figure out what ails the patient.

Activity 5 move to the domain of histopathology. Here we introduced the microscope and concept of 'good' cells and 'bad' cells (cancer). We prepared a lot of images (one example below) to show the children the differences in appearance and how a pathologist, with a microscope, can see what is wrong with a patient. We also gave them a couple of images were they had to figure out themselves what were the good and bad cells. 

The last activity combined artificial intelligence and histopathological diagnostics. Here again we used a [webapp](https://geertlitjens.github.io/metastaticcellclassifier/index.html) (source [here](https://github.com/GeertLitjens/metastaticcellclassifier)) which I made based of the [face classifier](https://github.com/brendansudol/faces) by Brendan Sudol. Here the students could upload images with cells and the computer would tell them whether they were good or bad. Initially they had to classify these images themselves and then see if the computer agreed. Additionally, they could try to find cases were they think the computer was wrong and see if a pattern could be established. This way they could interactively explore the limitations of this simple 'smart' computer system.

{{< figure src="featured.png" title="Example of the webapp for cell classification." width="50%">}}

After the activities were finished a group of teacher at elementary school ['de Gazelle'](https://www.po.deltascholen.org/BS-de-Gazelle/) in Arnhem tested the lessons at their school. We visited roughly halfway and gave a presentation after which the kids had the oppertunity to ask questions. I had a lot of fun and got great feedback, both from the teachers and the children.

Currently, we are in the phase of wrapping up the project. Our package of lessions and activities will be bundled in a book such that other schools can also use it. This book will be available through the [Radboud Wetenschapsknooppunt](https://www.ru.nl/wetenschapsknooppunt/). Last, we will give a presentation about this project at the Winterschool organized by the Wetenschapsknooppunt for teachers to share our experience.

All in all, it was great to see the enthusiasm for our research in both the teachers and the children and for me it was a very rewarding experience. If you are interested in any of the materials or the project, don't hesitate to reach out to me.