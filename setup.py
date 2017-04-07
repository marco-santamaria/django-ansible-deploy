from pycon8 import __version__
from setuptools import setup, find_packages

setup(
    name='pycon8',
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    version=__version__,
    install_requires=[]
)
