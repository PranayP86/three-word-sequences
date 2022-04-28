# New Relic - Common 3 Word Phrases

![Tests](https://github.com/PranayP86/three-word-sequences/actions/workflows/tests.yml/badge.svg)

Table of Contents

  - [Description](#Description)
  - [Installing and Running Program](#Installing-and-Running-Program)
    - [Prerequisites](#Prerequisites)
    - [Clone and Run Project](#Clone-and-Run-Project)
  - [Running Automated Tests](#Running-Automated-Tests)
  - [Program Efficiency and Run Times](#Program-Efficiency-and-Run-Times)
  - [Docker](#Docker)
  - [Development Notes](#Development-Notes)
  - [To Do](#To-Do)
  - [Known Issues](#Known-Issues)

## Description

Python program that, when given text file(s), will return a list of the top 100 most common 3-word sequences in descending order of frequency.

## Installing and Running Program


### Prerequisites

Python 3 (3.7 or higher) is required. Run `python --version`to check version:

```bash
$ python --version
Python 3.7.12
```

### Clone and Run Project

Sample text files can be found in the 'src/files/' directory.
First, set up package dependencies:

```bash
# Clone this repo
git clone https://github.com/PranayP86/three-word-sequences.git

# Setup package dependencies (root directory)
pip install -e .
```

Running the program:

```bash
# Run the program file and pass file arguments
python src/challenge/app.py sample/*

Or

# You can use stdin input method (cat) to run program
cat sample/* | python src/challenge/app.py
```

## Running Automated Tests

To run tests, first install the dev dependencies:

```bash
$ pip install -r requirements_dev.txt
```

Now you should be able to run tests (pytest, mypy, flake8, tox):

```bash
# Run pytest
$ pytest --cov src

# Run mypy
$ mypy src

# Run flake8 (should return nothing if passed)
$ flake8 src

# Run tox test locally (tests Python 3.7-3.9)
# Note: Made to work with GitHub Actions. Will throw InterpreterNotFound for any version not installed if running locally.
$ tox
```

## Program Efficiency and Run Times

I used Python's time module to check execution time on all the books in the sample directory.

These files were taken from the [Project Gutenberg Archive](https://www.gutenberg.org/):

| Book | Filename  | Size | Word Count |
| ---- |:---------:| ----:| ----------:|
| Anna Karenina by Leo Tolstoy| annakarenina.txt | 2 MB | 349,751 |
| Don Quixote by Miguel de Cervantes | donquixote.txt | 2.3 MB | 423,694 |
| Moby Dick by Herman Melville | mobydick.txt | 1.2 MB | 212,063 |

Using this, I could see if certain statements were taking longer than others.

The lowest time (initial, not consecutive runs) was:
```bash
___ 4.112549304962158 seconds ___
```
However, running consecutively many times increases the time inconsistently, ranging from 4.7 to 5.4 seconds. 
(Likely due to CPU usage)

## Docker

## Development Notes

## To Do

## Known Issues

