# Guess the number n=18
# number of guesses=9
# Print number of guesses left
# NUmber of guesses he took.
# Game over.

n = 18
inp=int(input("Guess the number: "))
i=0
print("\nYou have 8 guesses left.")
while(i<=9):
  if inp>18:
    inp=int(input("Decrease your guess and input another guess: "))
    i=i+1
    if i<9:
        print("\nYou have ", 9-(i+1), " guesses left.")
  elif inp<18:
    inp=int(input("Increase your guess and input another guess: "))
    i=i+1
    if i<9:
        print("\nYou have ", 9-(i+1), " guesses left.")
  elif inp==18:
    print("\nCongrats! You have guessed it right.")
    print("Number of guesses he took to finish = ", i)
    break


if(i>9):
    print("Game Over! You have used all your guesses.")


