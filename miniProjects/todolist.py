# Description:

# Allow user to add, remove, and view tasks.
# Each task can be stored as a string in a list.
# Use a while loop to keep showing the menu until the user exits.
# Optional Challenge:
# Use a Task class with attributes title and status
# Allow marking tasks as completed

task_list = []

while True: 
    option = input('Pick one of these options: Add, Remove, View or Exit: ')
    if option == 'Add': 
        add_task = input("Input your task: ")
        task_list.append(add_task)
    elif option == 'Remove': 
        remove_task = input("Input your task: ")
        task_list.remove(remove_task)
    elif option == 'View':
        print(task_list)
    elif option == 'Exit': 
        break
    else: 
        print('Option incorrect, please pick again')

# Doing with Class 

# class Task:
#     def __init__(self, title):
#         self.title = title
#         self.completed = False

#     def mark_completed(self):
#         self.completed = True

#     def __str__(self):
#         status = "Done" if self.completed else "Not Done"
#         return f"[{status}] {self.title}"

# tasks = []

# while True:
#     print("\n--- To-Do List Menu ---")
#     print("1. Add Task")
#     print("2. Remove Task")
#     print("3. View Tasks")
#     print("4. Mark Task as Completed")
#     print("5. Exit")

#     choice = input("Choose an option: ")

#     if choice == "1":
#         title = input("Enter task title: ")
#         tasks.append(Task(title))
#         print(f"Task '{title}' added.")
#     elif choice == "2":
#         for i, t in enumerate(tasks, 1):
#             print(f"{i}. {t}")
#         index = int(input("Enter the number of the task to remove: "))
#         if 1 <= index <= len(tasks):
#             removed_task = tasks.pop(index - 1)
#             print(f"Task '{removed_task.title}' removed.")
#         else:
#             print("Invalid task number.")
#     elif choice == "3":
#         if not tasks:
#             print("No tasks in the list.")
#         else:
#             print("Your tasks:")
#             for i, t in enumerate(tasks, 1):
#                 print(f"{i}. {t}")
#     elif choice == "4":
#         for i, t in enumerate(tasks, 1):
#             print(f"{i}. {t}")
#         index = int(input("Enter the number of the task to mark as completed: "))
#         if 1 <= index <= len(tasks):
#             tasks[index - 1].mark_completed()
#             print(f"Task '{tasks[index - 1].title}' marked as completed.")
#         else:
#             print("Invalid task number.")
#     elif choice == "5":
#         print("Exiting the program. Goodbye!")
#         break
#     else:
#         print("Invalid option. Please try again.")
