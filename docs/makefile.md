# Makefile

We automate all DevOps with a [Makefile][gnu-make].

## Environment

### Conda packages

```bash
make conda-create \
make conda-setup \
make conda-dependencies \
make nodejs-dependencies
```

TODO: Instructions for adding conda packages

```bash
conda activate <project_name>
```

```bash
make conda-lock
```

```bash
make pre-commit-install
```

### PyPI packages

```bash
conda activate <project_name>
```

### Reproduce

```bash
make environment
```

### Update

```bash
make locks
```

## Formatting

```bash
make formatting
```

```bash
make validate
```

```bash
make lint
```

## Testing

```bash
make test
```

## Building

```bash
make build
```

## Cleaning

```bash
make cleanup
```

## Documentation

```bash
make serve
```

[gnu-make]: https://www.gnu.org/software/make/manual/html_node/index.html
