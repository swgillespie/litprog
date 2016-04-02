from setuptools import setup

setup(
    name='litprog',
    description='A small utility for working with literate programs',
    author='Sean Gillespie',
    author_email='sean.william.g@gmail.com',
    url='https://github.com/swgillespie/litprog',
    version='0.0.1',
    py_modules=['litprog'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        litprog=litprog.main:convert
    ''',
)
