import random

magic_number = random.randrange(11)
count = 0
guess = -1

#loops until the guess matches the magic number
while True:
    count += 1
    guess = int(input("Guess the magic number: "))

    if guess == magic_number:
        break
    else:
        if guess > magic_number:
            print("Try guessing lower")
        else:
            print("Try guessing higher")
        

if count == 1:
    print("Congrats! You got it on the first try!")
else:
    print("Congrats! It only took you " + str(count) + " tries!")

print("The magic number was " + str(magic_number))