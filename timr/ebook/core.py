"""E-book core engine."""


class Engine(object):
    """E-book core engine."""
    def __init__(self, corpus_iterable):
        """Create an Engine instance, pass it an iterable of sentences."""
        self._corpus = self._process(corpus_iterable)

    def _process(self, corpus_iterable):
        """Process the iterable of sentences."""
        try:
            iter(corpus_iterable)
        except TypeError:
            raise Exception('Corpus must be an iterable.')
