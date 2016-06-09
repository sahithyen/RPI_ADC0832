from ez_setup import use_setuptools
use_setuptools()
from setuptools import setup, find_packages

setup(
    name = 'RPI_ADC0832',
    version = '1.0.0',
    author = 'Sahithyen Kanaganayagam',
    author_email = 'sahithyen@me.com',
    description = 'A python library to use the ADC0832 analog to digital converter with a Raspberry Pi',
    license = 'GPLv3',
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Operating System :: POSIX :: Linux',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development',
        'Topic :: System :: Hardware'
    ],
    url = 'https://github.com/sahithyen/RPI_ADC0832',
    packages = find_packages()
    )
