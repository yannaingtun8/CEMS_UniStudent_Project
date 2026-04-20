import json

FB_FILE = "data/feedback.json"
with open(FB_FILE, "r") as f:
    fb = json.load(f)

print("--- Feedback & Ratings ---")
print("1. Add Feedback")
print("2. View Feedback")
sub = input("Choose: ").strip()

if sub == "1":
    eid = input("Event ID: ").strip()
    sid = input("Student ID: ").strip()
    rating = int(input("Rating (1-5): "))
    comment = input("Comment: ")

    fb.append({
        "event_id": eid,
        "student_id": sid,
        "rating": rating,
        "comment": comment
    })

    with open(FB_FILE, "w") as f:
        json.dump(fb, f, indent=4)

    print(" Feedback saved!")

elif sub == "2":
    eid = input("Event ID: ").strip()

    ratings = []
    for f in fb:
        if f["event_id"] == eid:
            ratings.append(f["rating"])

    if len(ratings) == 0:
        print("No feedback yet.")
    else:
        avg = sum(ratings) / len(ratings)
        print("Average rating:", avg)

        print("Comments:")
        for f in fb:
            if f["event_id"] == eid:
                print("-", f["student_id"], ":", f["comment"])