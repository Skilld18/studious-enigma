#!/usr/bin/env python

"""A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
# noinspection PyUnresolvedReferences
from codecs import open
from os import path

from setuptools import setup

from studious import version

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name=version.__name__,


    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version=version.__version__,

    description='A sample Python project',
    long_description=long_description,

    # The project's main homepage.
    url='https://github.com/Skilld18/studious-enigma',

    # Author details
    author='Russell Dunk',
    author_email='rdunk@mail.uoguelph.ca',

    # Choose your license
    license='MIT',

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Education',
        'Topic :: Education :: Computer Aided Instruction (CAI)'

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3.5',
    ],

    # What does your project relate to?
    keywords='learn education programming challenges practice',


    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    # TODO:: This doesn't install a sql lib that is needed
    install_requires=['psycopg2', 'argparse'],
    test_suite='nose.collector',
    tests_require=['nose'],


)
