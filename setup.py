import sys
if sys.version[0] in '2':
    print("\n[0] Sorry! We do not support Python 2.x. Should you use Python 3.x, please. \n")

# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='Full Webcrawler | Upwork',
    version='0.1.0',
    description='Authenticate, exfiltrate and save informations from a Upwork user.',
    long_description=readme,
    author='kr4m3r',
    author_email='',
    url='https://github.com/att4ck3rs3cur1ty',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
