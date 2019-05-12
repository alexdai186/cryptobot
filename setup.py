from setuptools import setup, find_packages
from os import path

setup(name='cryptotrader',
      version='0.0.1',
      description='Standardized common API for several cryptocurrency exchanges.',
      package_dir={'':'src'},
      packages=find_packages(where='src'),
      install_requires=['requests', 'python-dateutil'],
      tests_require=['pytest'], 
      zip_safe=False
      )
