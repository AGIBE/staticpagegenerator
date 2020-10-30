# -*- coding: utf-8 -*-
from distutils.core import setup
from setuptools import find_packages
import codecs
import os.path

def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), 'r') as fp:
        return fp.read()

def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")

setup(
      name = "staticpagegenerator",
      packages = find_packages(where="src"),
      version = get_version("src/staticpagegenerator/__init__.py"),
      package_dir = {"": "src"},
      # Abhängigkeiten
      install_requires = ["AGILib>=1.3.2"],
      # PyPI metadata
      author = "Peter Schär",
      author_email = "peter.schaer@be.ch",
      description = "Erstellt die statischen Suchseiten im Geoportal des Kantons Bern",
      url = "http://www.be.ch/oerebk",
      # https://pythonhosted.org/setuptools/setuptools.html#automatic-script-creation
    entry_points={
         'console_scripts': [
              'staticpagegenerator = staticpagegenerator.__main__:main',
              'spg = staticpagegenerator.__main__:main'
          ]
    }
)