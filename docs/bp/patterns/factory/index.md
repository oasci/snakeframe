# Factory Pattern

The **Factory Pattern** is a creational design pattern that provides an interface for creating objects **without specifying their exact class**. It encapsulates the instantiation logic and delegates the responsibility of object creation to a factory, thereby promoting flexibility and adherence to the Open/Closed Principle.

In Python, where class construction is relatively straightforward, the Factory Pattern is still highly useful—particularly when the instantiation logic becomes complex or dependent on runtime parameters.

## Purpose and Benefits

The Factory Pattern is used to:

* **Encapsulate object creation logic**, hiding complexity from the client.
* **Promote loose coupling**, allowing the code to rely on interfaces or abstract classes rather than concrete implementations.
* **Support polymorphism**, enabling the system to work with different object types through a unified interface.
* **Improve scalability**, by making it easy to add new types without modifying existing code.

## When to Use

Consider the Factory Pattern when:

* You need to create objects based on dynamic input (e.g., configuration, user input, environment).
* Object creation involves conditional logic or preparation steps.
* You want to isolate the process of deciding *which* class to instantiate.

## Basic Implementation in Python

Let’s assume we have several types of **shapes**, each with a common interface:

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        print("Drawing a circle")

class Square(Shape):
    def draw(self):
        print("Drawing a square")
```

A naive approach might instantiate shapes like this:

```python
shape = Circle()  # Tight coupling
```

With the **Factory Pattern**, we delegate this responsibility to a factory class or function.

## Factory Function (Simple Form)

```python
def shape_factory(shape_type):
    if shape_type == "circle":
        return Circle()
    elif shape_type == "square":
        return Square()
    else:
        raise ValueError(f"Unknown shape type: {shape_type}")
```

**Usage:**

```python
shape = shape_factory("circle")
shape.draw()  # Output: Drawing a circle
```

This allows clients to request shapes by type without knowing the class names or how they’re constructed.

## Factory Class (Encapsulated Form)

For more complex scenarios (e.g., registering new types, managing shared instances), you may prefer a factory class:

```python
class ShapeFactory:
    def create_shape(self, shape_type):
        if shape_type == "circle":
            return Circle()
        elif shape_type == "square":
            return Square()
        else:
            raise ValueError(f"Unknown shape type: {shape_type}")
```

## Using a Registry for Extensibility

A more advanced approach uses a **registration-based factory**, enabling dynamic extension:

```python
class ShapeFactory:
    def __init__(self):
        self._creators = {}

    def register_shape(self, shape_type, creator):
        self._creators[shape_type] = creator

    def create_shape(self, shape_type):
        creator = self._creators.get(shape_type)
        if not creator:
            raise ValueError(f"Unknown shape type: {shape_type}")
        return creator()

# Setup
factory = ShapeFactory()
factory.register_shape("circle", Circle)
factory.register_shape("square", Square)

# Usage
shape = factory.create_shape("square")
shape.draw()  # Output: Drawing a square
```

This pattern is powerful in plugin systems or applications with user-defined types.

## Advantages of the Factory Pattern

* **Encapsulation of object creation**: Construction logic is centralized.
* **Simplified client code**: Clients need not understand class hierarchies.
* **Enhanced maintainability**: New types can be added with minimal impact.
* **Compliance with SOLID principles**: Especially Open/Closed and Dependency Inversion.

## Limitations and Considerations

* **Indirection**: Adds an additional layer, which may be unnecessary for simple cases.
* **Potential overuse**: In Python, simple instantiations often don’t require a factory.
* **Less transparency**: Debugging and understanding object flow can be more difficult if factories are deeply nested.

Use factories thoughtfully—when they add clarity or flexibility—not just as a default habit.
