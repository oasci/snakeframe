# Pipeline Pattern

The **Pipeline Pattern** is a behavioral and structural design strategy that models a series of processing steps where **the output of one step becomes the input to the next**. Each step—also called a **stage**, **filter**, or **component**—performs a distinct operation and passes its result downstream.

This pattern promotes composability, reusability, and clarity, especially in systems involving **sequential transformations or processing stages**, such as:

* Data pipelines
* Command processing
* Image or signal processing
* Machine learning workflows
* Middleware stacks in web frameworks

## Purpose and Benefits

The Pipeline Pattern is used to:

* **Decompose complex operations** into simple, composable stages
* **Encapsulate transformations** into independent units
* **Improve code modularity and reusability**
* **Enable reordering, replacement, or extension** of individual processing stages without affecting the whole pipeline
* **Support parallelism or streaming**, if needed, in larger systems

## When to Use

* When data or operations must be passed through multiple, clearly defined stages
* When each stage has a **single, independent responsibility**
* When you want to **compose behavior declaratively** or dynamically
* When building **data transformation workflows**, **event processors**, or **task pipelines**

## Core Structure

```plaintext
[Input] → [Stage 1] → [Stage 2] → ... → [Stage N] → [Output]
```

Each stage performs an operation and forwards the result.

## Basic Implementation in Python

Let’s define a pipeline to transform a string through multiple formatting stages.

### Step 1: Define Pipeline Stages as Callables

```python
def to_lowercase(text):
    return text.lower()

def remove_punctuation(text):
    return ''.join(c for c in text if c.isalnum() or c.isspace())

def strip_whitespace(text):
    return text.strip()
```

### Step 2: Define the Pipeline

```python
class Pipeline:
    def __init__(self):
        self.stages = []

    def add_stage(self, func):
        self.stages.append(func)
        return self  # For chaining

    def run(self, data):
        for stage in self.stages:
            data = stage(data)
        return data
```

### Usage:

```python
pipeline = (
    Pipeline()
    .add_stage(to_lowercase)
    .add_stage(remove_punctuation)
    .add_stage(strip_whitespace)
)

result = pipeline.run("  Hello, World! ")
print(result)  # Output: hello world
```

Each stage is focused, testable, and reusable. The pipeline is flexible and can be extended or reordered with minimal effort.

## Object-Oriented Stages with a Common Interface

For more structured or stateful systems, you can define each stage as a class implementing a common interface:

```python
from abc import ABC, abstractmethod

class Stage(ABC):
    @abstractmethod
    def process(self, data):
        pass

class MultiplyByTwo(Stage):
    def process(self, data):
        return data * 2

class AddFive(Stage):
    def process(self, data):
        return data + 5
```

### Compose Pipeline:

```python
class DataPipeline:
    def __init__(self, stages):
        self.stages = stages

    def run(self, data):
        for stage in self.stages:
            data = stage.process(data)
        return data
```

### Usage:

```python
pipeline = DataPipeline([MultiplyByTwo(), AddFive()])
print(pipeline.run(3))  # Output: 11
```

This model supports stage-specific configuration and encapsulates state or complex logic in each step.

## Real-World Applications

* **Data Processing**: ETL (Extract, Transform, Load) tasks
* **Web Frameworks**: Middleware pipelines (e.g., Flask, FastAPI, ASP.NET)
* **Compilers**: Lexical analysis → parsing → optimization → code generation
* **Machine Learning**: Data cleaning → feature extraction → model training
* **Event Handling**: Normalization → validation → dispatch

## Advantages

* **Modularity**: Each stage is independently developed and tested.
* **Reusability**: Stages can be shared across pipelines.
* **Readability**: Pipelines express operations in a clear linear sequence.
* **Extensibility**: New stages can be added or existing ones swapped with ease.
* **Composability**: Pipelines can be nested, chained, or dynamically constructed.

## Drawbacks

* **Linear rigidity**: Assumes a straight processing flow—more complex control logic may require branching or more advanced coordination.
* **Debugging challenges**: Tracking the data through many transformations can be difficult without good logging.
* **Error propagation**: Failures in one stage can affect the entire pipeline; proper error handling is essential.

To mitigate these issues, consider adding logging, exception handling, and observability to your pipeline infrastructure.
