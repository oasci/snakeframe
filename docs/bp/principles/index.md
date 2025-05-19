# Coding Principles

Coding principles are short, memorable guidelines that help you write software that is **clean**, **reliable**, and **maintainable**—even as your codebase grows in complexity.

This section introduces several core principles that every Python developer should know: **DRY**, **KISS**, **YAGNI**, and an overview of the **SOLID** principles adapted to Python.

These aren’t hard rules—but they are powerful heuristics. Practiced consistently, they help you and your collaborators avoid bugs, reduce duplication, and make better design decisions.

## DRY – Don’t Repeat Yourself

> “Every piece of knowledge must have a single, unambiguous, authoritative representation within a system.” — *The Pragmatic Programmer*

### What It Means

Whenever you find yourself copying and pasting code—or writing similar code in multiple places—pause and ask: *Should this logic live in one reusable place instead?*

The DRY principle encourages **abstraction and reuse**. It improves maintainability and reduces bugs because you only need to update logic in *one* place when something changes.

### Common Repetitions

#### ❌ Repeating logic

```python
# Bad: repeated logic for distance
d1 = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
d2 = ((a - b)**2 + (c - d)**2)**0.5
```

#### ✅ DRY alternative

```python
def euclidean_distance(x1, x2, y1, y2):
    return ((x1 - x2)**2 + (y1 - y2)**2)**0.5

d1 = euclidean_distance(x1, x2, y1, y2)
d2 = euclidean_distance(a, b, c, d)
```

#### ❌ Repeating constants or config

```python
learning_rate = 0.01
# later
alpha = 0.01
```

#### ✅ DRY alternative

```python
DEFAULT_LEARNING_RATE = 0.01
```

Use constants, functions, and well-named variables to represent shared concepts. If you find similar functions in multiple modules, consider unifying them in a common helper or utility module.

> 💡 **DRY ≠ no repetition at all.** Sometimes duplication is better than premature abstraction—especially if the abstraction would be unclear or fragile.

## KISS – Keep It Simple, Stupid

> “Simplicity is the soul of efficiency.” — *Austin Freeman*

### What It Means

KISS is a reminder to avoid overengineering. The simplest solution that works is often the best solution.

You don’t need a class hierarchy, metaclasses, or decorators for every problem. Write the **clearest**, not the cleverest, version of your code—especially early in a project’s life.

### Examples

#### ❌ Too complex

```python
class Counter:
    def __init__(self):
        self._count = 0
    def increment(self):
        self._count += 1
    def get(self):
        return self._count
```

#### ✅ Simpler version

```python
count = 0
count += 1
```

Unless you're building a reusable counter object, just use a variable. Start simple. You can always refactor later.

### Tips for Simplicity

* Prefer functions over classes until you need state
* Avoid unnecessary generalization or configuration
* Don’t add complexity for “what-ifs” that don’t exist yet

> 🧠 If you don’t understand your own code a week after writing it, it probably violates KISS.

## YAGNI – You Aren’t Gonna Need It

> “Always implement things when you actually need them, never when you just foresee that you need them.” — *Ron Jeffries*

### What It Means

YAGNI is about **deferring unnecessary features** or code. It’s easy to fall into the trap of writing code to “future-proof” a system by adding hooks, options, or abstraction layers before they’re needed. Most of that code will go unused—and worse, it will add complexity.

### Common Violations

* Adding configuration options for features no one has requested
* Designing an inheritance tree for a single object type
* Writing a plugin system when you only have one plugin

#### ❌ YAGNI violation

```python
def save_file(data, backend="json", path="file.json"):
    if backend == "json":
        save_as_json(data, path)
    elif backend == "xml":
        save_as_xml(data, path)
    elif backend == "yaml":
        save_as_yaml(data, path)
```

#### ✅ Simplified version (YAGNI-compliant)

```python
def save_file(data, path="file.json"):
    save_as_json(data, path)
```

If you don’t need YAML today, don’t add support until it becomes necessary.

> 🔍 YAGNI doesn't mean *never* planning—it means not building until you're sure the need is real.

## SOLID Principles (in Python)

**SOLID** is a set of object-oriented design principles. While originally rooted in statically typed languages like Java or C#, they can be applied thoughtfully in Python—especially in large, modular codebases.

Let’s adapt each for the Python ecosystem:

### S – Single Responsibility Principle

> A class (or function) should have one job.

In Python, this often applies to **functions more than classes**. Each function should do one thing, and do it well.

#### ✅ Example

```python
def load_config(path):
    # Only loads config—doesn't validate or save
```

Avoid functions or classes that combine multiple responsibilities like loading, processing, and writing data.

### O – Open/Closed Principle

> Software entities should be open for extension, but closed for modification.

In Python, you can honor this with **plug-in patterns**, strategy classes, or dispatch systems.

#### ✅ Example

Instead of editing logic:

```python
if mode == "fast":
    ...
elif mode == "accurate":
    ...
```

Use:

```python
strategies = {
    "fast": FastStrategy(),
    "accurate": AccurateStrategy(),
}
strategies[mode].run()
```

This way, adding new behavior doesn’t require modifying core logic.

### L – Liskov Substitution Principle

> Subtypes should be substitutable for their base types.

In Python, this means that if you subclass something or define an abstract base class (ABC), the subclass should behave consistently.

If your subclass breaks assumptions of the parent, it violates LSP—even if the code runs.

### I – Interface Segregation Principle

> Clients should not be forced to depend on interfaces they don’t use.

In Python, this encourages **small, focused classes** or protocols instead of large do-everything objects. If you have a class with many unrelated methods, it might be time to split it up.

### D – Dependency Inversion Principle

> High-level modules should not depend on low-level modules; both should depend on abstractions.

In Python, this often means **injecting dependencies** via arguments instead of importing and hardcoding them.

#### ✅ Example

```python
def run_simulation(model, data_loader):
    data = data_loader.load()
    return model.run(data)
```

This makes your code testable, flexible, and composable.
