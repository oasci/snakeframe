# Strategy Pattern

The **Strategy Pattern** is a behavioral design pattern that enables selecting an algorithm’s behavior at runtime. It defines a family of algorithms, encapsulates each one, and makes them interchangeable. This promotes flexibility, adheres to the Open/Closed Principle, and reduces conditional logic in client code.

In Python, the Strategy Pattern is particularly elegant to implement due to the language’s support for first-class functions and dynamic typing.

## Purpose and Motivation

Many programs rely on varying behavior based on user input, configuration, or context. Without the Strategy Pattern, this often leads to bulky `if`/`elif`/`else` chains scattered throughout the codebase. This approach is brittle, hard to extend, and violates the Single Responsibility and Open/Closed Principles.

**The Strategy Pattern solves this by:**

* **Encapsulating interchangeable behaviors**
* **Allowing behavior to be injected at runtime**
* **Separating decision-making logic from execution logic**

## When to Use

* You have multiple variations of an algorithm (e.g., different sorting, filtering, payment, or rendering strategies).
* You want to switch behavior dynamically at runtime.
* You want to isolate algorithm-specific logic for testing or extension.

## Conceptual Structure

```plaintext
Context
 └── uses ──> Strategy Interface
               ├── ConcreteStrategyA
               └── ConcreteStrategyB
```

* **Strategy Interface**: Defines a common interface for all supported strategies.
* **Concrete Strategies**: Implement the interface with different behavior.
* **Context**: Maintains a reference to a strategy and delegates the algorithm execution to it.

## Example in Python: A Text Formatter

### Step 1: Define the Strategy Interface

```python
from abc import ABC, abstractmethod

class TextFormatter(ABC):
    @abstractmethod
    def format(self, text: str) -> str:
        pass
```

### Step 2: Implement Concrete Strategies

```python
class UpperCaseFormatter(TextFormatter):
    def format(self, text: str) -> str:
        return text.upper()

class LowerCaseFormatter(TextFormatter):
    def format(self, text: str) -> str:
        return text.lower()

class CapitalizeFormatter(TextFormatter):
    def format(self, text: str) -> str:
        return text.capitalize()
```

### Step 3: Define the Context

```python
class TextEditor:
    def __init__(self, formatter: TextFormatter):
        self.formatter = formatter

    def publish(self, text: str) -> str:
        return self.formatter.format(text)

    def set_formatter(self, formatter: TextFormatter):
        self.formatter = formatter
```

### Step 4: Using the Pattern

```python
editor = TextEditor(UpperCaseFormatter())
print(editor.publish("hello strategy"))  # Output: HELLO STRATEGY

editor.set_formatter(CapitalizeFormatter())
print(editor.publish("hello strategy"))  # Output: Hello strategy
```

## Pythonic Strategy: Using Functions as Strategies

Since Python supports first-class functions, strategies can also be passed as simple callables:

```python
def upper(text):
    return text.upper()

def lower(text):
    return text.lower()

def capitalize(text):
    return text.capitalize()

def publish(text, formatter):
    return formatter(text)

print(publish("hello", upper))       # HELLO
print(publish("hello", capitalize))  # Hello
```

This is functionally equivalent to the OO implementation, and often preferable when a full class hierarchy is unnecessary.

## Advantages

* **Flexibility**: New strategies can be introduced without changing client code.
* **Separation of Concerns**: Algorithms are cleanly separated from the objects that use them.
* **Testability**: Strategies can be tested in isolation.
* **Runtime Behavior Change**: Swap strategies during execution without modifying objects.

---

## Drawbacks

* **Proliferation of Classes**: In object-oriented implementations, many small strategy classes can clutter the codebase.
* **Indirection**: Behavior is no longer visible directly in the context class, which may increase learning overhead for newcomers.
* **Overkill for Simple Logic**: Using the pattern for extremely simple or rarely-changing behavior may introduce unnecessary abstraction.
