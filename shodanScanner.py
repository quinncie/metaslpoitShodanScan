# 2/20/24 Metasploit Module Draft 1
# Havent actually gotten this to run yet, who know if it works.
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging

dependencies_missing = False
try:
    import requests
except ImportError:
    dependencies_missing = True

from shodan import Shodan

from metasploit import module

metadata = {
    'name': 'Shodan API',
    'description': '''
        This is a Metasploit module that uses the Shodan API to scan ips 
        and dumps the open ports and the headers.
    ''',
    'authors': [
        'Quinn Cotter'
    ],
    'date': '2024-02-20',
    'license': 'MSF_LICENSE',
    'references': [
        {'type': 'url', 'ref': 'https://blog.rapid7.com/2017/12/28/regifting-python-in-metasploit/'},
    ],
    'type': 'single_scanner',
    'options': {
        'rhost': {'type': 'address', 'description': 'Target address', 'required': True, 'default': None},
        'apikey': {'type': 'string', 'description': 'Shodan API Key', 'required': True, 'default': None}
    }
}

class cpd_shodan_search:    
    def __init__(self, api, ip):
        self.api = api
        self.ip = ip

def apiSearch(args):
    SHDN = cpd_shodan_search((args['apikey']), (args['rhost']))
    api = Shodan(str(SHDN.api))
    ipinfo = api.host(str(SHDN.ip))
    return ipinfo

def run(args):
    module.LogHandler.setup(msg_prefix='{} - '.format(args['rhost']))
    ipinfo = apiSearch(args)
    portList = []
    headerList = []
    for item in ipinfo['data']:
        portList.append(item.get('port', 'N/A'))
        headerList.append(item.get('product', 'N/A'))
    logging.info("""
            {}
            {}
            """.format(portList, headerList))

module.run(metadata, run)
