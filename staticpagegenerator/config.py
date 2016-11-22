# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals
import configobj
import os

def get_general_configfile_from_envvar():
    '''
    Holt den Pfad zur Konfigurationsdatei aus der Umgebungsvariable
    STATICPAGEGENERATORHOME und gibt dann den vollständigen Pfad (inkl. Dateiname)
    der Konfigurationsdatei zurück.
    '''
    config_directory = os.environ['STATICPAGEGENERATORHOME']
    config_filename = "config.ini"
    
    config_file = os.path.join(config_directory, config_filename)
    
    return config_file

def init_generalconfig():
    '''
    liest die zentrale Konfigurationsdatei in ein ConfigObj-Objet ein.
    Dieser kann wie ein Dictionary gelesen werden.
    '''
    config_filename = get_general_configfile_from_envvar()
    config_file = configobj.ConfigObj(config_filename, encoding="UTF-8")

    return config_file.dict()

def get_config():
    config = init_generalconfig()

    return config