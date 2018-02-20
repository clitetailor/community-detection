Community Detection
===================

Prerequisite
------------

> - Python 3

Instructions
------------

- First, create an application and an endpoint at [Twitter/Getting Started App](https://developer.twitter.com/en/docs/basics/getting-started#get-started-app).
- Replace the sample fields in `src/config.sample.yaml` with 
your own access token key and consumer key.

```yaml
access_token_key: <access-token-key>
access_token_secret: <access-token-secret>
consumer_key: <consumer-key>
consumer_secret: <consumer-secret>
```

- Follow the following instructions to setup the project.
- Run `src/twitter_app.py` and see the result in `src/output.yaml` file.

```bash
python src/twitter_app.py
```

**output.yaml**

```yaml
- contributors: null
  coordinates: null
  created_at: Fri Feb 09 02:37:44 +0000 2018
  entities:
    hashtags: []
    symbols: []
    urls:
    - display_url: turing-nlp.github.io
      expanded_url: https://turing-nlp.github.io
      indices: [69, 92]
      url: https://t.co/5HQxR3yqN8
...
```

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
