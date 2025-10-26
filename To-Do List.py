to_do = []

while True:
    print("\nTo-Do List")
    print("1. Add a task")
    print("2. View a task")
    print("3. Delete a task")
    print("4. Quit")

    user_decision = input('What do you want to do (1-4)?: ')

    if user_decision == "1":
        add_task = str(input('What task do you want to add? '))
        if add_task:
            to_do.append(add_task)
            print("Task added")
        else:
            print("Task was not added")

    elif user_decision == "2":
        if not to_do:
            print("No tasks in the list")
        else:
            print("\nThis is all your tasks: ", to_do)

    elif user_decision == "3":
        if not to_do:
            print("No tasks to delete")
        else:
            print("\nYour tasks: ", to_do)

        delete_task = str(input('Which task do you want to delete? '))
        if delete_task in to_do:
            to_do.remove(delete_task)
            print("Task deleted")
        else:
            print("Task was not deleted")

    elif user_decision == "4":
        break

    else:
        print("Invalid input. Choose number from 1-4")



