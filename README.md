# Simple CLI To-Do List Application

## Project:
- Use Python to create a simple To-Do list application in the command line interface (CLI)

## Languages Used:
- Python
    - Elements Used:
        - loops, Python list, list modifications, user input, error handling, functions

## App Features
- Add tasks
- View tasks
- Delete tasks
- Quit the application

## Application Flow
- Welcome message and menu is displayed to user
- Prompt for user to enter a number associated with a menu action
    - Error prints out if input is invalid
- Menu option 1: Add task
    - Prompts user to enter a task to add
    - Adds the task to the to-do list
- Menu option 2: View tasks
    - Displays a numbered list of the user's tasks by using a for loop
    - Will also notify user if the task list is empty
- Menu option 3: Delete task
    - Calls `view_task()` function to display a numbered list of tasks
    - Prompts user to enter the number associated with the task they want to delete
    - Deletes the task if found in the list
        - Prints error message if invalid input
- Menu option 4: Quit application
    - Quits the application and prints a goodbye message
- Menu option 5: Show menu
    - Prints the menu to the user
- Using a while loop, the application will stay open until user chooses Menu option 4 to quit the application