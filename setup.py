from setuptools import setup

setup(
    name='noformat',
    version='0.1',
    packages=['noformat'],
    url='https://github.com/Palpatineli/noformat',
    download_url='https://github.com/Palpatineli/noformat/archive/0.1.tar.gz'
    license='GPLv3',
    author='Keji Li',
    author_email='mail@keji.li',
    description='save and load a structured collection of data as folder',
    extras_require={'pd': ['pandas']},
    install_requires=['numpy'],
    classifiers=['data storage', 'file format']
)
