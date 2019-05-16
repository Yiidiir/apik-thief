import os
from dotenv import load_dotenv
import argparse
from shodan import Shodan
from bs4 import BeautifulSoup
import re
import urllib.parse as urlparse
import requests

load_dotenv()
parser = argparse.ArgumentParser()
parser.add_argument("-s", "--service", help="Specify what service to look for", choices=['googleMaps'])
args = parser.parse_args()

api = Shodan(os.getenv('SHODAN_API'))
if (args.service == "googleMaps"):
    def checkGoogleMapsApiKey(key):
        if key not in validMapsApiKeys:
            r = requests.head(
                'https://maps.googleapis.com/maps/api/js?v=3.exp&libraries=places&signed_in=true&key=' + format(key))
            if (r.status_code == 200):
                validMapsApiKeys.add(key)
                with open("maps_keys.txt", "a") as txtfile:
                    txtfile.write(key + "\n")


    try:
        # Search Shodan
        validMapsApiKeys = set()
        for result in api.search_cursor('https://maps.googleapis.com/maps/api/js'):
            if 'http' in result:
                if 'html' in result['http']:
                    soup = BeautifulSoup(format(result['http']), features="html.parser")
                    sources = soup.findAll('script', {"src": True})
                    for source in sources:
                        if re.search(r"^https:\/\/maps.googleapis.com\/maps\/api(.*)$", source['src']):
                            checkGoogleMapsApiKey(urlparse.parse_qs(urlparse.urlparse(source['src']).query)['key'][0])
    except Exception as e:
        print('Error: {}'.format(e))
