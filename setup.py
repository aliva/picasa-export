#!/usr/bin/env python3

from distutils.core import setup

setup(
    name='picasa-export',
    version='1.0',
    description='exports your media from google-photos/picasa',
    author='Ali Vakilzade',
    author_email='ali@vakilzade.ir',
    url='https://github.com/aliva/picasa-export/',
    scripts=[
        "picasa-export",
    ],
    install_requires=open("requirements.txt", "r").readlines()
)
