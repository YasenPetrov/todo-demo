import json
import os

# File to store tasks
tasks_file = 'tasks.json'


# Load existing tasks
def load_tasks():
    if os.path.exists(tasks_file):
        with open(tasks_file, 'r') as file:
            return json.load(file)
    return []


# Save tasks to file
def save_tasks(tasks):
    with open(tasks_file, 'w') as file:
        json.dump(tasks, file, indent=4)


# Add a new task
def add_task(tasks, task):
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task '{task}' added!")


# View all tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        print("Your tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")


# Delete a task
def delete_task(tasks, task_number):
    if 0 < task_number <= len(tasks):
        task = tasks.pop(task_number - 1)
        save_tasks(tasks)
        print(f"Task '{task}' deleted!")
    else:
        print("Invalid task number!")


# Main program loop
def main():
    tasks = load_tasks()
    while True:
        print("\nOptions:")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Delete a task")
        print("4. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            task = input("Enter the task: ")
            add_task(tasks, task)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            task_number = int(input("Enter the task number to delete: "))
            delete_task(tasks, int(choice))
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
