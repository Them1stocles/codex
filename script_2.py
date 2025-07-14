import feedparser, json
d=feedparser.parse('https://feeds.buzzsprout.com/2393362.rss')
print(len(d.entries))
print([e.title for e in d.entries[:5]])
