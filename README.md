# black-junit

This project is a tool for generation JUnit report from black/blue output

# Install

`pip install black-junit`

# Usage

```bash
black . --check --verbose 2>results.txt
black-junit < results.txt > report.xml
```

or, in case using **blue** formatter:

```bash
blue . --check --verbose 2>results.txt
black-junit < results.txt > report.xml
```

# Badges

[![wakatime](https://wakatime.com/badge/github/Quantum-0/black-junit.svg)](https://wakatime.com/badge/github/Quantum-0/black-junit)
[![PyPI version](https://badge.fury.io/py/black-junit.svg)](https://badge.fury.io/py/black-junit)
[![Black](https://github.com/Quantum-0/black-junit/actions/workflows/black.yml/badge.svg)](https://github.com/Quantum-0/black-junit/actions/workflows/black.yml)

# License

[MIT License](./LICENSE)