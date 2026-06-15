from packages.assistant import Assistant
from packages.joke_tool import get_joke

assistant = Assistant()
while True:
    print("\n=== Smart Assistant ===\n")
    print("1. Set Name")
    print("2. View Name")
    print("\n")
    print("3. Add Note")
    print("4. View Notes")
    print("5. Delete Note")
    print("\n")
    print("6. Add Task")
    print("7. Complete Task")
    print("8. Delete Task")
    print("9. View Tasks")
    print("\n")
    print("10. Get Joke")
    print("\n")
    print("11. View History")
    print("\n")
    print("12. Exit\n")

    try:
        choose = int(input("Choose - "))
        
        if choose == 1:
            user = input("Enter Name : ")
            assistant.set_name(user)
            print("Name Updated Successfully!!")

        elif choose ==2:
            print(f"Name - {assistant.get_name()}")

        elif choose == 3:
            note = input("Enter Note : ")
            assistant.add_note(note)
            print("Note Added Successfully!!")

        elif choose ==4:
            print("Notes :")
            print(f"{assistant.view_notes()}")

        elif choose == 5:
            try:
                note_num = int(input("Enter Note Number To Delete : "))
                assistant.delete_note(note_num)
                print("Note Deleted Successfully!!")
            except ValueError:
                print("Enter Only Numeric Value")

        elif choose ==6:
            try:
                task = input("Enter Task : ")
                assistant.add_task(task)
                print("Task Added Successfully!!")
            except ValueError:
                print("Enter Only Numeric Value")

        elif choose ==7:
            task = int(input("Enter Task Number : "))
            assistant.complete_task(task)
            print("Task Marked Completed!")

        elif choose == 8:
            try:
                task_num = int(input("Enter Task Number To Delete : "))
                assistant.delete_task(task_num)
                print("Task Deleted Successfully!!")
            except ValueError:
                print("Enter Only Numeric Value")

        elif choose == 9:
            print("-----Tasks-----")
            print(f"{assistant.view_tasks()}")

        elif choose == 10:
            print(get_joke())

        elif choose == 11:
            print(assistant.history_viewer())

        elif choose == 12:
            print(assistant.task_stats())
        elif choose == 13:
            print("GoodBye!")
            break
        else:
            print("Invalid Choice")
        
        print()
        input("Press Enter To Continue...")

    except ValueError:
        print()
        print("Enter Only Numeric Value")
        print()
        input("Press Enter To Continue...")