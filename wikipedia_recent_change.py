import json
import sketches
from sseclient import SSEClient as EventSource
from datetime import datetime
import requests
import urllib.request
import wikipediaapi
import boto3

class WikiEventStreamer:
    def __init__(self):
        self.mg_title = sketches.Misra_Gries(100)
        self.mg_topic = sketches.Misra_Gries(100)
        self.s3 = boto3.client('s3', aws_access_key_id = 'AKIARNSJLSMP7ZD5FAYT', aws_secret_access_key = "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")



    def stream_wiki_changes_loop(self):
        url = 'https://stream.wikimedia.org/v2/stream/recentchange'
        counter = 0
        start_time = datetime.now()
        wiki = wikipediaapi.Wikipedia()

        for event in EventSource(url):
            if event.event == 'message':

                # title
                try:
                    change = json.loads(event.data)
                except ValueError:
                    pass
                else:

                    if change['namespace']==0 and change['type']=='edit' and \
                    change['bot']==False and \
                    change['meta']['domain'].endswith('wikipedia.org'):

                        self.mg_title.insert(change['title'])
                        page = wiki.page(change['title'])
                        topics = list(page.categories.keys())
                        for t in topics:
                            self.mg_topic.insert(t)



                        counter += 1

                    if counter == 1000:
                        frequent_title = self.mg_title.top_counters(100)
                        frequent_topic = self.mg_topic.top_counters(100)
                        self.s3.put_object(Body=json.dumps(frequent_title), Bucket='sketch-db', Key='wiki-title-hh.json')
                        self.s3.put_object(Body=json.dumps(frequent_topic), Bucket='sketch-db', Key='wiki-topic-hh.json')
                        counter = 0


    def begin_streaming(self):
        self.stream_wiki_changes_loop()



stream = WikiEventStreamer()
stream.begin_streaming()
