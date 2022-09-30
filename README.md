# black-junit

This project is a tool for generation JUnit's report from black/blue output

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
[![Black](https://github.com/Quantum-0/black-junit/actions/workflows/black.yml/badge.svg)](https://github.com/Quantum-0/black-junit/actions/workflows/black.yml)
[![GitHub Org's stars](https://img.shields.io/github/stars/quantum-0/black-junit)](https://github.com/Quantum-0/black-junit/)
![PyPI - License](https://img.shields.io/pypi/l/black-junit)
[![PyPI](https://img.shields.io/pypi/v/black-junit)](https://pypi.org/project/black-junit/)
![PyPI - Status](https://img.shields.io/pypi/status/black-junit)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/black-junit)
![PyPI - Downloads](https://img.shields.io/pypi/dm/black-junit)


# License

[MIT License](./LICENSE)