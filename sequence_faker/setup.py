from setuptools import setup

setup(
   name='sequence_faker',
   version='1.0',
   description='A provider for faker to generate random numeric sequences',
   author='d chayes',
   packages=['sequence_faker'],
   install_requires=['Faker', 'noise'],
)