# NLTK-Me!

## Introduction

NLTK-Me! is an application based in the NLTK library for Python. It processes texts using different functions of NLTK, such as tokenizing texts, removing stopwords, searching frequency of a specific word or displaying a graph with the most frequent words. It comes with an user interface created with PySimpleGUI and designed in a simple and intuitive way, displaying information to the user regarding each function of the application.

## Description of functions

- **Text tokenizer**: Tokenizes (splits) a text into sentences. The text is split based on full stops. The function will create a file with the results, the user can choose the name for the file and the path where they want to save it.
- **Sentence tokenizer**: Tokenizes (splits) sentences into words. The sentences are split based on spaces. The function will create a file with the results, the user can choose the name for the file and the path where they want to save it.
- **Stopwords remover**: Removes the stopwords from a text. The stopwords are words with no meaning in the text, such as articles, prepositions or punctuation marks. The function will create a file with the results, the user can choose the name for the file and the path where they want to save it.
- **Count of total words**: Counts how many words are in the text. A popup window will appear with the result.
- **Frequency Distribution - Count**: Counts how many times a specific words appear in the text. The user can input the word to be counted. A popup window will appear with the result.
- **Frequency Distribution - Max**: Shows the most frequent word in a text. A popup window will appear with the result.
- **Frequency Distribution - Plot**: Displays a graph with the most frequent words in a text. The user can input the number of words that will be displayed.

## Requirements

Platform: Windows (tested in Windows 10 Home) \
Python 3.9.0 \
Python interpreter

## How To Run

Note: step 2 and onwards must be executed from the terminal, possibly requiring root privileges

1) Install Python3 (tested on 3.9.0) \
  https://www.python.org/downloads/
2) Upgrade pip: \
    \>> pip3 install --upgrade pip
3) Install pysimplegui: \
    \>> pip3 install pysimplegui
4) Install NLTK: \
    \>> pip3 install nltk
4) Install NLTK popular packages: \
    \>> python -m nltk.downloader popular
5) Install matplotlib: \
    \>> pip3 install matplotlib
5) Download the application from the path and run NLTK-Me!.py: \
    \>> python NLTK-Me!.py
6) Enjoy!

## Screenshots

Welcome Window



Main GUI in English


Main GUI in Spanish

