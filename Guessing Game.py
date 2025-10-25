import random

secret_num = random.randint(1, 100)

num_attempts = 5

print("I guessed a number X between 1 and 100")
print("You have {} attempts remaining".format(num_attempts))

for i in range(num_attempts):
    guess = int(input("Attempt {}: ".format(i+1)))


    if guess < secret_num:
        print("Too low!")

    elif guess > secret_num:
        print("Too high!")

    else:
        print("Correct! You guessed the number!")
        break

else:
    print("Thank you for a game. Guessed number was {}".format(secret_num))
