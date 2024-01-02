# Initialize an empty to-do list
todo_list = []

# Function to display the current to-do list
def display_todo_list():
    if not todo_list:
        print("Your to-do list is empty.")
    else:
        print("Your To-Do List:")
        for idx, task in enumerate(todo_list, start=1):
            print(f"{idx}. [{task['status']}] {task['name']}")

# Function to add a new task to the to-do list
def add_task():
    new_task_name = input("Enter the task's name: ")
    todo_list.append({'name': new_task_name, 'status': 'Incomplete'})
    print(f"Task '{new_task_name}' added to your to-do list.")

# Function to mark a task as completed
def mark_completed():
    display_todo_list()
    if not todo_list:
        return

    task_num = int(input("Enter the task number to mark as completed: "))
    if 1 <= task_num <= len(todo_list):
        todo_list[task_num - 1]['status'] = 'Completed'
        print(f"Task {task_num} marked as completed.")
    else:
        print("Invalid task number.")

# Function to remove a task from the to-do list
def remove_task():
    display_todo_list()
    if not todo_list:
        return

    task_num = int(input("Enter the task number to remove: "))
    if 1 <= task_num <= len(todo_list):
        removed_task = todo_list.pop(task_num - 1)
        print(f"Task '{removed_task['name']}' removed from your to-do list.")
    else:
        print("Invalid task number.")

# Main function to run the To-Do List application
def main():
    while True:
        print("\nSelect an option:")
        print("1. Display To-Do List")
        print("2. Add a Task")
        print("3. Mark a Task as Completed")
        print("4. Remove a Task")
        print("5. Quit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            display_todo_list()
        elif choice == '2':
            add_task()
        elif choice == '3':
            mark_completed()
        elif choice == '4':
            remove_task()
        elif choice == '5':
            print("Exiting the To-Do List application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
