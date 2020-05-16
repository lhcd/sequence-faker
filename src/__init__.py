from faker import Faker
from faker.providers import BaseProvider

from random import random
from noise import snoise2


class SequenceFaker(BaseProvider):
    """A faker provider to provide random number sequences"""

    def uniform(i, min, max):
        return (random() * (max - min))

    def perlin(i, min, max):
        return ((snoise2(x=i, y=0) + 1)/2 * (max - min))

    def sinusoidal(i, min, max):
        pass

    SEQUENCE_TYPES = {
        'UNIFORM': uniform,
        'SINUSOIDAL': sinusoidal,
        'PERLIN': perlin,
        # 'SMOOTH_NOISE': ,
        # 'SHARP_NOISE': ,
    }

    def round_value(self, value, should_round, ndigits):
        if should_round:
            return round(value, ndigits)
        return value

    def sequence(
        self,
        sequence_type='UNIFORM',
        min=0,
        max=1,
        count=10,
        should_round=False,
        ndigits=2
    ):
        try:
            return [
                self.round_value(
                    value=self.SEQUENCE_TYPES[sequence_type](i, 0, 1),
                    should_round=should_round,
                    ndigits=ndigits
                )
                for i in range(count)
            ]
        except KeyError as e:
            raise KeyError(
                'The sequence type "{}" does not exist.'.format(e.args[0])
            )


fake = Faker()
fake.add_provider(SequenceFaker)
