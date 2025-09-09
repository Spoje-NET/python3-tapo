#!/usr/bin/env python3

from setuptools import setup

setup(
    name='tapo',
    version='0.8.4',
    description='Unofficial Tapo API Client for TP-Link smart devices',
    author='Mihai Dinculescu',
    author_email='mihai.dinculescu@outlook.com',
    url='https://github.com/mihai-dinculescu/tapo',
    license='MIT',
    packages=[],  # We install from wheel manually
    python_requires='>=3.9',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Topic :: Software Development :: Embedded Systems',
        'Environment :: Console',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Topic :: Home Automation',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
    ],
)
