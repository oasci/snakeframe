# Documentation Directory

The `docs/` directory contains the **source files for your project's documentation site**. This is where you write structured explanations, guides, tutorials, and reference material that make your code understandable and usable by others—including your future self.

Unlike docstrings or inline comments, the content in `docs/` is intended to be **user-facing** and often rendered into a static website for easy browsing. The structure and contents of this directory depend on the documentation engine you choose: `mkdocs` (the default in this template) or `sphinx`.

## Common Structure

Regardless of the tool, the `docs/` directory typically sits at the top level of your project and follows a clean, organized layout:

```
docs/
  index.md
  usage.md
  reference/
    mymodule.md
  assets/
    logo.png
    diagram.svg
```

This structure separates high-level guides (`index.md`, `usage.md`) from detailed reference material (`reference/`) and static resources like images (`assets/`). Good documentation layouts mirror how readers think and explore, not how code is structured internally.

## If Using `mkdocs` (Default)

When you use **MkDocs**, your documentation is written in Markdown (`.md`) and configured through a single file named `mkdocs.yml` in the project root—not inside the `docs/` folder.

Typical file layout:

```
mkdocs.yml         # Global configuration
docs/
  index.md         # Landing page
  installation.md  # Setup guide
  reference/
    api.md         # Manual or auto-generated API docs
  assets/
    logo.svg
```

* **Markdown files** become individual pages in the documentation site.
* **Folders** inside `docs/` help organize the content into logical sections.
* The `mkdocs.yml` file defines the navigation structure, theme, site name, and plugins.

> Note: MkDocs does not require or use `conf.py`—it reads configuration from `mkdocs.yml` instead.

This layout is intuitive and flexible, making MkDocs an excellent choice for newcomers or teams that want readable, easily written documentation.

## If Using `sphinx`

If you opt for **Sphinx**, your documentation source files are often written in reStructuredText (`.rst`) or Markdown, depending on configuration and plugins. The configuration lives in a Python script: `conf.py`.

Typical layout:

```
docs/
  conf.py           # Sphinx configuration
  index.rst         # Landing page
  usage.md          # Optional if Markdown plugin enabled
  modules/
    mymodule.rst
  _static/          # Images, CSS, etc.
  _templates/       # Custom HTML templates
```

* `conf.py` defines build options, extensions, theming, and auto-documentation behavior.
* `_static/` holds CSS, logos, or JavaScript files used in the HTML output.
* `_templates/` is optional and used for advanced HTML customization.

Sphinx is more powerful and extensible than MkDocs—particularly for projects with large APIs or that need automatic documentation from code—but it requires more setup and familiarity with the Python ecosystem.

## Auto-generated API Docs

Both MkDocs and Sphinx can include automatically generated documentation from your source code using tools like:

* [`mkdocstrings`](https://mkdocstrings.github.io/) (for MkDocs)
* `sphinx.ext.autodoc` (for Sphinx)

These tools pull docstrings from your Python code and render them into nicely formatted API reference pages. Typically, they live in a subfolder like `docs/reference/` or `docs/api/`, but the specific location is flexible.

## Static Assets

It’s common to include supporting files like images, custom CSS, or JavaScript in the documentation directory. These are usually placed in subfolders like:

```
docs/
  assets/         # Logos, diagrams
  css/            # Custom stylesheets
  js/             # Optional scripts
```

This keeps your documentation self-contained and version-controlled along with your code.

