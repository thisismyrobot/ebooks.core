"""Tests tools."""
import timr.ebook.tools as tools


def test_normalise():
    """Word normalising."""
    assert tools.normalise('G\'day!') == 'gday'


def test_normal_map():
    """The normal map maps normalised words to their variations."""
    corpus = (
        'Hello, my name is Robert.',
        'Good morning, how are you?',
        'It\'s nice to finally meet',
        'I really, really, really like to eat a lot of cake.',
        'That really isn\'t the best name for a dog.',
    )

    assert tools.normal_map(corpus) == {
        'a': ['a', 'a'],
        'are': ['are'],
        'best': ['best'],
        'cake': ['cake.'],
        'dog': ['dog.'],
        'eat': ['eat'],
        'finally': ['finally'],
        'for': ['for'],
        'good': ['Good'],
        'hello': ['Hello,'],
        'how': ['how'],
        'i': ['I'],
        'is': ['is'],
        'isnt': ["isn't"],
        'its': ["It's"],
        'like': ['like'],
        'lot': ['lot'],
        'meet': ['meet'],
        'morning': ['morning,'],
        'my': ['my'],
        'name': ['name', 'name'],
        'nice': ['nice'],
        'of': ['of'],
        'really': ['really,', 'really,', 'really', 'really'],
        'robert': ['Robert.'],
        'that': ['That'],
        'the': ['the'],
        'to': ['to', 'to'],
        'you': ['you?']
    }
