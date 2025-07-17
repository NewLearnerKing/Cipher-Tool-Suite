from setuptools import setup, find_packages

setup(
    name='Ciphers',
    version='0.1.0',
    description='A collection of classical cryptographic ciphers with CLI',
    author='Your Name',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'ciphers-cli=cli:main',
        ],
    },
) 