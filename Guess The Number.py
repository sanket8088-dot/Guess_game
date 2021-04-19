n=20
no_of_guess=1
print("the chance of guess are 9")
while (no_of_guess<=9):
    guess=int(input("Guess your no\n"))
    if guess<20:
        print("the number you enter is greter then  guess no:\n")
    elif guess>20:
        print("the number you enter is less then  guess no:\n")
    else:
        print("you win \n")
        print(no_of_guess,"took to finish")
        break
    print(9-no_of_guess,"no of guess left")
    no_of_guess=no_of_guess+1
if(no_of_guess>9):
  print("game over")

"""

# no of guesses 9
# print no of guesses left
# No of guesses he took to finish
# game over

n = 18
number_of_guesses = 1
print("Number of guesses is limited to only 9 times: ")
while (number_of_guesses <= 9):
    guess_number = int(input("Guess the number :\n"))
    if guess_number < 18:
        print("you enter less number please input greater number.\n")
    elif guess_number > 18:
        print("you enter greater number please input smaller number.\n ")
    else:
        print("you won\n")
        print(number_of_guesses, "no.of guesses he took to finish.")
        break
    print(9 - number_of_guesses, "no. of guesses left")
    number_of_guesses = number_of_guesses + 1

if (number_of_guesses > 9):
    print("Game Over")

"""