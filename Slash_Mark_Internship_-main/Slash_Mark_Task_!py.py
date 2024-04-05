# Define an empty list to store tasks
custom_tasks = []

# Function to display the custom to-do list
def display_custom_tasks():
    if not custom_tasks:
        print("Your custom to-do list is empty.")
    else:
        print("Custom To-Do List:")
        for i, task in enumerate(custom_tasks, start=1):
            status = "Completed" if task["is_done"] else "Not Completed"
            print(f"{i}. {task['description']} ({status})")

# Function to add a custom task to the to-do list
def add_custom_task(description):
    task = {"description": description, "is_done": False}
    custom_tasks.append(task)
    print(f"Custom task '{description}' added to your to-do list.")

# Function to mark a custom task as completed
def mark_custom_task_completed(task_number):
    if 1 <= task_number <= len(custom_tasks):
        custom_tasks[task_number - 1]["is_done"] = True
        print(f"Custom task {task_number} marked as completed.")
    else:
        print("Invalid task number. Please enter a valid task number.")

# Function to remove a custom task from the to-do list
def remove_custom_task(task_number):
    if 1 <= task_number <= len(custom_tasks):
        removed_task = custom_tasks.pop(task_number - 1)
        print(f"Custom task '{removed_task['description']}' removed from your to-do list.")
    else:
        print("Invalid task number. Please enter a valid task number.")

# Main program loop
while True:
    print("\nOptions:")
    print("1. Display custom to-do list")
    print("2. Add a custom task")
    print("3. Mark a custom task as completed")
    print("4. Remove a custom task")
    print("5. Quit")
    choice = input("Enter your choice: ")

    if choice == '1':
        display_custom_tasks()
    elif choice == '2':
        task_description = input("Enter the custom task description: ")
        add_custom_task(task_description)
    elif choice == '3':
        display_custom_tasks()
        task_number = int(input("Enter the custom task number to mark as completed: "))
        mark_custom_task_completed(task_number)
    elif choice == '4':
        display_custom_tasks()
        task_number = int(input("Enter the custom task number to remove: "))
        remove_custom_task(task_number)
    elif choice == '5':
        break
    else:
        print("Invalid choice. Please enter a valid option.")
