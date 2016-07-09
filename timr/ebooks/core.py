"""E-book core engine."""
import tools


class Engine(object):
    """E-book core engine."""
    def __init__(self, corpus_iterable):
        """Create an Engine instance, pass it an iterable of sentences."""
        self._corpus, self._normal_map = self._process(corpus_iterable)

    @property
    def corpus(self):
        """Return the current corpus."""
        return list(self._corpus)

    @staticmethod
    def _process(corpus_iterable):
        """Process the iterable of sentences."""
        try:
            iter(corpus_iterable)
        except TypeError:
            raise TypeError('Corpus must be an iterable.')

        normal_map = tools.normal_map(corpus_iterable)

        return corpus_iterable, normal_map
