# SOLID Principles in Python

The **SOLID** principles are a set of five object-oriented design guidelines intended to create software that is more maintainable, scalable, and robust. Introduced by Robert C. Martin (Uncle Bob), these principles help developers write code that is easier to understand, extend, and refactor.

The SOLID acronym stands for:

1. **S** – Single Responsibility Principle
2. **O** – Open/Closed Principle
3. **L** – Liskov Substitution Principle
4. **I** – Interface Segregation Principle
5. **D** – Dependency Inversion Principle

Though originating in statically typed, class-based languages like Java and C#, these principles are highly relevant to Python as well—particularly when writing larger, more structured applications.

## Single Responsibility Principle (SRP)

**Definition:** A class should have only one reason to change.
**In other words:** A class should do one thing and do it well.

**Why it matters:** Classes with multiple responsibilities tend to become large, difficult to test, and hard to modify safely. By narrowing focus, SRP encourages modularity and cohesion.

**Poor Example:**

```python
class Report:
    def __init__(self, data):
        self.data = data

    def calculate_statistics(self):
        # Perform data calculations
        pass

    def save_to_file(self, filename):
        # Write report to file
        pass

    def send_email(self, recipient):
        # Email report
        pass
```

This class is handling three concerns: computation, persistence, and communication.

**Improved with SRP:**

```python
class Report:
    def __init__(self, data):
        self.data = data

    def calculate_statistics(self):
        # Logic here
        pass

class FileSaver:
    def save(self, report, filename):
        # Save to file
        pass

class EmailSender:
    def send(self, report, recipient):
        # Send email
        pass
```

Now, each class has a focused responsibility and can be developed or tested independently.

## Open/Closed Principle (OCP)

**Definition:** Software entities should be **open for extension**, but **closed for modification**.

**In other words:** You should be able to add new functionality without altering existing, tested code.

**Poor Example:**

```python
class PaymentProcessor:
    def process(self, method, amount):
        if method == "credit":
            self._process_credit(amount)
        elif method == "paypal":
            self._process_paypal(amount)
```

Adding a new payment method requires modifying this class—violating OCP.

**Improved with OCP (using polymorphism):**

```python
class PaymentMethod:
    def process(self, amount):
        raise NotImplementedError

class CreditCardPayment(PaymentMethod):
    def process(self, amount):
        # Credit processing logic
        pass

class PaypalPayment(PaymentMethod):
    def process(self, amount):
        # PayPal processing logic
        pass

class PaymentProcessor:
    def process(self, payment_method: PaymentMethod, amount):
        payment_method.process(amount)
```

To add a new payment method, you only need to create a new class—no existing code changes are required.

## Liskov Substitution Principle (LSP)

**Definition:** Subtypes must be substitutable for their base types **without altering the correctness** of the program.

**In other words:** Derived classes should behave in such a way that they can be used in place of their base class without unexpected side effects.

**Poor Example:**

```python
class Bird:
    def fly(self):
        pass

class Ostrich(Bird):
    def fly(self):
        raise Exception("Ostriches can't fly")
```

An `Ostrich` is a `Bird`, but using it in code that assumes all birds can fly will break things.

**Improved with LSP in mind:**

```python
class Bird:
    pass

class FlyingBird(Bird):
    def fly(self):
        pass

class Sparrow(FlyingBird):
    def fly(self):
        # Flies
        pass

class Ostrich(Bird):
    # Doesn't inherit fly behavior
    pass
```

By restructuring the class hierarchy, we maintain substitutability and avoid unexpected behavior.

## Interface Segregation Principle (ISP)

**Definition:** No client should be forced to depend on methods it does not use.

**In other words:** Interfaces (or abstract classes) should be specific rather than general-purpose.

While Python doesn’t enforce interfaces in the same way as languages like Java, the concept still applies to abstract base classes and duck typing.

**Poor Example:**

```python
class Machine:
    def print(self):
        pass

    def scan(self):
        pass

    def fax(self):
        pass

class Printer(Machine):
    def print(self):
        # Ok
        pass

    def scan(self):
        raise NotImplementedError

    def fax(self):
        raise NotImplementedError
```

This class forces `Printer` to implement unused functionality.

**Improved with ISP:**

```python
from abc import ABC, abstractmethod

class Printable(ABC):
    @abstractmethod
    def print(self):
        pass

class Scannable(ABC):
    @abstractmethod
    def scan(self):
        pass

class Printer(Printable):
    def print(self):
        # Print logic
        pass
```

Now classes implement only the behaviors they need.

## Dependency Inversion Principle (DIP)

**Definition:** High-level modules should not depend on low-level modules. Both should depend on abstractions.

**In other words:** Depend on *interfaces*, not *concrete implementations*.

**Poor Example:**

```python
class MySQLDatabase:
    def connect(self):
        pass

class UserService:
    def __init__(self):
        self.db = MySQLDatabase()
```

This tightly couples `UserService` to a specific database implementation.

**Improved with DIP:**

```python
class Database:
    def connect(self):
        raise NotImplementedError

class MySQLDatabase(Database):
    def connect(self):
        # MySQL-specific connection
        pass

class UserService:
    def __init__(self, db: Database):
        self.db = db
```

Now, `UserService` depends on an abstraction and can be easily reused or tested with different database types.

## Applying SOLID in Python

Python is a dynamic language, and some of these principles (especially ISP and DIP) manifest differently than in static languages. However, their spirit still holds. You can follow SOLID by:

* Using abstract base classes (`abc` module)
* Designing with composition over inheritance
* Writing modular, loosely coupled components
* Relying on duck typing and clean, minimal interfaces

