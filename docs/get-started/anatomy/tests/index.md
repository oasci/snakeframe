# Testing Directory

The `tests/` directory is dedicated to storing all test code and lives outside of the `src/` directory.
This separation helps reinforce the boundary between production code and test code—your application does not depend on its own tests.

A basic example of the structure looks like this:

```
tests/
  test_main_module.py
  test_utils.py
  conftest.py
```

Each file in this directory corresponds to modules inside your source code.
This parallel structure makes it easy to find where tests live and how they relate to your implementation.

## Naming Conventions

* File names should start with `test_`.
For example, if you have a module named `core.py`, the corresponding test file should be named `test_core.py`.
* Function names inside those files should also begin with `test_` so tools like `pytest` can discover them automatically.

This consistent naming makes it easier for tooling to locate and run tests without needing extra configuration.

## Structural Mirroring

As your codebase grows, your test directory should reflect the structure of the `src/` directory.
This approach keeps your project organized and scalable.
For example:

```
src/
  mypackage/
    simulation/
      topo.py
    structure/
      center.py
tests/
  simulation/
    test_topo.py
  structure/
    test_center.py
```

This one-to-one mapping between source and test modules makes navigating and maintaining your code much easier—especially in large or collaborative projects.

## Shared Test Setup: `conftest.py`

A file named `conftest.py` can live at the root of your `tests/` directory or inside nested subfolders.
This is a special file used to define reusable test fixtures and shared setup logic.
It’s automatically recognized by test runners like `pytest` and can help reduce repetition in your test files.

If your project has specialized setup for different modules, it’s common to have multiple `conftest.py` files placed within subdirectories of `tests/` that match their respective areas of the codebase.

## Grouping Test Assets

When your tests rely on input files or temporary data (like configuration files, structures, or mock inputs), it’s best to organize these assets within the `tests/` directory:

```
tests/
  files/
    example_config.yaml
    dummy_input.json
  tmp/
    test_output/
```

This keeps your test data version-controlled, clearly separated from production assets, and scoped appropriately to the test environment.

