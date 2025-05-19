# Decorator Pattern

The **Decorator Pattern** is a structural design pattern that allows behavior to be added to an individual object, dynamically, without affecting the behavior of other objects from the same class. It is a powerful alternative to subclassing for extending functionality.

In Python, the Decorator Pattern is particularly natural to use because the language supports **function and class decorators** natively, making the pattern both expressive and concise.

## Purpose and Benefits

The Decorator Pattern is used to:

* **Extend or modify an object’s behavior at runtime**, without modifying its structure.
* **Avoid subclass explosion**, which occurs when creating many subclasses to add combinations of behavior.
* **Promote the Open/Closed Principle**, allowing objects to be extended without modifying existing code.

The core idea is to "wrap" an object inside another object that implements the same interface and adds extra behavior.

## When to Use

* When you want to add responsibilities to individual objects, not entire classes.
* When subclassing would result in too many subclasses for every combination of behaviors.
* When you want to adhere to composition over inheritance.
* When you need to apply enhancements dynamically, such as logging, access control, or caching.

## Core Structure

```plaintext
Component (Interface)
 ├── ConcreteComponent
 └── Decorator (wraps Component)
      └── ConcreteDecorator
```

Each decorator **implements the same interface** as the object it wraps, and delegates to the original while adding its own behavior.

## Example in Python (Classic Object-Oriented Approach)

### Step 1: Define the Component Interface

```python
from abc import ABC, abstractmethod

class Text(ABC):
    @abstractmethod
    def render(self) -> str:
        pass
```

### Step 2: Create a Concrete Component

```python
class PlainText(Text):
    def __init__(self, content):
        self.content = content

    def render(self) -> str:
        return self.content
```

### Step 3: Create Decorators

```python
class TextDecorator(Text):
    def __init__(self, wrapped: Text):
        self._wrapped = wrapped

    def render(self) -> str:
        return self._wrapped.render()

class BoldDecorator(TextDecorator):
    def render(self) -> str:
        return f"<b>{super().render()}</b>"

class ItalicDecorator(TextDecorator):
    def render(self) -> str:
        return f"<i>{super().render()}</i>"
```

### Step 4: Usage

```python
text = PlainText("Hello, world")
decorated = ItalicDecorator(BoldDecorator(text))
print(decorated.render())  # Output: <i><b>Hello, world</b></i>
```

Here, decorators are composed dynamically at runtime, with each layer adding its own behavior.

## Pythonic Function Decorators

In Python, the `@decorator` syntax is syntactic sugar for applying the decorator pattern to **functions or methods**.

**Example: Logging Decorator**

```python
def log_execution(func):
    def wrapper(*args, **kwargs):
        print(f"Executing {func.__name__}...")
        result = func(*args, **kwargs)
        print(f"Finished {func.__name__}")
        return result
    return wrapper

@log_execution
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
 Output:
 Executing greet...
 Hello, Alice!
 Finished greet
```

This technique is ideal for cross-cutting concerns like logging, access control, and timing.

## Real-World Use Cases

* **Access Control**: Wrapping resources with permission checks.
* **Input/Output Formatting**: Adding headers, footers, or styles to output.
* **Caching**: Wrapping functions to store and reuse results.
* **Instrumentation**: Adding logging, profiling, or metrics.
* **Stream Processing**: Decorating file-like objects with buffering, compression, or encryption.

## Advantages

* **Flexible behavior composition**: New behaviors can be mixed and matched at runtime.
* **Avoids subclass explosion**: One class per behavior, not per combination.
* **Open/Closed compliance**: Enhancements don’t require modifying existing code.
* **Reusable and composable**: Decorators can be layered and reused in multiple contexts.

## Drawbacks

* **Multiple layers can be hard to trace**: When many decorators are stacked, debugging becomes more complex.
* **Indirection**: Understanding the full behavior of an object may require unwrapping several layers.
* **Inconsistent with isinstance()**: Wrapped objects are no longer instances of their original class without careful delegation.

To mitigate these concerns, use clear naming, documentation, and consistent interfaces.
