
while True:
 print("This is CEMS MAIN MENU ")
 print("1. Event Management")
 print("2. Participant Registration")
 print("3. Search Event")
 print("4. Attendance Tracking")
 print("5. Feedback & Ratings")
 print("6. Exit")

 choice = input("Choose: ").strip()

 if choice == "1":
    import events
 elif choice == "2":
    import registration
 elif choice == "3":
    import search
 elif choice == "4":
    import attendance
 elif choice == "5":
    import feedback
 else:
    print("Bye!")