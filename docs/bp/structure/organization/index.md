# Organizing by Function vs. Layer

Once your project grows beyond a few modules, you’ll need to make thoughtful decisions about how to organize your internal structure. This isn’t just about where files go—it’s about how you and others navigate, extend, and maintain the project over time.

There are two common strategies for organizing subpackages in Python projects:

1. Layered Structure: Organizing by technical role (e.g., “core logic”, “API interface”, “utilities”)
2. Feature-Based Structure: Organizing by domain features (e.g., “molecules”, “simulations”)

Both approaches are valid. Each offers different strengths depending on the size, purpose, and complexity of your project.

## Layered Structure

In a layered structure, your code is grouped by its technical responsibility—regardless of the specific domain it serves.

```
mypackage/
  api/
    cli.py
    web.py
  core/
    model.py
    simulation.py
  utils/
    io.py
    math.py
```

### Folder Roles

- `api/`: Entry points and interfaces—e.g., CLI commands, REST endpoints, or notebooks.
- `core/`: The essential logic that defines what your software *does*. This is your business or scientific logic.
- `utils/`: Supporting functionality that is general-purpose and not tied to the domain (e.g., string manipulation, file loading, error formatting).

### Benefits

- Separation of concerns: Each folder serves a clearly defined purpose.
- Familiarity: This structure is common in web frameworks and enterprise applications.
- Pluggability: It’s easy to swap out infrastructure—like replacing a CLI with a web UI—without touching your core logic.

### When to Use It

- Your project has multiple “delivery mechanisms” (e.g., a CLI *and* an API).
- You want to isolate interfaces from internal logic.
- You expect to evolve your user interface or input/output mechanisms over time.

> 🧠 Mental model: You’re building a layered cake—each layer has a clear role and responsibility.

## Feature-Based Structure

In a feature-based structure, code is grouped by domain or functional area. Each folder encapsulates everything related to a specific feature, including logic, configuration, and utilities.

```
mypackage/
  molecules/
    align.py
    visualize.py
    io.py
  simulation/
    run.py
    config.py
    slurm.py
```

### Folder Roles

- `molecules/` might contain everything related to molecular manipulation.
- `simulation/` might handle simulation configuration, orchestration, and results.

Each subpackage becomes a sort of mini-application, responsible for its own domain. Logic, helpers, and configs live side-by-side—often closer to how subject-matter experts think about the problem.

### Benefits

- Cohesion: All code related to a feature lives together.
- Discoverability: Easier for new contributors or domain experts to find what they need.
- Maintainability: You can evolve one feature without accidentally affecting others.

### When to Use It

- Your project is research- or domain-driven.
- You’re working with a team of specialists who each own part of the problem space.
- The user mental model aligns with distinct functional areas.

> 🧠 Mental model: You’re building modules like LEGO bricks—each one complete and self-contained.

## Which Should You Use?

There’s no universal rule, but here are some guiding questions:

| Question                                              | Prefer Layered | Prefer Feature-Based |
| ----------------------------------------------------- | -------------- | -------------------- |
| Are your features tightly interconnected?             | ✅              | 🚫                   |
| Are your interfaces likely to change?                 | ✅              | 🚫                   |
| Do domain experts need to navigate the code?          | 🚫             | ✅                    |
| Are you building a platform with multiple subsystems? | ✅              | ✅ (with nesting)     |

## Hybrid Approaches

Many mature projects adopt a hybrid structure—feature-based at the top, but layered within each feature.

Example:

```
mypackage/
  simulation/
    api/
      cli.py
    core/
      run.py
      config.py
    utils/
      file_io.py
```

This combines the clarity of feature boundaries with the benefits of layering inside each submodule.
