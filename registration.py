import json

EVENTS_FILE = "data/events.json"
PART_FILE = "data/participants.json"

with open(EVENTS_FILE, "r") as f:
    events = json.load(f)

with open(PART_FILE, "r") as f:
    parts = json.load(f)

print("--- Registration ---")
eid = input("Event ID: ").strip()

event_found = None
for e in events:
    if e["event_id"] == eid:
        event_found = e

if event_found is None:
    print("Event not found!")
else:
    sid = input("Student ID: ").strip()
    name = input("Student Name: ").strip()

    record = None
    for r in parts:
        if r["event_id"] == eid:
            record = r

    if record is None:
        record = {"event_id": eid, "participants": []}
        parts.append(record)

    dup = False
    for p in record["participants"]:
        if p["student_id"] == sid:
            dup = True

    if dup:
        print("Duplicate student!")
    elif len(record["participants"]) >= event_found["capacity"]:
        print("Event full!")
    else:
        record["participants"].append({
            "student_id": sid,
            "name": name,
            "attendance": ""
        })
        with open(PART_FILE, "w") as f:
            json.dump(parts, f, indent=4)
        print(" Registered!")