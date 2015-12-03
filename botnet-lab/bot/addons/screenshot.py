import json
import requests
from base64 import b64encode
import os
import autopy
import subprocess

def screenshot():
    client_id = "2ed32bb280dd0b8"
    output = ""
    try:
        if os.name != "nt":
            p = subprocess.Popen(["echo", "$DISPLAY"], stdout=subprocess.PIPE)
            output, err = p.communicate()
    except:
        return "Display not found"
    if output != " " or output != "" or os.name == "nt":
        b = autopy.bitmap.capture_screen()
        b.save("im.png")
    else:
        return "Display not found"
    headers = {"Authorization": "Client-ID 2ed32bb280dd0b8"}
    api_key = 'eb215a75b4e3b0e3604c42b98f3ab7b41656ddfb'
    url = "https://api.imgur.com/3/upload.json"
    try:
        j1 = requests.post(
            url,
            headers=headers,
            data={
                'key': api_key,
                'image': b64encode(open('im.png', 'rb').read()),
                'type': 'base64',
                'name': 'im.png',
                'title': 'screen'
            }, verify=False
        )
    except:
        return "Failed to upload."
    os.remove('im.png')
    try:
        return json.loads(j1.text)["data"]["link"]
    except:
        return "Failed to retrieve response."
