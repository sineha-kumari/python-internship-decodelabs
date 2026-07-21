# Project 1: To-Do List
# DecodeLabs Python Internship

my_tasks = []

def add_task(task):
    my_tasks.append(task)
    print(f"Task added: {task}")

def view_tasks():
    if len(my_tasks) == 0:
        print("No tasks yet.")
    else:
        print("\n--- Your To-Do List ---")
        for index, task in enumerate(my_tasks):
            print(f"{index + 1}. {task}")
        print("------------------------\n")

def main():
    while True:
        print("\n1. Add Task")
        print("2. View Tasks")
        print("3. Exit")
        choice = input("Choose an option (1/2/3): ")

        if choice == "1":
            task = input("Enter a new task: ")
            add_task(task)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            print("Exiting program. Bye!")
            break
        else:
            print("Invalid option, try again.")

if __name__ == "__main__":
    main()