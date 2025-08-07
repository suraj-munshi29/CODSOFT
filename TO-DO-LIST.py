todo_list =[]
completed = []

def show_menu ():
  print("\n ----- To Do List Menu -----")
  print("1. Add Task ")
  print("2. View Task")
  print("3. Mark task as completed")
  print("4. Update Task")
  print("5. Delete Task")
  print("6. Exit")

def add_task ():
  task = input("Enter task: ")
  todo_list.append(task)
  completed.append(False)
  print("Task Added")

def view_task ():
  if not todo_list :
    print("No task added")
    return
  for i,t in enumerate(todo_list , start=1):
   status = "COMPLETED" if completed[i-1] else "NOT COMPLETED"
   print(f"{i}. [{status}] {t}")

def mark_completed ():
  view_task()
  task_index = int(input("Enter task number to mark as done: "))
  if 1 <= task_index <= len(todo_list):
    completed[task_index-1] = True
    print("Task marked as done")
  else:
    print("Invalid task number")

def update_task():
  view_task()
  task_index = int(input("Enter task number to update: "))
  if 1 <= task_index <= len(todo_list):
    new_task = input("Enter new task: ")
    todo_list[task_index-1] = new_task
    print(" Your task is updated")
  else:
    print("You entered invalid task number")

def delete_task ():
  view_task()
  task_index = int(input("Enter task number to delete: "))
  if 1 <= task_index <= len(todo_list):
    del todo_list[task_index-1]
    del completed[task_index-1]
    print("Task deleted")

while True:
  show_menu()
  choice = input("Enter your choice: ")
  if choice == "1":
    add_task()
  elif choice == "2":
    view_task()
  elif choice == "3":
    mark_completed()
  elif choice == "4":
    update_task()
  elif choice == "5":
    delete_task()
  elif choice == "6":
    print("Exit     THANK YOU ")
    break
  else:
    print("Invalid choice. Please try again.")
