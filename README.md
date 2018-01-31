Community Detection
===================

Prerequisite
------------

> - Python 3

Install
-------

To install project dependencies, run the following command in cmd or bash:

```bash
# use pip3 on linux
pip install -r requirement.txt
```

In powershell, you need to replace `pip` with `pip.exe` in order to make it work.

Testing
-------

You can run test by running either one of the following commands:

```bash
# pytest.exe in powershell
pytest

# py.test.exe in powershell
py.test

# use git bash on windows
scripts/test.sh
````

Incase you want to debug test with vscode, run `./test.py`.

Run test coverage:

```bash
py.test --cov=src --cov-config .coveragerc

# use git bash on windows
scripts/cov.sh
```
