from faker.providers import BaseProvider
from noise import snoise2

from random import random
from functools import reduce
import math
import operator


class SequenceFaker(BaseProvider):
    """A faker provider to provide random number sequences"""
    SINUSOIDAL_SETS = [
        (lambda x: math.sin(x * 38)),
        (lambda x: math.sin(x * 10)),
        (lambda x: math.cos(x * 80)),
        (lambda x: math.cos(x * 2)),
    ]

    def product(self, iterable):
        return reduce(operator.mul, iterable, 1)

    def uniform(self, i, min, max):
        return min + (random() * (max - min))

    def perlin(self, i, min, max):
        return min + ((snoise2(x=i, y=0) + 1)/2 * (max - min))

    def sinusoidal(self, i, min, max):
        return (self.product([
                    x(i) for x in self.SINUSOIDAL_SETS
                ])/2 + .5) * (max - min) + min

    SEQUENCE_TYPES = {
        'UNIFORM': uniform,
        'SINUSOIDAL': sinusoidal,
        'PERLIN': perlin,
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
                    value=self.SEQUENCE_TYPES[sequence_type](self, i, min, max),
                    should_round=should_round,
                    ndigits=ndigits
                )
                for i in range(count)
            ]
        except KeyError as e:
            raise KeyError(
                'The sequence type "{}" does not exist.'.format(e.args[0])
            )
