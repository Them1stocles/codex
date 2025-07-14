import feedparser, json, re
entries=feedparser.parse('https://feeds.buzzsprout.com/2393362.rss').entries
dataset=[]
for e in entries:
    title=e.get('title','')
    link=e.links[0].href if e.links else ''
    name=re.split('[.,]', title)[0].strip()
    dataset.append({'title': title, 'link': link})
print(len(dataset))
print(dataset[:10])
