from __future__ import print_function
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import io
import codecs
import os
import sys

import poisimulator

here = os.path.abspath(os.path.dirname(__file__))

def read(*filenames, **kwargs):
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)

long_description = read('README.txt', 'CHANGES.txt')

# This stuff likely won't work at present
class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errcode = pytest.main(self.test_args)
        sys.exit(errcode)

setup(
    name='poisimulator',
    version=poisimulator.__version__,
    url='http://github.com/dbuscher/poisimulator/',
    license='BSD 2-clause License',
    author='David Buscher',
    tests_require=['pytest'],
    install_requires=['numpy',
                    ],
    cmdclass={'test': PyTest},
    author_email='dfb@mrao.cam.ac.uk',
    description='Simulation framework for optical interferometers',
    long_description=long_description,
    packages=['poisimulator'],
    include_package_data=True,
    platforms='any',
    test_suite='poisimulator.test.test_poisimulator',
    classifiers = [
        'Programming Language :: Python',
        'Development Status :: 4 - Beta',
        'Natural Language :: English',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD Software License',
        'Operating System :: OS Independent',
        'Topic :: Scientific/Engineering :: Astronomy',
        'Topic :: Scientific/Engineering :: Physics',
        ],
    extras_require={
        'testing': ['pytest'],
    }
)