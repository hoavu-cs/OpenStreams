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



def get_edits(num_of_edits):

    S = requests.Session()


    URL = "https://en.wikipedia.org/w/api.php"
    PARAMS = {
        "format": "json",
        "rcprop": "title|ids|sizes|flags|timestamp",
        "list": "recentchanges",
        "action": "query",
        "rclimit": str(num_of_edits),
        "rcshow": "!minor|!anon|!bot",
        "rcnamespace": "0",
        "rctype": "edit",
        "rcdir": "newer"
        }

    R = S.get(url=URL, params=PARAMS)
    data = R.json()
    recent_changes = data['query']['recentchanges']
    return recent_changes


# remove any article in X with revision id
# less than or equal to max revision id in Y
def remove_duplicate_edits(X, Y):

    max_X_revid = 0
    max_Y_revid = 0

    for item in Y:
        if max_Y_revid < int(item["revid"]):
            max_Y_revid = int(item["revid"])

    X_copy = []

    for item in X:
        if int(item["revid"]) > max_Y_revid:
            X_copy.append(item)

    return X_copy


def frequently_edited_articles(num_counters = 100, time_window = 5, delay = 5, num_buckets_to_report = 10):

    timeout = time.time() + 60*time_window
    mg = sketches.Misra_Gries(num_counters)
    cur = time.localtime()
    old_rc = {}

    while time.time():
        if time.time() > timeout:
            break

        rc = get_edits(num_of_edits=100)
        rc = remove_duplicate_edits(rc, old_rc)

        print(f"Frequently edited articles since {cur.tm_hour}:{cur.tm_min}")

        for item in rc:
            mg.insert(item["title"])

        top_buckets = mg.top_counters(num_buckets_to_report)

        for y in top_buckets:
            print(f"Article: {y}, (est: {top_buckets[y]})")

        time.sleep(delay)
        old_rc = rc

        print("-------------------------------------------")


frequently_edited_articles(num_counters=200, time_window=30, delay=10, num_buckets_to_report = 5)
