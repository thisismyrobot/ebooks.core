"""Tools to help with sentence generation."""
import re


def normalise_word(word):
    """Normalise a word for frequency lookups."""
    word = re.sub('&', 'and', word)
    word = re.sub(r'[^\w]', '', word)
    return word.lower()
