from setuptools import setup
setup(
    name = 'pyfun',
    version = '0.1.0',
    packages = ['pyfun'],
    entry_points = {
        'console_scripts': [
            'pyfun = pyfun.__main__:main'
        ]
    })