# Auxiliary Files

In addition to your source code, tests, and documentation, a professional Python project includes a set of supporting files in the project root.
These are called auxiliary files.
They don’t contain code, but they define policies, provide metadata, and support tooling that make your project robust, maintainable, and contributor-friendly.

New developers often overlook these files, but they play a critical role in making your code understandable and usable—especially in collaborative, research, or open-source environments.

Here’s an overview of the most important auxiliary files in this template:

## `.gitignore`

This file tells Git which files and directories it should ignore when tracking changes.
This prevents large, temporary, or machine-specific files (like Python bytecode, virtual environments, and logs) from being added to your version control history.

A typical `.gitignore` includes entries like:

```
__pycache__/
*.pyc
.env
.cache/
*.log
```

It helps keep your repository clean and focused on source files and assets that matter.

## `README.md`

The README is the front page of your project.
It’s the first thing users and collaborators see when they visit your repository.
It typically lives at the root of your project and is written in Markdown.

A well-structured README includes:

* A short project description
* Installation instructions
* Example usage
* Links to documentation
* Contributor information

Even in early-stage projects, writing a README early helps you clarify your goals and communicate them clearly.

## `CHANGELOG.md`

The changelog is a chronological list of notable changes made to the project across versions.
It’s helpful for users, contributors, and future maintainers to understand what changed, when, and why.

This file typically uses a versioned structure like:

```
# [1.2.0] - 2025-04-02
## Added
- Support for new simulation models
- CLI flag for verbosity

## Fixed
- Bug in data export for large structures
```

Maintaining a changelog is especially important in academic or research tools where reproducibility depends on knowing what version was used.

## `CODE_OF_CONDUCT.md`

This file outlines expectations for behavior in the project's community and defines how to report unacceptable behavior.
It’s especially important for public-facing or collaborative projects.

Even if your team is small, a code of conduct:

* Sets the tone for inclusive, respectful communication
* Provides clarity on how issues will be handled
* Signals professionalism and openness to contributors

This template includes a standard Contributor Covenant–style code of conduct that you can adapt to your team or organization’s needs.

## `LICENSE` or `LICENSE.md`

This file defines the legal terms under which others can use, modify, and share your code.
It is a required part of any open-source project.
Even internal or academic projects benefit from having a clear license.

Depending on your selection during project generation (`MIT`, `Apache-2.0`, etc.), this file will be pre-populated with the appropriate text and include your name and year.

A project without a license is not open source, and others technically have no right to use or contribute to it—even if it’s public.

## `pyproject.toml`, `pixi.toml`, and Tooling Configs

While not always classified as "auxiliary," configuration files like `pyproject.toml` and `pixi.toml` also live at the project root and are central to how your project is built, linted, and run.
These are covered in detail in earlier sections, but it’s worth noting that keeping all key configs at the top level of your repository is a standard convention.
