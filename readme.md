An addon to [faker](https://faker.readthedocs.io/en/stable/index.html) that generates characteristic sequences of random numbers for use in tests and mockups.

Example usage:

```python
from faker import Faker
from src import SequenceFaker

fake = Faker()
fake.add_provider(SequenceFaker)
random_sequence = fake.sequence()
perlin_sequence = fake.sequence(sequence_type='PERLIN', count=5, should_round=True, ndigits=2)
```