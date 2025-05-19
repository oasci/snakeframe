# Design Patterns

Design patterns are repeatable solutions to common software design problems. They offer proven ways to structure code so it’s easier to understand, extend, test, and maintain.

Design patterns are not code snippets or rules—they are high-level conceptual templates. They become especially valuable as projects grow beyond a few scripts and into collaborative, multi-module systems.

Python’s flexibility means that some classic object-oriented patterns are used less often than in Java or C++. However, many are still relevant, especially when building modular systems, plugins, or data pipelines.

## Factory Pattern

The Factory pattern provides a way to create objects without exposing the instantiation logic. This is useful when you want to return different types of objects based on runtime input.

### Use Cases

* Selecting different simulation engines or models
* Creating interface objects for different data sources
* Avoiding direct class references in higher-level logic

### Example

```python
class CSVLoader:
    def load(self, path): ...

class JSONLoader:
    def load(self, path): ...

def get_loader(file_type):
    if file_type == "csv":
        return CSVLoader()
    elif file_type == "json":
        return JSONLoader()
    else:
        raise ValueError("Unsupported file type")
```

The consumer of this function doesn’t need to know which class is instantiated—they just use `loader.load(path)`.

## Strategy Pattern

The Strategy pattern defines a family of algorithms or behaviors and makes them interchangeable at runtime. This is useful when you want to vary a process (e.g., scoring, filtering, transforming) without modifying the core logic.

### Use Cases

* Choosing between different analysis methods
* Supporting different optimization strategies
* Allowing user-defined behavior in a plugin architecture

### Example

```python
class MeanStrategy:
    def compute(self, values):
        return sum(values) / len(values)

class MedianStrategy:
    def compute(self, values):
        return sorted(values)[len(values) // 2]

def run_analysis(values, strategy):
    return strategy.compute(values)
```

## Adapter Pattern

The Adapter pattern allows incompatible interfaces to work together by wrapping an existing class with a new interface.

### Use Cases

* Integrating third-party libraries with different APIs
* Wrapping legacy code to work with a new system
* Translating between internal and external data formats

### Example

```python
class LegacyLoader:
    def read_file(self, path):
        ...

class LoaderAdapter:
    def __init__(self, legacy_loader):
        self.legacy_loader = legacy_loader

    def load(self, path):
        return self.legacy_loader.read_file(path)
```

Now you can use `LoaderAdapter` in contexts expecting a `load()` method.

## Observer Pattern

The Observer pattern allows multiple components to be notified automatically when another object changes. This is useful for decoupling components.

### Use Cases

* Logging changes to simulation state
* Triggering side effects (e.g., visualization, data export)
* Monitoring configuration or user input changes

### Example

```python
class Subject:
    def __init__(self):
        self._observers = []

    def subscribe(self, callback):
        self._observers.append(callback)

    def notify(self, data):
        for callback in self._observers:
            callback(data)
```

This allows you to register multiple listeners without tightly coupling them.

## Singleton Pattern

The Singleton pattern ensures a class has only one instance and provides a global point of access to it. This is often overused, but it can be helpful for shared configuration or logging.

### Use Cases

* Managing a single configuration object
* Centralized logging or telemetry services
* Shared resource pools

### Pythonic Singleton Example

```python
class Config:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Config, cls).__new__(cls)
        return cls._instance
```

Alternatively, use a module-level global instead, which is more idiomatic in Python.

## Command Pattern

The Command pattern encapsulates a request or action as an object, allowing you to log, queue, or undo operations.

### Use Cases

* Implementing command-line commands
* Building task queues or pipelines
* Supporting undo/redo in UIs or simulations

### Example

```python
class SaveCommand:
    def execute(self):
        print("Saving data...")

class DeleteCommand:
    def execute(self):
        print("Deleting data...")

def run_command(cmd):
    cmd.execute()
```

You can store and manage command objects consistently without knowing what they do internally.

## Decorator Pattern

The Decorator pattern adds behavior to an object or function without modifying its source code. In Python, this pattern is implemented natively with `@decorators`.

### Use Cases

* Caching, logging, or timing function calls
* Adding retry logic or instrumentation
* Validating inputs or enforcing permissions

### Example

```python
def log_call(func):
    def wrapper(*args, kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, kwargs)
    return wrapper

@log_call
def run():
    print("Running task")
```

This pattern helps you keep cross-cutting concerns out of core logic.

## Pipeline Pattern

Though not a classical GoF pattern, the Pipeline pattern is widely used in data science and research code. It chains multiple operations into a defined sequence.

### Use Cases

* Processing raw data into cleaned, structured output
* Running sequential analysis or transformation steps
* Building reproducible workflows

### Example

```python
def load(path):
    ...

def normalize(data):
    ...

def analyze(data):
    ...

def pipeline(path):
    return analyze(normalize(load(path)))
```

Each function is pure and composable. Pipelines encourage clean separation of steps and are easy to test individually.
