import json
EVENTS_FILE = "data/events.json"


with open(EVENTS_FILE, "r") as f:
    events = json.load(f)

print(" Event Management ")
print("1. Add Event")
print("2. List Events")
sub = input("Choose: ").strip()

if sub == "1":
    eid = input("Event ID: ").strip()
    name = input("Event Name: ").strip()
    date = input("Date (YYYY-MM-DD): ").strip()
    time = input("Time (HH:MM): ").strip()
    cap = int(input("Capacity: "))

    exists = False
    for e in events:
        if e["event_id"] == eid:
            exists = True

    if exists:
        print("Event already exists!")
    else:
        events.append({
            "event_id": eid,
            "name": name,
            "date": date,
            "time": time,
            "capacity": cap
        })
        with open(EVENTS_FILE, "w") as f:
            json.dump(events, f, indent=4)
        print(" Event added!")

elif sub == "2":
    if len(events) == 0:
        print("No events yet.")
    else:
        for e in events:
            print(e["event_id"], e["name"], e["date"], e["time"], "Cap:", e["capacity"])