# Installation and execution of `grin-portal-client`

This python package is for https://grin-portal.broadinstitute.org/.

### 1. install poetry

Make sure that **Poetry** is installed on your system.

To install **Poetry**, run the following command:

```bash
pip install poetry
````

#### Check the installation

```bash
poetry --version
````

If the command fails, ``Python\Scripts`` must be added to the PATH environment variable.

### 2. install the project
Clone or download the project. Then go to the project directory and execute the following command
to install all dependencies:


```bash
poetry install --dev
````

### 3. run the application
You can run the project with Poetry by using the following command:

```bash
poetry run grin-portal-client
````

or

```bash
poetry run python -m grin-portal-client
````

### 4. run tests
To run tests (if available), use:

```bash
poetry run pytest
````
