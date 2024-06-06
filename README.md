# To-Do List Application

This is a simple command-line To-Do List application written in Python. It allows users to add, view, and delete tasks. The tasks are stored in a JSON file, so they persist between runs of the application.

## Features

- Add tasks to your to-do list
- View all tasks
- Delete tasks from the list
- Tasks are saved in a JSON file for persistence

## Requirements

- Python 3.x

## Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your-username/todo-list-app.git
   cd todo-list-app
   ```

2. **Run the application**

    ```bash
    python todo_list.py
    ```

## Usage

Once you run the script, you will see the following options:



- **Add a task:** Enter `1` and type the task you want to add.
- **View tasks:** Enter `2` to view all the tasks in your to-do list.
- **Delete a task:** Enter `3` and specify the task number you want to delete.
- **Exit:** Enter `4` to exit the application.

## Example

```bash
Welcome to the Python To-Do List Application!

Options:
1. Add a task
2. View tasks
3. Delete a task
4. Exit
Enter your choice: 1
Enter the task: Buy groceries
Task 'Buy groceries' added!

Options:
1. Add a task
2. View tasks
3. Delete a task
4. Exit
Enter your choice: 2
Your tasks:
1. Buy groceries

Options:
1. Add a task
2. View tasks
3. Delete a task
4. Exit
Enter your choice: 3
Enter the task number to delete: 1
Task 'Buy groceries' deleted!

Options:
1. Add a task
2. View tasks
3. Delete a task
4. Exit
Enter your choice: 4
Goodbye!