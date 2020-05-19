import unittest
from faker import Faker
from sequence_faker.src import SequenceFaker

class TestSequenceFaker(unittest.TestCase):
    def setUp(self):
        self.fake = Faker()
        self.fake.add_provider(SequenceFaker)

    def test_sequence_type_range_adherence(self):
        for sequence_type in SequenceFaker.SEQUENCE_TYPES:
            actual = self.fake.sequence(sequence_type=sequence_type, min=10, max=50, count=1)[0]
            self.assertLessEqual(actual, 50)
            self.assertGreaterEqual(actual, 10)

    def test_sequence_type_count(self):
        for sequence_type in SequenceFaker.SEQUENCE_TYPES:
            actual = self.fake.sequence(sequence_type=sequence_type, count=20)
            self.assertEqual(len(actual), 20)

    def test_rounding(self):
        for sequence_type in SequenceFaker.SEQUENCE_TYPES:
            actual = self.fake.sequence(sequence_type=sequence_type, count=1, should_round=True, ndigits=None)[0]
            self.assertTrue(isinstance(actual, int))

            actual = self.fake.sequence(sequence_type=sequence_type, count=1, should_round=True, ndigits=2)[0]
            self.assertEqual(round(actual, 2), actual)


    def test_hardcoded_sequences(self):
        pass
