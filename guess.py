import random

while True:
    # Select difficulty
    number = input("Choose the difficulty\n(X = Easy, Y = Medium, Z = Hard)\nOr type a custom number: ").strip().lower()

    if number == 'x':
        limit = 10
    elif number == 'y':
        limit = 50
    elif number == 'z':
        limit = 100
    else:
        try:
            limit = int(number)
        except ValueError:
            print("Invalid input. Defaulting to Easy (10).")
            limit = 10

    # Generate target number
    target = random.randint(1, limit)

    # Ask for number of chances
    try:
        chances = int(input("\nEnter how many chances you want: ").strip())
    except ValueError:
        print("Invalid input. Defaulting to 5 chances.")
        chances = 5

    attempts = 0

    while chances > 0:
        print(f"\nYou have {chances} chances left.")

        try:
            guess = int(input("Guess the number: ").strip())
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        attempts += 1

        if guess == target:
            print("\nCorrect! Good job.")
            print(f"Number of turns used: {attempts}")
            break
        else:
            print("Wrong guess.")
            if guess > target:
                print("Your number is higher than the correct number.")
            else:
                print("Your number is lower than the correct number.")

        chances -= 1

    else:
        print(f"\nYou are out of chances. The correct number was: {target}")

    # Replay check
    replay = input("\nDo you want to play again? (y/n): ").strip().lower()
    if replay != 'y':
        print("\nGame over.")
        break