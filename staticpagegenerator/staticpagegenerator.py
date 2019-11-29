# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals
import staticpagegenerator.config
import staticpagegenerator.log
import requests
import os
import codecs

def download_content(url, timeout, logger):

    result_text = ""

    try:
        # #3500: Aufruf der URL mit einem Timeout
        response = requests.get(url, timeout=timeout)
        # Prüfen, ob ein Fehler vorliegt (Statuscode != 200)
        response.raise_for_status()
        result_text = response.text
    # Timeout-Exception abfangen
    except requests.exceptions.ReadTimeout as exc:
        logger.warn("Timeout beim Herunterladen erreicht...")
        logger.warn(exc)
    # Alle übrigen Requests-Exceptions abfangen (z.B. HTTP 500 etc)
    except requests.exceptions.RequestException as exc:
        logger.warn("Anderer Fehler beim Herunterladen erreicht...")
        logger.warn(exc)

    return result_text

def process_content(content):
    
    start_search_string = '<div class="catalog-searchresults">'
    end_search_string = '<!-- Top-Link -->'
    
    start_position = content.find(start_search_string)
    end_position = content.find(end_search_string)
    
    extracted_content = content[start_position:end_position]    
    
    return extracted_content

def generate():
    '''
    Erzeugt die HTML-Files, mit denen die statischen
    Suchen im Geoportal betrieben werden.
    Vorlage = https://bitbucket.org/stubr/staticpagegenerator
    '''
    config = staticpagegenerator.config.get_config()
    logger = staticpagegenerator.log.init_logging(config)
    
    base_url = config['URL']['baseurl']
    logger.info("Folgende Basis-URL wird verwendet:")
    logger.info(base_url)
    
    upload_dir = config['DIRECTORIES']['upload_dir']
    logger.info("Die HTML-Dateien werden gespeichert in ")
    logger.info(upload_dir)

    timeout = float(config['TIMEOUT']['timeout'])
    logger.info("Es wird ein Timeout von %s Sekunden verwendet." % (unicode(timeout)))

    min_filesize = int(config['FILESIZE']['min_filesize'])
    logger.info("Es wird eine minimale Dateigrösse von %s Bytes verwendet." % (unicode(min_filesize)))
        
    for staticpage in config['STATICPAGES'].items():

        upload_file = False
        
        search_url = base_url + staticpage[1]['params']
        
        logger.info("Downloading content from ")
        logger.info(search_url)
        content = download_content(search_url, timeout, logger)

        # Heruntergeladener Inhalt prozessieren
        processed_content = process_content(content)
        processed_content_length = len(processed_content)
        
        upload_file = os.path.join(upload_dir, staticpage[1]['filename'])

        # #3500: das File wird nur geschrieben, wenn eine bestimmte Dateigrösse
        # erreicht wird. Damit wird erreicht, dass im Falle der ausgefallenen
        # dynamischen Suche kein leeres File erzeugt wird, sondern das alte
        # File bestehen bleibt.
        logger.info("Länge des Files: " + unicode(processed_content_length))
        if processed_content_length > min_filesize:
            logger.info("Minimale Dateigrösse ist erreicht.")
            logger.info("Speichere " + upload_file)
            with codecs.open(upload_file, "w", "utf8") as f:
                f.write(processed_content)
        else:
            logger.warn("Minimale Dateigrösse ist nicht erreicht.")
            logger.warn("Die Datei wird nicht ersetzt.")
       
    logger.info("Die statischen Seiten wurden erzeugt und abgespeichert.")
    print("SUCCESSFUL")