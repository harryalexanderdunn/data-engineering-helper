# Material for Mkdocs

## What is it?

MkDocs is a fast, simple and downright gorgeous static site generator that's geared towards building project documentation. Documentation source files are written in Markdown, and configured with a single YAML configuration file. Material is a version of mkdocs which provides added customisation and extensions that you cannot get on regular Mkdocs.

The main benefits of using material include it being fast, lightweight, open source and built for everyone. The main benefit of material is the plugins that you can use with the site. This includes a mermaid2 plugin, mono-repo/multi-repo plugins etc, more plugins will be added as the site grow. See below for available plugins with material.

[Material for Mkdocs site](https://squidfunk.github.io/mkdocs-material/)

---

## Trusted in the industry

Industry leaders, as well as many successful Open Source projects, rely on Material for MkDocs to create professional and beautiful documentation – no frontend experience required. Choose a mature and actively maintained solution and start writing in minutes.

We are currently not a sponsor so only have the open source package. However, this is more than enough to utilise documentation as code efficiently.

## Getting started

Material for MkDocs is a powerful documentation framework on top of [MkDocs],
a static site generator for project documentation.[^1] If you're familiar with 
Python, you can install Material for MkDocs with [`pip`][pip], the Python
package manager. If not, we recommend using [`docker`][docker].

  [^1]:
    In 2016, Material for MkDocs started out as a simple theme for MkDocs, but
    over the course of several years, it's now much more than that – with the
    many built-in plugins, settings, and countless customization abilities,
    Material for MkDocs is now one of the simplest and most powerful frameworks
    for creating documentation for your project.

  [MkDocs]: https://www.mkdocs.org
  [pip]: #with-pip
  [docker]: #with-docker

## Installation

### with pip <small>recommended</small> { #with-pip data-toc-label="with pip" }

Material for MkDocs is published as a [Python package] and can be installed with
`pip`, ideally by using a [virtual environment]. Open up a terminal and install
Material for MkDocs with:

=== "Latest"

    ``` sh
    pip install mkdocs-material
    ```

=== "9.x"

    ``` sh
    pip install mkdocs-material=="9.*" # (1)!
    ```

    1.  Material for MkDocs uses [semantic versioning][^2], which is why it's a
        good idea to limit upgrades to the current major version.

        This will make sure that you don't accidentally [upgrade to the next
        major version], which may include breaking changes that silently corrupt
        your site. Additionally, you can use `pip freeze` to create a lockfile,
        so builds are reproducible at all times:

        ```
        pip freeze > requirements.txt
        ```

        Now, the lockfile can be used for installation:

        ```
        pip install -r requirements.txt
        ```

  [^2]:
    Note that improvements of existing features are sometimes released as
    patch releases, like for example improved rendering of content tabs, as
    they're not considered to be new features.

This will automatically install compatible versions of all dependencies:
[MkDocs], [Markdown], [Pygments] and [Python Markdown Extensions]. Material for
MkDocs always strives to support the latest versions, so there's no need to
install those packages separately.

---

:fontawesome-brands-youtube:{ style="color: #EE0F0F" }
__[How to set up Material for MkDocs]__ by @james-willett – :octicons-clock-24:
15m – Learn how to create and host a documentation site using Material for 
MkDocs on GitHub Pages in a step-by-step guide.

  [How to set up Material for MkDocs]: https://www.youtube.com/watch?v=Q-YA_dA8C20

---

__Tip__: If you don't have prior experience with Python, we recommend reading 
[Using Python's pip to Manage Your Projects' Dependencies], which is a really
good introduction on the mechanics of Python package management and helps you
troubleshoot if you run into errors.

  [Python package]: https://pypi.org/project/mkdocs-material/
  [virtual environment]: https://realpython.com/what-is-pip/#using-pip-in-a-python-virtual-environment
  [semantic versioning]: https://semver.org/
  [Markdown]: https://python-markdown.github.io/
  [Pygments]: https://pygments.org/
  [Python Markdown Extensions]: https://facelessuser.github.io/pymdown-extensions/
  [Using Python's pip to Manage Your Projects' Dependencies]: https://realpython.com/what-is-pip/
