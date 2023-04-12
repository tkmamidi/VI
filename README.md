# Variant Interpreter

## Table of Contents

- [Variant Interpreter](#variant-interpreter)
    - [Aim](#aim)
    - [Description](#description)
    - [Data](#data)
        - [Installation](#installation)
        - [Requirements](#requirements)
        - [Activate pip environment](#activate-pip-environment)
        - [Steps to run ](#steps-to-run)
    - [Contact Info](#contact-info)

## Aim

Easy to use web interface for biologists to look for variants and understand their deleteriousness using DITTO scores.

## Description

A web app where anyone can lookup variants and understand the mechanism/details of
these variants such as domain, function, DITTO deleterious score and Clinvar reported significance.

## Data

We are using predictions from DITTO streamlit app.

### Installation

Installation simply requires fetching the source code. Following are required:

- Git

To fetch source code, change in to directory of your choice and run:

```sh
git clone -b pkd \
    https://github.com/tkmamidi/VI.git
```

### Requirements

*OS:*

Currently works only in Mac OS. Docker versions may need to be explored later to make it useable in Mac (and
potentially Windows).

*Tools:*

- Pip3

### Activate pip environment

Change in to root directory and run the commands below:

```sh
# create environment. Needed only the first time.
pip3 install -r requirements.txt
```

### Steps to run

```sh
python src/pyqt5_vi.py
```

## Contact Info

Tarun Mamidi | tmamidi@uab.edu
