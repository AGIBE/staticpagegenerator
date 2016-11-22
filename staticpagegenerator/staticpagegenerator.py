# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals
import staticpagegenerator.config
import staticpagegenerator.log
import requests
import os
import codecs

def download_content(url):
    result = requests.get(url)
    
    return result.text

def process_content(content):
    
    start_search_string = '<div class="catalog-searchresults">'
    end_search_string = '<!-- Top-Link -->'
    
    start_position = content.find(start_search_string)
    #start_position = start_position + len(start_search_string)
    
    end_position = content.find(end_search_string)
    
    extracted_content = content[start_position:end_position]    
    
    return extracted_content

def generate():
    config = staticpagegenerator.config.get_config()
    logger = staticpagegenerator.log.init_logging(config)
    
    base_url = config['URL']['baseurl']
    logger.info("Folgende Basis-URL wird verwendet:")
    logger.info(base_url)
    
    upload_dir = config['DIRECTORIES']['upload_dir']
    logger.info("Die HTML-Dateien werden gespeichert in ")
    logger.info(upload_dir)
        
    for staticpage in config['STATICPAGES'].items():
        
        print(staticpage[1])
        search_url = base_url + staticpage[1]['params']
        
        logger.info("Downloading content from ")
        logger.info(search_url)
        content = download_content(search_url)
        processed_content = process_content(content)
        
        upload_file = os.path.join(upload_dir, staticpage[1]['filename'])
        logger.info("Speichere " + upload_file)
        
        with codecs.open(upload_file, "w", "utf8") as f:
            f.write(processed_content)
       
    logger.info("Die statischen Seiten wurden erzeugt und abgespeichert.")
    print("SUCCESSFUL")