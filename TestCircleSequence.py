from unittest import TestCase
from CircleSequence import CircleSequence


class TestCircleSequence(TestCase):

    def test_with_string(self):
        sequence = CircleSequence('xyz', 5)
