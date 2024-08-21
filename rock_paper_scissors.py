import random
#print multiline instructions
print('Winning rules of the game Rock Paper Scissors are :\n'
      + "Rock vs Paper -> Paper Wins \n"
      + "Rock vs Scissors -> Rock Wins \n"
      + "Paper vs Scissors -> Scissors Wins \n")

while True:
    print("Enter your choice \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n")

    choice = int(input("Enter your choice :"))

    while choice > 3 or choice <1:
        choice = int(input('Enter a valid choice please '))

    if choice == 1:
        choice_name ='Rock'
    elif choice == 2:
        choice_name = 'Paper'
    else:
        choice_name = 'Scissors'

    print('User choice is \n', choice_name)
    print('Now its computer turn...')


    comp_choice = random.randint(1, 3)

    while comp_choice == choice:
        comp_choice = random.randint(1, 3)
    
    #initialize value of comp_choice_name
    if comp_choice == 1:
        comp_choice_name = 'Rock'
    elif comp_choice == 2:
        comp_choice_name = 'Paper'
    else:
        comp_choice_name = 'Scissors'
    print('Computer choice is \n', comp_choice_name)
    print(choice_name, 'Vs', comp_choice_name)

    #check of a draw
    if choice == comp_choice:
        print('Its a draw', end="")
        result = 'DRAW'
    #condition for winning
    if(choice == 1 and comp_choice ==2):
        print('paper wins =>', end="")
        result='Paper'
    elif (choice == 2 and comp_choice == 1):
        print('paper wins =>', end="")
        reslur='Paper'

    if(choice == 1 and comp_choice == 3):
        print('Rock wins =>\n', end="")
        result='Rock'
    elif(choice == 3 and comp_choice == 1):
        print('Rock wins =>\n', end="")
        reult='Rock'

    if(choice == 2 and comp_choice == 3):
        print('Scissors wins =>', end="")
        result='Scissors'
    elif(choice == 3 and comp_choice == 2):
        print('Scissors wins =>', end="")
        result='Scissors'

    #printting either user or computer wins or draw
    if result == 'DRAW':
        print("<== Its a tie ==>")
    if result == choice_name:
        print("<== User wins ==>")
    else:
        print("<== Computer wins ==>")
    print("Do you want to play again? (Y?N)")
    # if user input n or N then condition is True
    ans = input().lower()
    if ans == 'n':
        break


#Code Explanation:

#The code starts by printing a message that states the rules of the game.
#The first line in the code prints “Rock vs paper->paper wins.”
#This is because if you have a rock, and you play against someone who has a piece of paper, the rock will beat the paper.
#The next line in the code prints “Rock vs scissor->Rock wins.”
#This is because if you have a rock, and you play against someone who has a scissors, the rock will beat the scissors.
#The last line in the code prints “paper vs scissor->scissor wins.”
#This is because if you have a piece of paper, and you play against someone who has a scissors, then the piece of paper will beat the scissors.
#The code will print the following output: Winning Rules of the Rock paper scissor game as follows: Rock vs paper->paper wins Rock vs scissor->Rock wins paper vs scissor->scissor wins
#The code starts by asking the user for a choice.
#The code then checks to see if the input is 1, 2, or 3.
#If it is not one of those values, the code sets the choice_name variable to ‘Rock’ if choice == 1, ‘paper’ if choice == 2, and ‘scissor’ if choice == 3.
#The next part of the code asks the user for their computer turn.
#The code uses a random number generator to choose between 1, 2, and 3.
#This value is stored in comp_choice_name.
#Next, the code loops until comp_choice equals choice.
#In each loop iteration, comp_choice will be randomly chosen from 1-3 and stored in comp_choice_name.
#Once comp_choice equals choice, this means that the computer has chosen rock as its turn!
#Finally, it prints out both choices so that everyone can see what happened (user choice is: Rock V/s paper; Computer choice is: Rock V/s scissor).
#The code will ask the user for a choice between rock, paper and scissors.
#Once the user enters their choice, the code will randomly choose one of those options as the computer’s turn.
#The code then prints out the chosen option and the user’s choice.
#Finally, it loops back to ask for another choice from the user.
