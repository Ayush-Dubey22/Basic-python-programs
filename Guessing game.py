right_number = 8
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input("Guess the right number: "))
    guess_count += 1
    if guess == right_number:
        print("You Win!")
        break
else:
        print("Sorry you Lost")