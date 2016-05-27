from setuptools import setup

setup(
    name='noformat',
    version='0.1',
    packages=['noformat'],
    url='',
    license='',
    author='Keji Li',
    author_email='mail@keji.li',
    description='save and load a flat collection of arrays as folder',
    extras_require={'npy': ['numpy'], 'pd': ['pandas']},
    install_requires=[]
)
