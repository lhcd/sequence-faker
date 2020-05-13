from faker import Faker
from faker.providers import BaseProvider

import random

class SequenceFaker(BaseProvider):
    """A faker provider to provide random number sequences"""
    def uniform(i, min, max):
        return random.random()

    def round()

    SEQUENCE_TYPES = {
        'UNIFORM': uniform,
        # 'SINUSOIDAL': ,
        # 'PERLIN': ,
        # 'SMOOTH_NOISE': ,
        # 'SHARP_NOISE': ,
    }

    def sequence(self, sequence_type='UNIFORM', min=0, max=1, count=10, integer=False, ndigits=2):
        try:
            return [self.SEQUENCE_TYPES[sequence_type](i) for i in range(count)]
        except KeyError as e:
            raise KeyError('The sequence type "{}" does not exist.'.format(e.args[0]))

fake = Faker()
fake.add_provider(SequenceFaker)
print(fake.sequence())