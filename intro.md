---
jupytext:
  cell_metadata_filter: -all
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Data+AI Lab knowledge base

This website provides an introduction to all things related to data science and AI, based on the collective experience from all researchers in the Data+AI lab. The scope of this page is very broad: From a gentle introduction into the basics of data science to a deep dive in the fundamentals of explainable AI. Of course, a lot of great educational material already exists around the majority of the topics covered here, so we provide links for further reading wherever we can. 

First and foremost, we intend this to be a *practical* site for students and researchers who are eager to learn more about data science or AI, or are looking for ways to use any of these technologies in their projects. 

The topics covered in this knowledge base are structured as follows:

```{code-cell}
:tags: ["remove-input"]

from generate_full_toctree import generate_full_toctree, pretty_print_toctree

toctree = generate_full_toctree()
pretty_print_toctree(toctree)
```
