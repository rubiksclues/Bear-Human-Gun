# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 15:43:47 2021

@author: Courtney
"""
#import random and math functions
import random
import math


#gets user choice/controls user input so lower and uppercase values are accepted the same/ creates error message if invalid choice is made
def get_user_choice(user_input):
    user_input = user_input.lower()
    if (user_input == 'bear') or (user_input == 'human') or (user_input == 'gun'): 
        return user_input
    else:
        return 'Please enter valid option'

#get computer choice, math floor turns this into a whole number
def get_computer_choice():
  random_number = math.floor(random.uniform(0,3))
  if random_number == 0:
    return "bear"
  if random_number == 1:
    return "human"
  if random_number == 2:
    return "gun"

#function determines winner of game
def determine_winner(user_input, computer_choice):
  #tie
  if user_input == computer_choice:
    return "It is a tie!"
  #user either wins with bear, or loses to gun  
  if user_input == "bear":
    if computer_choice == "gun":
      return "You have been shot by a gun!"
    else:
      return "You have mauled a human!"
  #user either defeats gun or loses to bear    
  if user_input == "human":
    if computer_choice == "bear":
      return "You have been mauled by a bear!"
    else:
      return "You have disarmed the computers gun!"
  #user either shoots bear or is disarmed
  if user_input == "gun":
    if computer_choice == "human":
      return "Your gun has been disarmed by a human!"
    else:
      return "You have shot a bear!"

#function begins game
def play_game():
  prompt_user_choice = input("Please choose either bear, gun, or human: ")
  user_choice = get_user_choice(prompt_user_choice)
  computer_choice = get_computer_choice()
  print("Your choice is", user_choice)
  print("Computers choice was", computer_choice)
  print(determine_winner(user_choice, computer_choice))
  play_again = input("Would you like to play again? y/n: ")
  if play_again == "y":
      play_game()
  if play_again == "n":
      print("Goodbye,Thanks for playing!")
 
         
play_game()

    