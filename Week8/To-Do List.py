import os

to_do = []

if os.path.exists("tasks.txt"):
    with open("tasks.txt", "r") as file:
        for line in file:
            task = line.strip()
            if task:
                to_do.append(task)
else:
    pass

while True:
    print("\nTo-Do List")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Delete a task")
    print("4. Quit")

    user_decision = input('What do you want to do (1-4)?: ')

    # ADD TASK
    if user_decision == "1":
        add_task = input('What task do you want to add? ')
        if add_task:
            to_do.append(add_task)
            with open("tasks.txt", "a") as file:
                file.write(add_task + "\n")
            print("Task added")
        else:
            print("Task was not added")

    # VIEW TASKS
    elif user_decision == "2":
        if not to_do:
            print("No tasks in the list")
        else:
            print("\nYour tasks:")
            for task in to_do:
                print("-", task)

    # DELETE TASK
    elif user_decision == "3":
        if not to_do:
            print("No tasks to delete")
        else:
            print("\nYour tasks:")
            for task in to_do:
                print("-", task)

        delete_task = input('Which task do you want to delete? ')
        if delete_task in to_do:
            to_do.remove(delete_task)
            with open("tasks.txt", "w") as file:
                for task in to_do:
                    file.write(task + "\n")
            print("Task deleted")

        else:
            print("Task not found")

    # QUIT
    elif user_decision == "4":
        break

    else:
        print("Invalid input. Choose number from 1-4")
