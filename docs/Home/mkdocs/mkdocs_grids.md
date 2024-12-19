# MKDocs Grids

Grids are great for building index pages that show a brief overview of a large section of your documentation. Below I have highlighted some of the ways that the grid option can be used as part of Mkdocs Material, providing good visual information.

## Card Grids

We use "grid cards" class and fontawesome-brands-"brandname" to give visually appearing card grids. This approach works only fontawesome has expected brands and it can be found [here](https://fontawesome.com/v6/icons/markdown?f=brands&s=solid).

### syntax_1: 
```
<div class="grid cards" markdown>
- :fontawesome-brands-"brandname": __"Content to highlight"__ for content and structure
</div>
```

Example:

```
<div class="grid cards" markdown>
- :fontawesome-brands-html5: __HTML__ for content and structure
- :fontawesome-brands-js: __JavaScript__ for interactivity
- :fontawesome-brands-css3: __CSS__ for text running out of boxes
- :fontawesome-brands-internet-explorer: __Internet Explorer__ ... huh?
- :fontawesome-brands-youtube: __google cloud__ for data warehouse
</div>
```

<div class="grid cards" markdown>
- :fontawesome-brands-html5: __HTML__ for content and structure
- :fontawesome-brands-js: __JavaScript__ for interactivity
- :fontawesome-brands-css3: __CSS__ for text running out of boxes
- :fontawesome-brands-internet-explorer: __Internet Explorer__ ... huh?
- :fontawesome-brands-youtube: __YouTube__ for watching videos.
</div>


### syntax_2:

```
<div class="grid cards" markdown>
- :fontawesome-brands-markdown:{ .lg .middle } __It's just Markdown__
  "Card Contents"
  "Reference/Links"
</div>
```

Example:

```
<div class="grid cards" markdown>
-   :fontawesome-brands-markdown:{ .lg .middle } __It's just Markdown__
    ---
    Focus on your content and generate a responsive and searchable static site
    [:octicons-arrow-right-24: Markdown](https://www.markdownguide.org/)

</div>
```

<div class="grid cards" markdown>

-   :fontawesome-brands-markdown:{ .lg .middle } __It's just Markdown__

    ---

    Focus on your content and generate a responsive and searchable static site

    [:octicons-arrow-right-24: Markdown](https://www.markdownguide.org/)

</div>


### syntax_3:

::cards::

- title: "title"
  content: "Content fo the title"
  image: "image reference location"
  url: "URL Link"

::/cards::

Example:

```
::cards:: image-bg

- title: Markdown
  content: Focus on your content and generate a responsive and searchable static site.
  image: ../../mkdocs/images/markdown_mark.png
  url: https://www.markdownguide.org/

::/cards::
```

::cards:: image-bg

- title: Markdown
  content: Focus on your content and generate a responsive and searchable static site.
  image: ../../mkdocs/images/markdown_mark.png
  url: https://www.markdownguide.org/

- title: Markdown2
  content: Focus on your content and generate a responsive and searchable static site.
  image: ../../mkdocs/images/markdown_mark.png
  url: https://www.markdownguide.org/

::/cards::