from setuptools import setup

setup(
    name='PythonStac',
    version='0.1.0',
    author='NRajasekar',
    author_email='neeraj.rajasekar@gmail.com',
    packages=['PythonStac'],
    url='http://pypi.python.org/pypi/PythonStac/',
    description='A pythonic package to interact with Stac API',
    install_requires=[
       "requests",
       "shapely",
   ],
)