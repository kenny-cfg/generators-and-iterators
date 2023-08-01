from unittest import TestCase
from CircleSequence import CircleSequence


class TestCircleSequence(TestCase):

    def test_with_string(self):
        sequence = CircleSequence('xyz', 5)

        result = list(sequence)

        self.assertEquals(result, ['x', 'y', 'z', 'x', 'y'])

    def test_with_list(self):
        sequence = CircleSequence([1, 2], 5)

        result = list(sequence)

        self.assertEquals(result, [1, 2, 1, 2, 1])

