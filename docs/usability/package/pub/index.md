# Publishing to PyPI

Once your Python package has been built and validated, you can share it with the world by publishing it to [PyPI](https://pypi.org)—the Python Package Index. PyPI is the central repository for Python packages and allows users to install your project using tools like `pip`.

## Registering a PyPI Account

Before you can publish a package, you need an account on PyPI.

1. Go to: [https://pypi.org/account/register/](https://pypi.org/account/register/)
2. Create your account and verify your email address.
3. Navigate to "Account settings" and create an API token:

   * Click "Add API token"
   * Choose a name (e.g. "mypackage-deploy-token")
   * Optionally scope it to a specific project
   * Copy the token immediately—it won’t be shown again

Store this token securely. You can use it in one of two ways:

* As an environment variable (`TWINE_PASSWORD`)
* In a `.pypirc` configuration file in your home directory

## Uploading with `twine`

PyPI does not accept direct uploads from `pip` or `python setup.py`. Instead, you must use a dedicated tool like [`twine`](https://twine.readthedocs.io/), which securely uploads your built distributions.

### Step 1 – Install Twine

```bash
pip install twine
```

### Step 2 – Upload to PyPI

After building your package (which creates files in `dist/`), upload them with:

```bash
twine upload dist/*
```

Twine will:

* Prompt you for your username (`__token__`) and password (your API token)
* Upload all `.whl` and `.tar.gz` files in the `dist/` folder
* Display a success message or explain what went wrong

## Managing Credentials

There are two common ways to manage your PyPI credentials.

### Option 1 – Environment Variables

```bash
export TWINE_USERNAME="__token__"
export TWINE_PASSWORD="pypi-AgENdGVzd..."
```

This is ideal for automation or short-term sessions. Be sure to unset the password or use a secure `.env` file.

### Option 2 – `.pypirc` File

Place this in your home directory (`~/.pypirc`):

```ini
[distutils]
index-servers =
    pypi

[pypi]
  username = __token__
  password = pypi-AgENdGVzd...
```

Make sure this file is readable only by you (`chmod 600 ~/.pypirc`) to avoid exposing your token.

## Publishing to TestPyPI

Before uploading to the real PyPI, it's often a good idea to test the upload process using [TestPyPI](https://test.pypi.org), which is a sandboxed version of PyPI.

### Upload to TestPyPI

```bash
twine upload --repository-url https://test.pypi.org/legacy/ dist/*
```

You will need to:

* Create a separate account on [https://test.pypi.org](https://test.pypi.org)
* Generate a separate API token
* Install from TestPyPI using:

```bash
pip install --index-url https://test.pypi.org/simple/ mypackage
```

Testing here helps you catch formatting or metadata issues before a public release.

