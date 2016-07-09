"""Tests core."""
import pytest

import timr.ebooks.core as core


def test_corpus_must_be_iterable():
    """Corpus must be an iter of sentences."""
    with pytest.raises(TypeError):
        core.Engine(34)
