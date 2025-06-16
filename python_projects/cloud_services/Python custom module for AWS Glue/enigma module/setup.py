from setuptools import setup, find_packages

setup(
    name='enigma',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        "psycopg2-binary",  # Include psycopg2-binary as a dependency
        "uuid6"
    ],
)
