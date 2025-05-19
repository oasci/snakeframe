# Observer Pattern

The **Observer Pattern** is a behavioral design pattern that defines a one-to-many dependency between objects. When the *subject* (also called *publisher*) changes state, all its *observers* (or *subscribers*) are notified and updated automatically.

This pattern is commonly used in event-driven systems, GUI frameworks, messaging systems, and anywhere you want to decouple an event source from its consumers.

## Purpose and Benefits

The Observer Pattern enables:

* **Loose coupling** between a subject and its dependents.
* **Dynamic relationships**, where observers can be added or removed at runtime.
* **Reactivity**, allowing changes in one object to automatically propagate to others.

It promotes the **Separation of Concerns**, allowing the subject to focus on state management while observers handle their own update logic.

## When to Use

* When changes in one object must be automatically reflected in others.
* When you need a *plugin-like* mechanism for responding to events.
* When building **event-driven architectures**, **notification systems**, or **GUI components**.

## Terminology

* **Subject (Publisher):** The object whose state is being observed.
* **Observers (Subscribers):** Objects that want to be notified when the subject changes.
* **Event/Notification:** The signal that triggers an update to the observers.

## Classic Implementation in Python

### Step 1: Define the Observer Interface

```python
from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, message):
        pass
```

### Step 2: Define the Subject

```python
class Subject:
    def __init__(self):
        self._observers = set()

    def attach(self, observer: Observer):
        self._observers.add(observer)

    def detach(self, observer: Observer):
        self._observers.discard(observer)

    def notify(self, message):
        for observer in self._observers:
            observer.update(message)
```

### Step 3: Implement Concrete Observers

```python
class EmailAlert(Observer):
    def update(self, message):
        print(f"Email alert: {message}")

class LoggingService(Observer):
    def update(self, message):
        print(f"Log entry: {message}")
```

### Step 4: Using the Pattern

```python
subject = Subject()

email = EmailAlert()
logger = LoggingService()

subject.attach(email)
subject.attach(logger)

subject.notify("New user registered")
 Output:
 Email alert: New user registered
 Log entry: New user registered
```

Observers can be attached or removed dynamically, and the subject doesn't need to know their internal logic.

## Pythonic Observer Using Callables

Because Python treats functions as first-class citizens, a lightweight variation of the Observer Pattern can use functions (or lambdas) instead of full-blown observer classes:

```python
class EventPublisher:
    def __init__(self):
        self._subscribers = []

    def subscribe(self, callback):
        self._subscribers.append(callback)

    def unsubscribe(self, callback):
        self._subscribers.remove(callback)

    def notify(self, data):
        for subscriber in self._subscribers:
            subscriber(data)

 Usage
def send_email_alert(data):
    print(f"Email: {data}")

def log_to_file(data):
    print(f"Log: {data}")

publisher = EventPublisher()
publisher.subscribe(send_email_alert)
publisher.subscribe(log_to_file)

publisher.notify("Data updated")
 Output:
 Email: Data updated
 Log: Data updated
```

This approach is concise and useful when observers don’t need to maintain state.

## Observer in Real Applications

The Observer Pattern is widely used in:

* **Graphical User Interfaces**: Widgets subscribe to model changes.
* **Event-Driven Architectures**: Services respond to events from brokers like Kafka or RabbitMQ.
* **Data Binding**: UI components stay in sync with backend data models.
* **Notification Systems**: Multiple services respond to a single change (e.g., sending emails, updating logs, refreshing dashboards).

## Advantages

* **Decoupling**: Subjects and observers are independent.
* **Scalability**: Add new observers without modifying the subject.
* **Dynamic Subscription**: Observers can register and deregister at runtime.

## Drawbacks

* **Unexpected Order of Updates**: Observer execution order is not always predictable.
* **Memory Leaks**: If observers aren't unsubscribed properly, references may persist.
* **Complex Debugging**: Tracing notification chains can become difficult in large systems.

To mitigate these issues, use clear naming, logging, and observer lifecycle management.
