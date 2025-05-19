# The DRY Principle (Don't Repeat Yourself)

The DRY principle—short for *Don't Repeat Yourself*—is a foundational tenet in software development. Coined by Andy Hunt and Dave Thomas in *The Pragmatic Programmer*, DRY is best understood as a call to reduce duplication in code. At its core, the DRY principle encourages developers to express every piece of knowledge or logic within a system *once and only once*.

## Why DRY Matters

Duplication is a common source of software decay. When the same logic or data appears in multiple places, it becomes harder to maintain. A change to one instance often requires changes to others; if one is missed, it can introduce bugs, inconsistencies, and costly regressions.
Following DRY improves:

- **Maintainability:** Changes are easier and safer when logic is centralized.
- **Readability:** Code becomes more concise and understandable.
- **Reusability:** Well-factored code components can be reused across projects or systems.
- **Testability:** Modular, DRY code is easier to test in isolation.

## Recognizing Duplication

Duplication in software isn't limited to identical lines of code. It includes:

- **Logic Duplication:** Repeating the same calculations or conditional structures.
- **Structural Duplication:** Replicating function bodies, class definitions, or data structures.
- **Semantic Duplication:** Expressing the same idea or concept multiple ways in different parts of the codebase.
- **Configuration Duplication:** Hard-coding values or repeating settings across modules.

It is important to understand that not all repetition is harmful. Sometimes, attempting to eliminate minor or coincidental duplication can lead to over-generalization and reduced clarity. The key is to identify meaningful duplication—cases where the same logic or concept is repeated with only superficial differences.

## Applying DRY in Python

Python offers several tools and constructs to help enforce the DRY principle. Here are some illustrative examples.

### Using Functions to Eliminate Logic Duplication

**Before DRY:**

```python
def calculate_discounted_price(price):
    if price > 100:
        price -= price * 0.1
    return price

def calculate_discounted_shipping(shipping_cost):
    if shipping_cost > 100:
        shipping_cost -= shipping_cost * 0.1
    return shipping_cost
```

**After Applying DRY:**

```python
def apply_discount(amount, threshold=100, discount_rate=0.1):
    if amount > threshold:
        amount -= amount * discount_rate
    return amount
```

Now the logic is centralized and changes (e.g., altering the discount rate) only need to happen in one place.

### Eliminating Data Structure Duplication

**Before DRY:**

```python
user = {
    "first_name": "Alice",
    "last_name": "Smith",
    "email": "alice@example.com"
}

admin = {
    "first_name": "Alice",
    "last_name": "Smith",
    "email": "alice@example.com",
    "permissions": ["read", "write", "delete"]
}
```

**After Applying DRY with Inheritance:**

```python
class User:
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

class Admin(User):
    def __init__(self, first_name, last_name, email, permissions):
        super().__init__(first_name, last_name, email)
        self.permissions = permissions
```

This use of object-oriented principles avoids repetition and enables logical grouping of behavior.

### Consolidating Repeated Logic with Decorators

```python
def log_start_and_end(func):
    def wrapper(*args, **kwargs):
        print(f"Starting {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Ending {func.__name__}")
        return result
    return wrapper

@log_start_and_end
def process_data():
    # process logic
    pass

@log_start_and_end
def generate_report():
    # report logic
    pass
```

Here, the decorator encapsulates common logic (logging), keeping the core functionality of the functions clean and focused.

## When to Be Cautious

While DRY is a powerful guide, it must be applied judiciously. Overzealous adherence can lead to:

- **Over-abstraction:** Generalizing prematurely before sufficient use cases exist.
- **Tight Coupling:** Sharing logic between components that should evolve independently.
- **Reduced Readability:** Abstracted code may obscure the intent if not well-named or documented.

A good heuristic is the *Rule of Three*: duplication is acceptable the first time and possibly even the second. Only when the pattern appears a third time should you consider extracting it.
