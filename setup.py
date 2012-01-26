from setuptools import setup, find_packages
import sys, os

here = os.path.abspath(os.path.dirname(__file__))
readme = open(os.path.join(here, 'README')).read()
news = open(os.path.join(here, 'NEWS')).read()

version = '0.0.1'

requirements = []

setup(
        name='Kosmonaut',
        version=version,
        description='',
        long_description=(readme + '\n\n' + news),
        keywords='',
        author='Krzysztof Kowalik & Pablo Astigarraga',
        author_email='dev+nu7+pote@cuboxlabs.com',
        url='http://github.com/webrocket/kosmonaut.py',
        license='MIT',
        packages=find_packages('src'),
        package_dir={'': 'src'},
        namespace_packages=[],
        include_package_data=True,
        zip_safe=False,
        install_requires=requirements,
        )
