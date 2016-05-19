#!/usr/bin/env python

#import ez_setup
#ez_setup.use_setuptools()
from setuptools import setup, find_packages
from distutils.core import Extension


VERSION='0.1'
LONG_DESCRIPTION = """
"""
setup(name='vecap',
	version=VERSION,
	description='vector coded aperture imaging',
	long_description=LONG_DESCRIPTION,
	author='vecap team',
	#author_email='alex@810lab.com',
	#url='http://www.810lab.com',
	packages=find_packages(),
	install_requires = [
		'ipython',
		'numpy',
		'scipy',
        'pandas',
		'matplotlib',
        'scikit-rf',
		],
	
	package_dir={'vecap':'vecap'},
	include_package_data = True,
	)

