"""
A basic setup.py
"""

from setuptools import setup

setup(
    name='sample',
    version='1.2.0',
    description='A sample Python project',
    url='https://github.com/amitsaha/learning/python/pip_editable',
    author='Foo Bear',
    author_email='foo@bear.com',
    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
    ],

    packages=['sample'],
    entry_points={
        'console_scripts': [
            'hello=sample.hello:main',
        ],
    },
)
