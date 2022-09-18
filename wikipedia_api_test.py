#!/usr/bin/python3

"""
    get_recent_changes.py

    MediaWiki API Demos
    Demo of `RecentChanges` module: Get the three most recent changes with
    sizes and flags

    MIT License
"""

import requests
import time
import sketches
from datetime import datetime




def get_edits(num_of_edits=4):


    S = requests.Session()

    timestamp = datetime.now()
    timestamp = timestamp.isoformat()

    URL = "https://en.wikipedia.org/w/api.php"
    PARAMS = {
        "rcstart": str(timestamp),
        "format": "json",
        "rcprop": "title|ids|sizes|flags|timestamp|comment|",
        "list": "recentchanges",
        "action": "query",
        "rclimit": str(num_of_edits),
        "rcshow": "!minor|!anon|!bot",
        "rcnamespace": "0",
        "rctype": "edit",
        "rcdir": "newer"
        }
    time.sleep(1)

    R = S.get(url=URL, params=PARAMS)
    data = R.json()

    recent_changes = data['query']['recentchanges']
    return recent_changes


rc = get_edits(4)
for item in rc:
    print(item)
