import json
import csv

PART_FILE = "data/participants.json"
with open(PART_FILE, "r") as f:
    parts = json.load(f)

print("--- Attendance Tracking ---")
print("1. Mark Present/Absent")
print("2. View Summary")
print("3. Export CSV")
sub = input("Choose: ").strip()

eid = input("Event ID: ").strip()

record = None
for r in parts:
    if r["event_id"] == eid:
        record = r

if record is None:
    print("No participants for this event.")
else:
    if sub == "1":
        for p in record["participants"]:
            s = input(p["student_id"]+" "+p["name"]+" (P/A): ").upper()
            if s == "P":
                p["attendance"] = "Present"
            else:
                p["attendance"] = "Absent"

        with open(PART_FILE, "w") as f:
            json.dump(parts, f, indent=4)
        print(" Attendance saved!")

    elif sub == "2":
        total = len(record["participants"])
        present = 0
        absent = 0

        for p in record["participants"]:
            if p["attendance"] == "Present":
                present += 1
            elif p["attendance"] == "Absent":
                absent += 1

        print("Total:", total)
        print("Present:", present)
        print("Absent:", absent)

    elif sub == "3":
        filename = "attendance_" + eid + ".csv"
        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Student ID", "Name", "Attendance"])
            for p in record["participants"]:
                writer.writerow([p["student_id"], p["name"], p["attendance"]])

        print(" CSV exported:", filename)