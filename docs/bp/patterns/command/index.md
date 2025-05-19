# Command Pattern

The **Command Pattern** is a behavioral design pattern that turns a request or operation into a standalone object. This object encapsulates all the information needed to perform the action, including the method to call, the arguments to pass, and the target object itself.

By encapsulating actions as objects, the Command Pattern allows you to:

* Parameterize objects with operations
* Queue or log requests
* Support undo/redo functionality
* Decouple senders of requests from their receivers

This pattern is commonly used in GUI toolkits, job queues, transactional systems, and remote procedure calls.

## Purpose and Benefits

The Command Pattern is used to:

* **Encapsulate behavior** as an object
* **Defer execution** or queue operations
* **Support undoable operations**
* **Promote extensibility** through object composition
* **Decouple invokers** from the code that performs the action

It promotes adherence to the **Open/Closed Principle** and enables cleaner, more modular architectures.

## When to Use

* When you need to issue requests to objects without knowing the implementation details.
* When you want to support operations like **undo**, **redo**, **logging**, or **macro recording**.
* When operations must be executed at different times or in different contexts (e.g., job scheduling).
* When requests need to be **reversible** or **auditable**.

## Core Components

* **Command Interface**: Declares a method for executing an operation.
* **Concrete Command**: Implements the `execute()` method by invoking actions on a receiver.
* **Receiver**: Knows how to perform the operation.
* **Invoker**: Triggers command execution without knowing how the command works.
* **Client**: Configures the command with the receiver and passes it to the invoker.

## Example in Python: A Remote Control

### Step 1: Define the Command Interface

```python
from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass
```

### Step 2: Create Receivers

```python
class Light:
    def turn_on(self):
        print("Light is ON")

    def turn_off(self):
        print("Light is OFF")
```

### Step 3: Create Concrete Commands

```python
class LightOnCommand(Command):
    def __init__(self, light: Light):
        self.light = light

    def execute(self):
        self.light.turn_on()

class LightOffCommand(Command):
    def __init__(self, light: Light):
        self.light = light

    def execute(self):
        self.light.turn_off()
```

### Step 4: Create the Invoker

```python
class RemoteControl:
    def __init__(self):
        self._commands = []

    def submit(self, command: Command):
        self._commands.append(command)
        command.execute()
```

### Step 5: Usage

```python
light = Light()
remote = RemoteControl()

remote.submit(LightOnCommand(light))
remote.submit(LightOffCommand(light))
```

**Output:**

```
Light is ON
Light is OFF
```

## Pythonic Variation Using Callables

Because Python supports functions as first-class objects, you can simplify the Command Pattern using callables:

```python
class Remote:
    def __init__(self):
        self._queue = []

    def submit(self, command):
        self._queue.append(command)
        command()
```

**Usage:**

```python
def turn_on():
    print("Device ON")

def turn_off():
    print("Device OFF")

remote = Remote()
remote.submit(turn_on)
remote.submit(turn_off)
```

This is suitable for simple cases where encapsulating into full command classes would be overkill.

## Use Cases in Real Applications

* **GUI Frameworks**: Button clicks mapped to command objects.
* **Undo/Redo Systems**: Commands are stored and replayed or reversed.
* **Job Queues**: Commands represent tasks to be executed asynchronously.
* **Macro Recording**: Commands are logged and replayed to automate sequences.
* **Transactional Systems**: Encapsulate operations that can be committed or rolled back.

## Advantages

* **Decoupling**: Sender and receiver are separated.
* **Extensibility**: New commands can be added without changing existing code.
* **Reusability**: Commands can be reused across invokers.
* **Support for complex behaviors**: Such as queuing, logging, undoing, batching.

## Drawbacks

* **Verbosity**: In OO implementations, many small command classes may clutter the codebase.
* **Overhead**: For trivial operations, the structure may add unnecessary complexity.
* **State Management**: Undo/redo can require careful state tracking, depending on complexity.
