# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals
import argparse
import staticpagegenerator.staticpagegenerator
from staticpagegenerator import __version__

def main():
    version_text = "staticpagegenerator v" + __version__
    parser = argparse.ArgumentParser(description="staticpagegenerator: Erzeugt die HTML-Files für die statischen Suchen im Geoportal-CMS.", prog="staticpagegenerator.exe", version=version_text)
    
    args = parser.parse_args()
    #args.func(args)

    staticpagegenerator.staticpagegenerator.generate()
    
if __name__ == "__main__":
    main()