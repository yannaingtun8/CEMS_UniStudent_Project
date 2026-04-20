import json

EVENTS_FILE = "data/events.json"
with open(EVENTS_FILE, "r") as f:
    events = json.load(f)

print("--- Search Event by Name ---")
key = input("Keyword: ").lower()

found = False
for e in events:
    if key in e["name"].lower():
        print(e["event_id"], e["name"], e["date"])
        found = True

if not found:
    print("No matching event.")