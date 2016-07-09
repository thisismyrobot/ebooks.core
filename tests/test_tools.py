"""Tests tools."""
import timr.ebook.tools as tools


def test_normalise():
    """Word normalising."""
    assert tools.normalise_word('G\'day!') == 'gday'
