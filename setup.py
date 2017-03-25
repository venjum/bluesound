from setuptools import setup, find_packages
import os.path

version = open(os.path.join(os.path.split(__file__)[0], "VERSION"), "rt").read().strip()

setup(
    name="bluesound",
    version=version,
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    install_requires=['xmltodict'],
    description='Bluesound API in python 3 for for controlling a Bluesound player',
    long_description=open('README.md').read(),
    author='Kai André Venjum',
    author_email='kai.andre@venjum.com',
    url='https://github.com/venjum/bluesound')
