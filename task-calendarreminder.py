reminders = {}

def add_reminder():
    date = input("Enter the date (DD-MM-YYYY): ")
    time = input("Enter the time (HH:MM): ")
    reminder = input("Enter your reminder: ")
    
    reminder_datetime = f"{date} {time}"
    reminders[reminder_datetime] = reminder
    print("Reminder added successfully!")

def view_reminders():
    if not reminders:
        print("No reminders found.")
    else:
        print("Your reminders:")
        for datetime, reminder in reminders.items():
            print(f"{datetime}: {reminder}")

def delete_reminder():
    if not reminders:
        print("No reminders found to delete.")
    else:
        datetime_to_delete = input("Enter the date and time (DD-MM-YYYY HH:MM) of the reminder you want to delete: ")
        if datetime_to_delete in reminders:
            del reminders[datetime_to_delete]
            print("Reminder deleted successfully!")
        else:
            print("Reminder not found.")

while True:
    print("Choose an action:")
    print("1 - Add reminder")
    print("2 - View reminders")
    print("3 - Delete reminder")
    print("4 - Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        add_reminder()
    elif choice == "2":
        view_reminders()
    elif choice == "3":
        delete_reminder()
    elif choice == "4":
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please choose a valid option (1, 2, 3, or 4).")
