
# Displays list of options to the user
def menu():
    print("""
    Menu options:
        1. Add Task
        2. View Tasks
        3. Delete Tasks
        4. Quit App
        5. Show Menu""")

# Option 2 from the menu. Displays user's to-do list.
def view_task():
    # Checks if to-do list is empty and notifies user
    if tasks == []:
        print("No tasks avalible.")
        return
    
    # Iterates through tasks and prints them
    print("Your current tasks are:")
    for i in range(len(tasks)):
        print(f"\t{i + 1}. {tasks[i]}")

# Prompts user for task to input and adds it to the to-do list
def add_task():
    task = input("Task to add: ")
    tasks.append(task)
    print(f"\"{task}\" task added!")

# Displays task list then prompts user for task to delete and removes it from the to-do list
def delete_task():
    # Display task list
    view_task()
    
    # Exits function if no task in the list
    if tasks == []:
        return
    
    try:
        # Prompts user for task to delete (accepts number values, otherwise error is printed)
        task = int(input("\nWhich task would you like to delete? Enter the associated number: "))
        
        # Deletes task from list if found
        if task <= len(tasks) and task > 0:
            print(f"Deleting \"{tasks[task - 1]}\" task...")
            tasks.remove(tasks[task - 1])
            print("Deleted!")
        else:
            print("ERROR: Task does not exist.")
    except ValueError:
        print("ERROR: Entered value is not a number.")

# Stores task list
tasks = []

# Keeps app open until user quits the app
app_open = True

# Print welcome message once when app opens and displays menu
print("""
Welcome to this simple CLI to-do list app!""")
menu()

while app_open:
    try:
        option = int(input("\nSelect an option from the menu (1-5): "))
        if option == 1:
            add_task()
        elif option == 2:
            view_task()
        elif option == 3:
            delete_task()
        elif option == 4:
            print("\nThanks for visiting! App closing now.\n")
            app_open = False
        elif option == 5:
            menu()
        else:
            print("ERROR: Option selected is invalid. Please try again.")
    except ValueError:
        print("ERROR: Entered value is not a number.")
    
    
