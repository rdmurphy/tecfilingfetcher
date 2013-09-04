from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='tecfilingfetcher',
    version='0.0.3',
    description='A tool for processing raw filing files from the Texas Ethics Commission.',
    long_description=readme,
    author='Ryan Murphy',
    author_email='rmurphy@texastribune.org',
    url='https://github.com/rdmurphy/tecfilingfetcher',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    py_modules = ['tecfilingfetcher.tecfilingfetcher'],
    entry_points = {
      'console_scripts': [
          'fetchfiling = tecfilingfetcher.tecfilingfetcher:main',
        ]
    },
)
