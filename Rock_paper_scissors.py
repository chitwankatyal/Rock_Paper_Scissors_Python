# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 15:26:27 2021

@author: chitwan
Rock, paper, scissors
"""
import random
list = ['Rock','Paper','Scissors']

print('Welcome to the game!')
counter = 0
stop = 5
sum_won = 0
sum_lose = 0
sum_tie = 0

while counter < stop:
    computer_input = random.choice(list)
    user_input = (input("Please enter your choice(Rock,Paper,Scissors): ")).title()
   
    if user_input == computer_input:
        print(f"Tie! Both chose {user_input}. Try again!")
        counter += 1
        sum_tie += 1
    elif user_input == 'Rock':
        if computer_input == 'Paper':
            print(f"You lose as computer chose {computer_input}.")
            counter += 1
            sum_lose += 1
        else:
            print(f"Congratulations! You won as computer chose {computer_input}")
            sum_won += 1
            counter += 1
    elif user_input == 'Paper':
          if computer_input == 'Rock':
              print(f'Congratulation! You won as computer chose {computer_input}.')
              counter += 1
              sum_won += 1
          else:
              print(f"You lose as computer chose {computer_input}.")
              sum_lose += 1
              counter += 1
    elif user_input == 'Scissors':
            if computer_input == 'Rock':
             print(f"You lose as computer chose {computer_input}.")
             counter += 1
             sum_lose += 1
            else:
              print(f'Congratulation! You won as computer chose {computer_input}.')
              sum_won += 1
              counter += 1
    else:
        print("Please check your spelling and try again.")
                           
print(f'\nYou have used all your turns.Games won:{sum_won}, Games lose:{sum_lose}, Games tie:{sum_tie}')              
                  

    
                  
                    
                    
                    
          
            
            
            
        
