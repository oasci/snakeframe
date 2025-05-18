# Creating Your Project

To create a new project using this template:

```bash
cookiecutter gh:oasci/snakeframe
```

You'll be prompted to fill in some fields, such as:

- `project_name`: A human-readable name for your project (e.g.
"Snake Vision")
- `repo_name`: The name of the folder/repository (e.g.
`snake_vision`)
- `author_name`, `email`, etc.

Once the process finishes, a new folder will be created with a full scaffold of your project.

## `project_name`

Default: `python_project`

The `project_name` is the human-readable name of your project.
It appears in documentation, user interfaces, titles, and descriptive metadata files like `pyproject.toml` and `pixi.toml`.
This name is how people will refer to and remember your project, so it’s worth taking time to choose something that is meaningful, clear, and polished.

Here is some advice to think about:

- A good project name helps communicate the purpose of your tool, establishes a professional tone, and can make your work more memorable and discoverable.
- A strong project name should be short, easy to say, and ideally relevant to the domain or purpose of your software.
- It’s recommended to avoid names that are too long, generic, or difficult to pronounce.
- If your project name will eventually appear in publications, portfolios, or even a PyPI package or GitHub repository, its clarity and uniqueness will matter.
- Use only lowercase letters and underscores (`_`) when necessary, avoiding spaces or special characters.
- A name like `snake_vision` or `bio_stats_toolkit` is clean, readable, and compatible with most file systems and tools.
- Avoid names like `My Cool Tool`, `script-final-2023`, or `test_project_2`, which can seem temporary or unclear.
  While these names may work locally, they don’t scale well when shared with others or published online.

