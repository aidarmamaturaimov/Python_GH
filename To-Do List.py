to_do = []


user_decision = int(input('What do you want to do? '))

if user_decision == 1:
    add_task = str(input('What task do you want to add? '))
    to_do.append(add_task)

elif user_decision == 2:
    print("This is all your tasks!", to_do)

elif user_decision == 3:
    delete_task = str(input('What task do you want to delete? '))
    to_do.remove(delete_task)



print(to_do)
