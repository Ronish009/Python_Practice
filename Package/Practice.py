task = {}

def display_menu():
    print("\nPersonal Task Manager")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Save Tasks to File")
    print("5. Load Tasks from File")
    print("6. Exit")


def add_task():
    t = input("Enter the task: ")
    priority = input("Enter priority (HIGH/LOW/MEDIUM): ")
    task[t] = priority
    print("Task added successfully")


def view_tasks():
    if not task:
        print("No tasks available")
    else:
        for i, (k, v) in enumerate(task.items(), start=1):
            print(f"{i}. {k} - {v}")


def remove_task():
    t = input("Enter the task to be deleted: ")
    if t in task:
        del task[t]
        print("Task deleted successfully")
    else:
        print("No task found")


def save_tasks():
    with open("task.txt", "w") as file:
        for t, p in task.items():
            file.write(f"{t},{p}\n")
    print("Task saved to file")


def load_tasks():
    try:
        with open("task.txt", "r") as file:
            task.clear()
            for line in file:
                t, p = line.strip().split(",")
                task[t] = p
        print("Task loaded from file")
    except FileNotFoundError:
        print("No saved file found.")


while True:
    display_menu()
    try:
        choice = input("Enter your choice (1-6): ")
    except EOFError:
        print("No input detected. Exiting program.")
        break

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        save_tasks()
    elif choice == "5":
        load_tasks()
    elif choice == "6":
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")