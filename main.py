# This is a Rock, Paper, Scissor Game

import random

while True:
 print("Welcome to the Rock, Paper, Scissor game!")
 possible_choice = ['Rock', 'Paper', 'Scissor']
 user_input = input("User make your choice: ")
 computer_input = random.choice(possible_choice)
 print("Computer selected:", computer_input)

 P1 = user_input
 P2 = computer_input


 user_score = 0
 computer_score = 0
 if P1 == 'Rock' and P2 == 'Paper':
          print('Paper defeats Rock')
          print('The Winner is: Player 2!')
          computer_score += 1
          print('Computer Score:', computer_score)
          print('User Score:', user_score)

 elif P1 == 'Paper' and P2 == 'Rock':
          print('Paper defeats Rock')
          print('The Winner is: Player 1!')
          user_score += 1
          print('User Score:', user_score)
          print('Computer Score:', computer_score)

 elif P1 == 'Rock' and P2 == 'Scissor':
          print('Rock defeats Scissor')
          print('The Winner is: Player 1!')
          user_score += 1
          print('User Score:', user_score)
          print('Computer Score:', computer_score)

 elif P1 == 'Scissor' and P2 == 'Rock':
          print('Rock defeats Scissor')
          print("The Winner is: Player 2!")
          computer_score += 1
          print('Computer Score:', computer_score)
          print('User Score:', user_score)

 elif P1 == 'Paper' and P2 == 'Scissor':
          print('Scissor defeats Paper')
          print("The Winner is: Player 2!")
          computer_score += 1
          print('Computer Score:', computer_score)
          print('User Score:', user_score)

 elif P1 == 'Scissor' and P2 == 'Paper':
          print('Scissor defeats Paper')
          print("The Winner is: Player 1!")
          user_score += 1
          print('User Score:', user_score)
          print('Computer Score:', computer_score)

 elif (P1 and P2 == 'Paper') or (P1 and P2 == 'Rock') or (P1 and P2 == 'Scissor'):
          print("Its a Tie!")
          user_score += 1
          computer_score +=1
          print('User Score:', user_score)
          print('Computer Score:', computer_score)


 play_again = input("Do you want to play again? (y/n)")
 if play_again.lower() != "y":
  break

"""
#### Driver code

if __name__ == '__main__':
            


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
"""