# -*- coding: utf-8 -*-
# übernommen aus: https://pythonhosted.org/setuptools/setuptools.html#id24
import ez_setup
from staticpagegenerator import __version__
import staticpagegenerator
ez_setup.use_setuptools()

from setuptools import setup, find_packages
setup(
      name = "staticpagegenerator",
      packages = find_packages(),
      version = __version__,
      # Abhängigkeiten
      install_requires = ["chromalog==1.0.4", "requests==2.8.0"],
      # PyPI metadata
      author = "Peter Schär",
      author_email = "peter.schaer@bve.be.ch",
      description = "Generiert statische HTML-Seite für die Suchen im Geoportal-CMS",
      url = "http://www.be.ch/geoportal",
      # https://pythonhosted.org/setuptools/setuptools.html#automatic-script-creation
    entry_points={
         'console_scripts': [
              'staticpagegenerator = staticpagegenerator.commandline:main',
              'spg = staticpagegenerator.commandline:main'
          ]
    }
)