Before finalizing your project name, it's a good idea to check whether the name is already in use.
This includes checking GitHub repositories, PyPI packages, and domains.
The [NameChecker tool](https://namechecker.vercel.app/) can help you search across multiple platforms to see if your desired name is available.
Even if you’re not planning to publish the project yet, choosing a unique name now avoids conflicts later and reflects a habit of thinking ahead.

Here are a few real-world examples of well-chosen project names:

- `fastapi` — communicates performance and its focus on APIs.
- `cookiecutter` — uses a strong metaphor for reusable templates.
- `scikit-learn` — combines “SciKit” (scientific toolkit) and “learn” to suggest its focus on machine learning.

A good test of a project name is to imagine saying it out loud in a meeting or presentation.
If it sounds awkward or hard to explain, try a different one.
Some developers find it useful to write a one-sentence summary of what the project does and pick a name that reflects that idea.
For example, if your tool analyzes snake movement patterns using computer vision, `snake_vision` is clear and directly tied to its purpose.

## `project_description`

Default: based on the `project_name`

The `project_description` is a concise, one-sentence summary of what your project does.
It should clearly and accurately communicate the purpose or functionality of your tool to someone who’s never seen it before.
This sentence often appears at the top of your project’s README, in metadata fields (like in `pyproject.toml` or `setup.cfg`), and in documentation sites.

Aim to be informative but succinct.
A well-written description allows someone to immediately understand whether the project is relevant to their needs.
Avoid vague statements like “A Python project” or “Scripts for my code.” Instead, focus on what your project enables users to do or what problem it solves.

For example:

- “A lightweight toolkit for analyzing snake movement in scientific video data.”
- “An extensible CLI for managing large-scale neuroimaging workflows.”
- “A high-performance Python library for real-time statistical monitoring.”

Use active, descriptive language and include keywords that might help with searchability or context.
A good rule of thumb is to imagine the description as the single sentence you'd include in a class project submission or on your portfolio.

## `organization`

Default: based on the `project_name`

The `organization` field is used to specify the GitHub/GitLab username or organization name that will own the repository.
This value is typically used in generated URLs (such as for badges or links in the README), and it determines where the project will live —for example, `https://github.com/organization/project_name`.
You should enter either your personal username or the name of the organization under which the project will be maintained.

## `license`

Default: `Apache-2.0`

The `license` field determines the legal terms under which your project can be used, modified, and redistributed.
Choosing the right license is an important decision—it affects how others can collaborate with or build upon your work.
This template supports four widely used open-source licenses: `Apache-2.0`, `MIT`, `BSD-3-Clause`, and `GPL-3.0-only`.
Each comes with trade-offs in terms of permissiveness, legal protection, and compatibility with other projects.

### Apache-2.0

A permissive open-source license that also includes explicit patent protection.

- **Pros**:
    - Allows commercial use, modification, and redistribution.
    - Protects users from patent litigation.
    - Encourages contribution while offering legal safety.
- **Cons**:
    - Slightly more complex than MIT or BSD due to patent clauses.
    - Some developers may find it overly formal for small projects.
- **Used by**:
    - [Apache Airflow](https://github.com/apache/airflow)
    - [TensorFlow](https://github.com/tensorflow/tensorflow)
    - [spaCy](https://github.com/explosion/spaCy)

### MIT

A very simple and permissive license that allows almost unrestricted use.

- **Pros**:
    - Extremely easy to understand and implement.
    - Encourages wide adoption and contribution.
    - Minimal legal overhead.
- **Cons**:
    - Does not include patent protection.
    - Offers minimal liability protection for authors.
- **Used by**:
    - [Flask](https://github.com/pallets/flask)
    - [requests](https://github.com/psf/requests)
    - [Django REST Framework](https://github.com/encode/django-rest-framework)

### BSD-3-Clause

Similar to MIT in permissiveness but with a few extra clauses around attribution.

- **Pros**:
    - Permissive and business-friendly.
    - Slightly more formal than MIT; includes non-endorsement and attribution clauses.
- **Cons**:
    - Slightly more complex than MIT.
    - Still does not include patent protection.
- **Used by**:
    - [SciPy](https://github.com/scipy/scipy)
    - [Pandas](https://github.com/pandas-dev/pandas)
    - [Matplotlib](https://github.com/matplotlib/matplotlib)

### GPL-3.0-only

A strong copyleft license that requires derivative works to also be open source.

- **Pros**:
    - Protects software freedom—any derivative work must also be open source under the same license.
    - Ideal for projects aiming to stay in the open-source ecosystem.
- **Cons**:
    - Not compatible with many proprietary/commercial uses.
    - Some developers and companies avoid using GPL-licensed code due to its viral nature.
- **Used by**:

    - [GNU Bash](https://www.gnu.org/software/bash/)
    - [GIMP](https://www.gimp.org/)
    - [GNU Octave](https://www.gnu.org/software/octave/)


If you're unsure which license to choose, `Apache-2.0` is a safe default that offers a good balance between openness and legal protection.
However, for small personal projects, many developers prefer the simplicity of the `MIT` license.
If you're contributing to the scientific Python ecosystem, `BSD-3-Clause` is a common and compatible choice.
Choose `GPL-3.0-only` only if you intend to ensure that all downstream work remains open source.

For additional guidance, you can explore [choosealicense.com](https://choosealicense.com/) or consult your institution or organization if legal constraints apply.

## `min_python_version`

Default: `3.9`

The `min_python_version` field sets the lowest version of Python that your package officially supports.
This is used in places like `pyproject.toml` to define compatibility constraints and helps tooling, users, and continuous integration systems understand which Python interpreters can run your project.

Choosing the right minimum version depends on your needs and audience.
Setting it too low may require workarounds for older syntax and missing standard library features.
Setting it too high may exclude users on older systems or distributions.
A good rule of thumb is to support the oldest version you actively test against and use features from.

For example, Python 3.9 introduced new dictionary merge operators (`|`), updated type hint syntax, and improvements to the standard library.
If your codebase uses any of these features, earlier versions won’t be compatible.

Here’s a brief overview of some key Python versions:

- 3.9: Improved type hinting (`list[int]` instead of `List[int]`), `zoneinfo`, dictionary merge operators.
- 3.10: Structural pattern matching (`match/case`), better error messages, `typing.TypeGuard`.
- 3.11: Major speed improvements (\~10–60% faster), exception groups, fine-tuned error tracebacks.
- 3.12: Continued performance improvements, cleaner deprecations, more static typing enhancements.

If you're starting a new project and don't have strict compatibility requirements, it’s reasonable to choose Python 3.9 or higher.
It’s widely supported and avoids compatibility issues present in older 3.x versions.
Always make sure your project’s code, dependencies, and tests are compatible with the version you specify here.

## `dev_python_version`

Default: `3.12`

The `dev_python_version` sets the specific version of Python that will be used during local development.
This version defines the Python interpreter used in your virtual environment, development tools, linters, type checkers, and test runners.
It is also the version installed and managed by tools like Pixi or conda when setting up your development environment from scratch.

This value does not restrict the versions your project supports (that’s handled by `min_python_version`).
Instead, it ensures your development workflow is consistent, reproducible, and up to date with the latest language features and performance improvements.

Choosing a modern Python version like `3.12` is a good default.
It brings the latest syntax, runtime optimizations, and typing enhancements, making your development experience smoother and more efficient.
However, you should make sure that your development version is equal to or greater than your minimum supported version—ideally no more than one or two versions ahead, so you don’t accidentally introduce features or behavior not available in supported releases.

If you are collaborating with others, especially in educational or institutional settings, it’s helpful to document this clearly and ensure everyone is using the same version.
This prevents subtle issues where code works locally but fails in CI or on other machines.
Tools like Pixi will automatically use this setting to create a consistent environment, so your development tooling “just works” out of the box.

## `git_host`

Default: `GitHub`

The `git_host` field specifies which platform you will use to host your project’s Git repository.
This template supports either `GitHub` or `GitLab`, and the selected value determines how URLs for badges, remote links, and CI/CD configurations are generated.

By default, the host is set to `GitHub`, which is the most widely used Git hosting platform in the open-source community.
If your institution or team prefers `GitLab`, whether self-hosted or on gitlab.com, you can choose that instead.

While both platforms offer similar core features—issue tracking, pull/merge requests, wikis, CI/CD pipelines, and permissions—they have some differences in ecosystem and defaults.
GitHub is generally more popular in open-source communities, with broad support across documentation generators, dependency tools, and continuous integration platforms like GitHub Actions.
GitLab, on the other hand, is often favored for internal enterprise use and provides more built-in DevOps tools out of the box.

## `docs`

Default: `mkdocs`

The `docs` field determines which documentation framework will be used to build and manage your project’s documentation site.
You can choose between `mkdocs` and `sphinx`, two popular and widely adopted static site generators in the Python ecosystem.

The default is `mkdocs`, which is known for its simplicity, fast setup, and clean, modern output.
It’s Markdown-based, making it very approachable—especially for new developers or teams that prefer writing in plain text with minimal configuration.
It integrates well with MkDocs Material, a widely used theme, and supports easy deployment to GitHub Pages.

Alternatively, `sphinx` is a more powerful and extensible documentation engine built with Python in mind.
It supports both reStructuredText and Markdown (with extensions), and it excels at auto-generating documentation from docstrings using tools like `autodoc`, `napoleon`, and `autosummary`.
It’s the standard in the scientific Python community and is particularly strong for large, API-heavy libraries where automated documentation is essential.

Use `mkdocs` if:

- You want fast, clean, easy-to-maintain documentation.
- You prefer Markdown and a low-configuration setup.
- You’re building a tool, CLI, or small-to-medium Python project.

Use `sphinx` if:

- Your project has a large or complex codebase with many modules and APIs.
- You need fine-grained control over doc generation from source code.
- You’re targeting advanced scientific or academic users.

Choose the engine that best fits your project goals, content type, and team familiarity.
Both options support live preview, search, custom themes, and deployment to static hosting platforms.

## `user_name`

Default: based on the `organization`

The `user_name` field represents your GitHub username and is used to personalize and configure key parts of your project.
It’s often automatically derived from the `organization` field, but you can override it if needed.
This value appears in places like badge URLs, repository links, author metadata, and documentation headers.

It helps connect your identity to the project and ensures that generated links (such as `https://github.com/username/repo_name`) point to the correct profile or organization.
This value is also used when setting up files like `README.md`, `pyproject.toml`, and GitHub-related templates to reflect accurate ownership and attribution.

You should use the exact username associated with your GitHub account or organization, using the correct capitalization if applicable.
For individual projects, this is typically your personal GitHub handle.
For shared or team-maintained projects, it may be the name of the GitHub organization where the repository will be hosted.

## `email`

Default: based on the `organization`

The `email` field is used to designate the contact email address associated with the project.
It appears in files like `CODE_OF_CONDUCT.md`, where it serves as the point of contact for reporting conduct-related concerns, and in `pyproject.toml` to identify the project maintainer.

By default, this value is inferred from the `organization` field, but you can set it explicitly to ensure clarity and accuracy.
It should be a valid, regularly monitored email address that represents either an individual maintainer or a team/institution responsible for the project.

For personal projects, this is typically your own professional or academic email.
For collaborative or organizational projects, it might be a shared support or contact address like `opensource@organization.org` or `teamname.dev@gmail.com`.
This helps ensure that users, contributors, or automated systems have a reliable way to reach the maintainers when needed.

## `line_length`

Default: 88

The `line_length` field sets the maximum number of characters allowed per line of code and is used to configure formatting tools like `black` and `isort`.
This helps maintain consistent and readable code style throughout your project by automatically wrapping or splitting long lines according to the limit you define.

The default value is `88`, which is the standard adopted by the `black` formatter.
It strikes a practical balance between readability and horizontal space, especially when working with side-by-side editors or split screens.
This value is slightly longer than the traditional `79` character limit from PEP 8 but reflects modern development practices and screen resolutions.

You can customize the value to suit your team's preferences or coding environment, but it must fall between `50` and `300` characters.
Choosing a shorter line length (like `80`) can improve readability in narrow terminal windows or printed code reviews.
On the other hand, longer limits (like `100–120`) may reduce line breaks in heavily nested code or data structures.

