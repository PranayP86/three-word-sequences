# New Relic - Common 3 Word Phrases

![Tests](https://github.com/PranayP86/three-word-sequences/actions/workflows/tests.yml/badge.svg)

Table of Contents

  - [Description](#Description)
  - [Installing and Running Program](#Installing-and-Running-Program)
    - [Prerequisites](#Prerequisites)
    - [Clone and Run Project](#Clone-and-Run-Project)
  - [Program Efficiency / Run Times](#Program-Efficiency-/-Run-Times)
  - [Running Automated Tests](#Running-Automated-Tests)
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

```bash
# Clone this repo
git clone ---repo here

# Run the program file and pass file arguments
python src/__main__.py sample/*

Or

# You can use stdin input method (cat) to run program
cat sample/* | python3 src/__main__.py 
```

## Program Efficiency / Run Times

## Running Automated Tests

## Docker

## Development Notes

## To Do

## Known Issues

