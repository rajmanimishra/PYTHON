import random

jackPot = random.randint(1, 100)
guess_number = int(input("Enter the number (1-100): "))
attempts = 1

while guess_number != jackPot:
    if guess_number > jackPot:
        print("Wrong! Number is too high.")
    else:
        print("Wrong! Number is too low.")

    attempts += 1
    guess_number = int(input("Enter the number: "))

print(
    f"Congratulations! You correctly guessed the number in {attempts} attempts."
)