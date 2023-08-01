from unittest import TestCase
from CircleSequence import CircleSequence


class TestCircleSequence(TestCase):

    def test_with_string(self):
        sequence = CircleSequence('xyz', 5)

        result = list(sequence)

        self.assertEquals(result, ['x', 'y', 'z', 'x', 'y'])


