# Singleton Pattern

The **Singleton Pattern** is a creational design pattern that ensures a class has **only one instance** and provides a **global point of access** to it. It is used to control access to shared resources, such as configuration objects, logging mechanisms, thread pools, or database connections.

While simple in concept, the Singleton Pattern requires careful handling to avoid becoming a source of hidden dependencies and tightly coupled code.

## Purpose and Benefits

The Singleton Pattern is intended to:

* **Ensure a single instance** of a class across an application.
* **Provide centralized access** to shared data or services.
* **Control resource usage**, especially when instantiating a class is costly or stateful.

It is typically used when exactly one object is needed to coordinate actions across a system.

## When to Use

* When exactly one instance of a class should exist.
* When that instance must be easily accessible throughout the system.
* When managing a shared resource (e.g., configuration, logging, connection pool).

Avoid using Singleton as a convenience shortcut for global state—it should only be used when uniqueness is **logically required**.

## Classic Implementation (Not Thread-Safe)

```python
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
```

**Usage:**

```python
s1 = Singleton()
s2 = Singleton()

print(s1 is s2)  # True
```

Both `s1` and `s2` refer to the same instance.

## Thread-Safe Singleton with Lock

For multithreaded environments, ensure thread safety using `threading.Lock`:

```python
import threading

class ThreadSafeSingleton:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance
```

This is the **double-checked locking** pattern, which ensures that the instance is created only once, even under concurrent access.

## Singleton with Decorators (Pythonic)

You can also implement Singleton using a **decorator**, which wraps the class:

```python
def singleton(cls):
    instances = {}
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance

@singleton
class Config:
    def __init__(self):
        self.settings = {}
```

**Usage:**

```python
config1 = Config()
config2 = Config()

print(config1 is config2)  # True
```

This approach keeps the class clean and reusable while abstracting the Singleton logic.

## Singleton Using Modules

In Python, **modules themselves are singletons** by nature. Variables and functions defined at the top level of a module are only instantiated once and imported as references elsewhere.

**config.py:**

```python
settings = {
    "debug": True,
    "db": "postgres"
}
```

**Usage:**

```python
import config
print(config.settings["debug"])  # True
```

This is often the **simplest and most Pythonic way** to achieve singleton-like behavior.

## Advantages

* **Controlled Access**: Ensures consistent access to shared resources.
* **Memory Efficiency**: Avoids repeated instantiations of expensive objects.
* **Centralization**: Provides a global point of access for certain components.

---

## Drawbacks and Considerations

* **Hidden Dependencies**: Global access can lead to tight coupling and make testing harder.
* **Difficult to Subclass**: Singleton classes are often hard to extend or override.
* **Concurrency Risks**: Improper implementation can lead to race conditions.
* **Testing Challenges**: Singletons can hold state across tests if not properly reset.

If you use the Singleton Pattern, ensure that it does not substitute for proper dependency injection or lead to implicit, tightly coupled modules.
