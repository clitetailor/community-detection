Community Detection
===================

Prerequisite
------------

> - Python 3

Install
-------

To install project dependencies, run the following command in cmd or bash:

```bash
# use pip3 on Linux
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
````

Incase you want to debug test with vscode, run `./test.py`.

Run test coverage:

```
py.test --cov=src
```
