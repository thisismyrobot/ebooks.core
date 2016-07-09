"""Tools to help with sentence generation."""
import collections
import re


SENTENCE_BREAKS = '!?.,-'


def normalise(word):
    """Normalise a word for frequency lookups."""
    word = re.sub('&', 'and', word)
    word = re.sub('/', 'or', word)
    word = re.sub(r'[^\w]', '', word)
    return word.lower()


def normal_map(corpus):
    """Return a dict of normalised words in the corpus to their various
    versions.
    """
    normals_map = collections.defaultdict(list)

    for sentence in corpus:
        for word in sentence.split(' '):
            normals_map[normalise(word)].append(word)

    try:
        del normals_map['']
    except KeyError:
        pass

    return normals_map
