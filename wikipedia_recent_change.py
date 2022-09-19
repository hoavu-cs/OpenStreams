import json
import sketches
from sseclient import SSEClient as EventSource
from datetime import datetime
import requests
import urllib.request

class WikiEventStreamer:
    def __init__(self):
        self.mg = sketches.Misra_Gries(100)

    def stream_wiki_changes_loop(self):
        url = 'https://stream.wikimedia.org/v2/stream/recentchange'
        counter = 0
        now = datetime.now()

        for event in EventSource(url):
            if event.event == 'message':
                try:
                    change = json.loads(event.data)
                except ValueError:
                    pass
                else:

                    if change['namespace']==0 and change['type']=='edit' and \
                    change['bot']==False and change['minor']==False and \
                    change['meta']['domain'].endswith('en.wikipedia.org'):
                        self.mg.insert(change['title'])
                        counter += 1

                    if counter == 100:
                        heavy_hitters = self.mg.top_counters(100)
                        heavy_hitters["start time"] = str(now)
                        bin_url = 'https://api.jsonbin.io/v3/b/632806d65c146d63caa03e6d'
                        headers = {'Content-Type': 'application/json','X-Master-Key': '$2b$10$U1j48nqsYU/4kNWJ4cHjQeTad3SeIgiLpS1hD.vGLJ1PTLnzd3IGW'}
                        req = requests.put(bin_url, json=heavy_hitters, headers=headers)
                        counter = 0


    def begin_streaming(self):
        self.stream_wiki_changes_loop()



stream = WikiEventStreamer()
stream.begin_streaming()
