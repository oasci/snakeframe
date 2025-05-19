# Testing

High-quality software is underpinned by robust, reliable, and repeatable testing. In the Python ecosystem, testing is commonly performed using the `pytest` framework due to its simplicity, expressive syntax, and powerful plugin architecture. This section will guide you through the foundational practices of writing and organizing tests, using `pytest` features such as fixtures and markers, measuring and enforcing test coverage, and testing asynchronous or integrated components.

## Writing Tests with `pytest`: Structure, Naming, and `parametrize`

**Test Structure and Naming Conventions**

Tests should be easy to discover, read, and maintain. The `pytest` discovery mechanism identifies test files and functions based on naming patterns:

* Test files should be named with the prefix `test_` or suffix `_test.py`.
* Test functions should start with `test_`.

An example of a well-structured test file might look like this:

```python
 test_math_utils.py
from myapp.math_utils import add

def test_add_two_positive_numbers():
    assert add(2, 3) == 5

def test_add_with_zero():
    assert add(0, 4) == 4
```

Avoid overly generic names like `test_add`—use descriptive names that clearly state what is being tested.

**Using `@pytest.mark.parametrize`**

For repetitive test logic that changes only in inputs and expected results, `pytest.mark.parametrize` provides a clean way to test multiple scenarios:

```python
import pytest
from myapp.math_utils import multiply

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 6),
        (0, 5, 0),
        (-1, 5, -5),
        (4, -2, -8),
    ]
)
def test_multiply(a, b, expected):
    assert multiply(a, b) == expected
```

This reduces code duplication and improves test coverage.

## Fixtures, Markers, and Coverage Measurement

**Fixtures**

Fixtures in `pytest` allow you to set up and tear down test context. They are defined using the `@pytest.fixture` decorator and can be reused across tests:

```python
 conftest.py
import pytest
from myapp.database import Database

@pytest.fixture
def db_connection():
    db = Database.connect()
    yield db
    db.close()
```

In a test module:

```python
def test_user_fetch(db_connection):
    user = db_connection.get_user(1)
    assert user.username == "alice"
```

Fixtures can be scoped (function, module, session) to control their lifecycle and performance implications.

**Markers**

Markers are used to label tests for selective running or categorization. Common markers include `@pytest.mark.slow`, `@pytest.mark.asyncio`, or custom-defined tags.

```python
import pytest

@pytest.mark.slow
def test_large_dataset_processing():
    # Time-consuming test
    ...
```

To run only tests marked as slow:

```bash
pytest -m slow
```

**Measuring Coverage**

To measure code coverage during testing, use the `pytest-cov` plugin:

```bash
pytest --cov=myapp --cov-report=term-missing
```

This will show which lines are not covered by tests and help guide test development toward higher reliability.

## Enforcing Coverage Thresholds in CI

Code coverage alone does not guarantee correctness, but it is a useful proxy for how well your test suite exercises the codebase. In a CI/CD environment, enforcing a minimum coverage threshold ensures that all new code contributions maintain testing discipline.

To enforce thresholds locally or in CI:

```bash
pytest --cov=myapp --cov-fail-under=90
```

In a CI configuration file, such as GitHub Actions:

```yaml
- name: Run tests with coverage
  run: |
    pytest --cov=myapp --cov-fail-under=90
```

It is best to set thresholds as policy agreements within your team, striking a balance between completeness and pragmatism.

## Testing Asynchronous Code and Integration Tests

**Asynchronous Testing**

When testing asynchronous functions, `pytest` can integrate with `asyncio` using the `pytest-asyncio` plugin:

```python
import pytest
import asyncio
from myapp.async_utils import fetch_data

@pytest.mark.asyncio
async def test_fetch_data_returns_result():
    result = await fetch_data("https://example.com")
    assert "data" in result
```

Be cautious to isolate your tests; avoid making real HTTP calls by mocking or using tools such as `aiohttp`'s test utilities or `respx` for HTTP request interception.

**Integration Tests**

Integration tests evaluate multiple components working together, such as database access or external APIs. These often require setup such as containerized services (via Docker Compose) or sandbox environments.

Example of an integration test with a temporary test database:

```python
@pytest.mark.integration
def test_user_registration(db_connection, email_service):
    user = register_user("alice@example.com", "securepassword", db_connection, email_service)
    assert user.id is not None
    assert email_service.was_called_with("alice@example.com")
```

Integration tests should be clearly marked and may be separated from unit tests to control execution scope:

```bash
pytest -m integration
```

In CI pipelines, run unit tests on every push and integration tests less frequently or in dedicated pipelines to manage resources efficiently.
