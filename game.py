import time
import random
import json
import pathlib

import requests

language = (NotImplemented)

image_url = "https://cdn.discordapp.com/attachments/912447431466188840/912466380442468382/game.py"
  
# URL of the image to be downloaded is defined as image_url
r = requests.get(image_url) # create HTTP response object
  
# send a HTTP request to the server and save
# the HTTP response in a response object called r
with open("game.py",'wb') as f:
  
    f.write(r.content)

with open('config.json') as config3:
    config = json.load(config3)

    if config['language'] == "english":
        language = "locale-en.json"
    if config['language'] == "spanish":
        language = "locale-es.json"


version = config['version']


with open(language) as f:
    data = json.load(f)
 
print(data['welcome'])
print(data['versiontxt'], ":", version)