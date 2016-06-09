#!/usr/bin/env python

import os
import sys
import argparse
import time
from sys import version_info


py3 = version_info[0] > 2 #creates boolean value for test that Python major version > 2


class MyHeroInstall():

    def __init__(self):

        print("|**************************************************|")
        print("|Welcome to the MyHero app install script|")
        print("|**************************************************|")
        
    def deploy_data_service(self):
        
        print("|**************************************************|")
        print("|Deploying data service|")
        print("|**************************************************|")
        
        # Just for testing
        time.sleep(5)

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
    parser.add_argument('--name', dest='app_name', help='Provide a deployment name')
    args = parser.parse_args()
    
    install = MyHeroInstall()
    install.deploy_data_service()
    install.deploy_application_service()
    install.deploy_web_service()
    
    
    print("")
    print("Wait 5-10 minutes for the service to deploy")
    print("and then open the following page in your browser to view the application")
    print("")
    print("  http://" + args.app_name + ".app.mantldevnetsandbox.com")