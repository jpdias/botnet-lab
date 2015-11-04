import json
import requests
import pyscreenshot as ImageGrab
from base64 import b64encode
import os

def screenshot():
    client_id = "2ed32bb280dd0b8"
    im = ImageGrab.grab_to_file('im.png')

    headers = {"Authorization": "Client-ID 2ed32bb280dd0b8"}
    api_key = 'eb215a75b4e3b0e3604c42b98f3ab7b41656ddfb'
    url = "https://api.imgur.com/3/upload.json"
    j1 = requests.post(
        url,
        headers=headers,
        data={
            'key': api_key,
            'image': b64encode(open('im.png', 'rb').read()),
            'type': 'base64',
            'name': 'im.png',
            'title': 'screen'
        }
    )
    os.remove('im.png')
    return json.loads(j1.text)["data"]["link"]
