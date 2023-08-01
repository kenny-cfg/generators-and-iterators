from unittest import TestCase
from CircleSequence import circle_generator


class TestCircleGenerator(TestCase):

    def test_with_string(self):
        sequence = circle_generator('xyz', 5)

        result = list(sequence)

        self.assertEquals(result, ['x', 'y', 'z', 'x', 'y'])

    def test_with_list(self):
        sequence = circle_generator([1, 2], 5)

        result = list(sequence)

        self.assertEquals(result, [1, 2, 1, 2, 1])

