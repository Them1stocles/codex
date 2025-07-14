import feedparser, json, re
feed='https://feeds.buzzsprout.com/2393362.rss'
entries=feedparser.parse(feed).entries
dataset=[]
for e in entries:
    title=e.title
    link=e.link
    # Extract battle name (before comma)
    name=re.split('[.,]', title)[0].strip()
    dataset.append({'name': name, 'title': title, 'episode_link': link})
print(len(dataset))
print(dataset[:5])
print(json.dumps(dataset[:20]))
