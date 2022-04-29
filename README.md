# New Relic - Common 3 Word Phrases

![Tests](https://github.com/PranayP86/three-word-sequences/actions/workflows/tests.yml/badge.svg)

Table of Contents

  - [Description](#Description)
  - [Installing and Running Program](#Installing-and-Running-Program)
    - [Prerequisites](#Prerequisites)
    - [Clone and Run Project](#Clone-and-Run-Project)
  - [Running Automated Tests](#Running-Automated-Tests)
  - [GitHub Actions Tests](#GitHub-Actions-Tests)
  - [Program Efficiency and Run Times](#Program-Efficiency-and-Run-Times)
  - [Dockerized App](#Dockerized-App)
  - [Development Notes and To Do](#Development-Notes-and-To-Do)
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
## GitHub Actions Tests

Along with the automated tests, you can view the Tox test that I've configured for GitHub Actions. This will, on each push or pull request, will run the Tox test in multiple Python environments on both Linux and Windows environments. 

This ensures that the app runs consistently across more machines, instead of just my local one. The "checkmark" by the commit and the Tox Test badge show that the code is passing.

## Program Efficiency and Run Times

I used Python's time module to check execution time on all the books in the sample directory.

These files were taken from the [Project Gutenberg Archive](https://www.gutenberg.org/):

| Book | Filename  | Size | Word Count |
| ---- |:---------:| ----:| ----------:|
| Moby Dick by Herman Melville | mobydick.txt | 1.2 MB | 212,063 |
| Anna Karenina by Leo Tolstoy| annakarenina.txt | 2 MB | 349,751 |
| Don Quixote by Miguel de Cervantes | donquixote.txt | 2.3 MB | 423,694 |

Using this, I could see if certain statements were taking longer than others.

The lowest time (initial, not consecutive runs) was:
```bash
___ 4.112549304962158 seconds ___
```
However, running consecutively many times increases the time inconsistently, ranging from 4.7 to 5.4 seconds. 
(Likely due to CPU usage).

## Dockerized App
I took a different approach for the extra credit. 
I decided to create a simple Flask app (basic setup), Dockerize it, and deploy it on Azure.

The image is built with the [Dockerfile](web_app/Dockerfile) and is running as a containerized web app. 
For the sake of time, I configured it to run on custom text values from an input field.

Note: When inputting my entire, combined text file (5.6 MB), it lags on the clipboard paste. If this happens, just wait while it completes pasting and then click "Submit".

[You can see it running here.](http://threewordsequences.eastus.azurecontainer.io/)

## Development Notes and To Do

- When parsing and trimming the text of escape characters and punctuation, I ended up using the .replace method in a for loop. With more time, I could've refactored some functions and maybe ran it ~1 second quicker. However, I did end up testing it with two regex statements (one for empty replacements and one for space replacements). This, for some reason, added 2-3 seconds to the average runtime compared to the .replace method. My thought process was that using methods like regex and .translate would offer "lower-level" efficiency, but .replace was the most efficient. With more time, I could optimize it further.
- The extra credit was initially supposed to use a database instance as well to allow another function of the app to list uploaded text files and responses from users. This would be displayed on another "Library" screen, ideally showing multiple books/filenames and their respective top 100 three word sequences. As I already spent a good deal of time into it, I decided to keep it simple, but with more time I'd have added that.
- With more time, I'd liked to have implemented some catches on the file uploads to validate that they are readable .txt files and added some tests. This would avoid potential reading and parsing errors.

## Known Issues

- No known issues as of now.
