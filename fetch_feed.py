import feedparser, re, json, os
from geopy.extra.rate_limiter import RateLimiter
from geopy.geocoders import Nominatim

FEED = "https://feeds.buzzsprout.com/2393362.rss"
OUT = "battles.json"


def extract_episode_fields(entry):
    raw_title = entry.title
    title = raw_title.split('.')[0].strip()
    year_match = re.search(r'([1-9][0-9]{2,4})', raw_title)
    return {
        "battle": title.replace("The ", ""),
        "year": int(year_match.group()) if year_match else None,
        "link": entry.links[0]["href"],
    }


def geocode_rows(rows):
    geo = Nominatim(user_agent="hgb-map")
    gcode = RateLimiter(geo.geocode, min_delay_seconds=1.1)
    for r in rows:
        if "lat" in r:
            yield r
            continue
        place = gcode(r["battle"])
        if place is None:
            print("NO HIT:", r["battle"])
            continue
        r["lat"], r["lng"] = place.latitude, place.longitude
        yield r


def main():
    feed = feedparser.parse(FEED)
    items = [extract_episode_fields(e) for e in feed.entries]
    cache = {c["battle"]: c for c in json.load(open(OUT))} if os.path.exists(OUT) else {}
    merged = [cache.get(i["battle"], i) for i in items]
    full = list(geocode_rows(merged))
    open(OUT, "w").write(json.dumps(full, indent=2))
    print(f"Wrote {len(full)} records \u2192 {OUT}")


if __name__ == "__main__":
    main()
