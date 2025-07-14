import feedparser, json, textwrap, requests, re, unicodedata, os, sys, datetime, math, itertools
feed_url='https://feeds.buzzsprout.com/2393362.rss'
d=feedparser.parse(feed_url)
print(len(d.entries))
items=[{'title':e.title, 'link':e.link} for e in d.entries]
print(items[:10])
