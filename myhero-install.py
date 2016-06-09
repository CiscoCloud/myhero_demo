#!/usr/bin/env python
from __future__ import print_function
from pprint import pprint

import os
import sys
import argparse
import requests
import time
import json
import uuid

PY3 = sys.version_info[0] > 2 #creates boolean value for test that Python major version > 2

class Defaults:
    MANTL_URI = 'https://mantlsandbox.cisco.com'
    MARATHON_API = '{0}/marathon/api/v2'
    APP_SUFFIX = 'app.mantldevnetsandbox.com'

class MyHeroInstall():

    def __init__(self, args):

        print("|**************************************************|")
        print("|Welcome to the MyHero app install script|")
        print("|**************************************************|")
        self.marathon_uri = Defaults.MARATHON_API.format(args.mantl_uri)
        self.auth = (args.username, args.password)
        self.req_headers = {'Content-type': 'application/json'}

    def deploy_data_service(self):

        print("|**************************************************|")
        print("|Deploying data service|")
        print("|**************************************************|")

        with open('sample-myhero-data.json') as sample:
            data = json.load(sample)

        resp = requests.post(self.marathon_uri, headers=self.req_headers,
                             data=json.dumps(data), verify=False)

        if 200 == resp.status_code:
            pprint(resp.json)
        else:
            self.handle_error(resp)

    def deploy_application_service(self):

        print("|**************************************************|")
        print("|Deploying application service|")
        print("|**************************************************|")

        # Just for testing
        time.sleep(5)

    def deploy_web_service(self):

        print("|**************************************************|")
        print("|Deploying web service|")
        print("|**************************************************|")

        # Just for testing
        time.sleep(5)

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Get things setup!', epilog="All done!")
    parser.add_argument('--name', dest='app_name', help='Provide a deployment name',
                        default=str(uuid.uuid1()))
    parser.add_argument('--mantl-uri', dest='mantl_uri',
                        help='The base URI for the Mantl control plane, including scheme.',
                        default=Defaults.MANTL_URI)
    parser.add_argument('--uri-suffix', dest='app_suffix',
                        help='The URI suffix for application routing on Mantl deployment.',
                        default=Defaults.APP_SUFFIX)
    parser.add_argument('--username', dest='username', required=True)
    parser.add_argument('--password', dest='password', required=True)
    args = parser.parse_args()

    install = MyHeroInstall(args)
    install.deploy_data_service()
    install.deploy_application_service()
    install.deploy_web_service()


    print("")
    print("Wait 5-10 minutes for the service to deploy")
    print("and then open the following page in your browser to view the application")
    print("")
    print("  http://" + args.app_name + ".app.mantldevnetsandbox.com")
