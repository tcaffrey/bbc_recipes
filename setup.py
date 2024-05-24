from setuptools import setup, find_packages

setup(
    name='bbc_recipes',
    version='0.1.0',
    author='Thomas Caffrey',
    description='A project to scrape recipe metadata from the BBC Food pages to conduct analysis / modelling',
    url='https://github.com/tcaffrey/bbc_recipes',
    packages=find_packages(include=['src', 'src.*'])
)