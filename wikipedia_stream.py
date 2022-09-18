from misragries import MisraGries
import json
from sseclient import SSEClient as EventSource


class WikiEventStreamer:
    def __init__(self):
        self.misra_gries_titles = MisraGries(50)
        self.misra_gries_users = MisraGries(50)

    def stream_wiki_changes_loop(self):
        url = 'https://stream.wikimedia.org/v2/stream/recentchange'
        counter = 0
        for event in EventSource(url):
            if event.event == 'message':
                try:
                    change = json.loads(event.data)
                except ValueError:
                    pass
                else:
                    self.misra_gries_users.insert(change['user'])
                    self.misra_gries_titles.insert(change['title'])
                    counter += 1
                    if counter == 500:
                        counter = 0
                        self.misra_gries_users.output_heavy_hitters()

    def begin_streaming(self):
        self.stream_wiki_changes_loop()
