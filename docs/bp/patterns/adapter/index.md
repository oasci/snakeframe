# Adapter Pattern

The **Adapter Pattern** is a structural design pattern that allows objects with incompatible interfaces to work together. It acts as a translator between two interfaces, enabling the integration of existing classes into new systems without modifying their source code.

In Python, where duck typing and dynamic typing make interface enforcement looser, the Adapter Pattern is still useful when integrating external libraries, legacy systems, or mismatched components.

## Purpose and Benefits

The Adapter Pattern is used to:

* **Bridge incompatible interfaces**, allowing code reuse without modifying the original class.
* **Integrate legacy or third-party code** into a modern system.
* **Encapsulate transformation logic**, keeping the rest of the codebase clean and focused.
* **Promote single responsibility**, by isolating the adaptation concern from business logic.

## When to Use

Use the Adapter Pattern when:

* You want to use an existing class, but its interface doesn’t match the one your code expects.
* You are integrating third-party libraries into your application.
* You are refactoring or modernizing parts of a codebase while keeping backward compatibility.

## Real-World Analogy

Think of a power adapter. A European plug cannot fit into a U.S. socket, but a travel adapter allows it to connect and work without changing the plug or the socket.

The software equivalent achieves the same goal with class interfaces.

## Classic Object-Oriented Example in Python

### Problem: Incompatible Interfaces

```python
class OldPrinter:
    def print_text(self, message):
        print(f"Old Printer: {message}")
```

Let’s say our system expects objects with a `display()` method:

```python
class NewDisplaySystem:
    def __init__(self, device):
        self.device = device

    def show(self, message):
        self.device.display(message)
```

`OldPrinter` doesn’t have a `display()` method, so it can't be used directly.

### Solution: Adapter Class

```python
class PrinterAdapter:
    def __init__(self, old_printer):
        self.old_printer = old_printer

    def display(self, message):
        # Translate 'display' to 'print_text'
        self.old_printer.print_text(message)
```

### Usage:

```python
old_printer = OldPrinter()
adapter = PrinterAdapter(old_printer)

display_system = NewDisplaySystem(adapter)
display_system.show("Hello via adapter")  # Output: Old Printer: Hello via adapter
```

Now the system can work with the old printer, without modifying either the display system or the printer class.

## Pythonic Version Using Duck Typing

Python’s dynamic nature allows you to adapt interfaces more flexibly, even without formal inheritance.

```python
class PrinterAdapter:
    def __init__(self, adaptee):
        self._adaptee = adaptee

    def display(self, message):
        return self._adaptee.print_text(message)
```

This approach is functionally the same but emphasizes Python's convention-over-configuration philosophy.

## Using Adapter with Third-Party Code

Suppose you’re using a third-party library with a class like this:

```python
class ExternalLogger:
    def write_log(self, text):
        print(f"[LOG]: {text}")
```

But your app expects a logger with a `log(message)` method.

**Adapter:**

```python
class LoggerAdapter:
    def __init__(self, external_logger):
        self.external_logger = external_logger

    def log(self, message):
        self.external_logger.write_log(message)
```

**Usage:**

```python
logger = LoggerAdapter(ExternalLogger())
logger.log("System initialized")  # Output: [LOG]: System initialized
```

This allows seamless integration without altering the third-party library or your existing application logic.

## Object Adapter vs. Class Adapter

* **Object Adapter** (shown above): Uses composition. The adapter holds a reference to the adaptee. This is the typical and preferred approach in Python.
* **Class Adapter** (less common in Python): Uses inheritance to adapt the interface. Python supports multiple inheritance, so it’s possible, but composition is usually safer and more flexible.

## Advantages

* **Reusability**: Leverage existing or third-party code without modification.
* **Flexibility**: Adapt different interfaces without changing clients.
* **Single Responsibility**: Keeps adaptation logic separate from business logic.
* **Backward Compatibility**: Integrate legacy systems with modern interfaces.

## Drawbacks

* **Extra Abstraction**: Adds another layer between components, which can complicate debugging.
* **Limited by Interfaces**: In some cases, adapting deeply mismatched behaviors may lead to bloated adapters.
* **Misuse Risk**: Overusing adapters may signal architectural mismatches that need addressing.
