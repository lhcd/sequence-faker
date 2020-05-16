An addon to [faker](https://faker.readthedocs.io/en/stable/index.html) that generates characteristic sequences of random numbers for use in tests and mockups.

Example usage:

```python
>>> from faker import Faker
>>> from src import SequenceFaker
>>>
>>> fake = Faker()
>>> fake.add_provider(SequenceFaker)
>>>
>>> fake.sequence()
[0.6405127858469346, 0.21318226720074995, 0.19062564771416513, 0.45144176672346736, 0.5896017221495276, 0.4391766415951077, 0.06970482622241192, 0.8961255893311826, 0.7081595828054668, 0.34737949828859205]
>>> fake.sequence(sequence_type='PERLIN', count=5, should_round=True, ndigits=2)
[0.5, 0.46, 0.49, 0.62, 0.55]
```