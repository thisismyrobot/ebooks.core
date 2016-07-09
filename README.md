# NOTE: This repo is still WIP as I'm migrating code from elsewhere into a proper Python package.

# ebook.core

A reliable, reusable and quite good sentence generate to help create "ebook"
chat bots from.

## Install

    pip install git+https://github.com/thisismyrobot/ebooks.core.git

## Usage


```python

    >>> import timr.ebook.core as core


    >>> with open('example_corpus.txt', 'rb') as corpf:
    ...     engine = core.Engine(corpf)

    >>> print engine.sentence()

```

## Tests

    pip install tox
    tox
