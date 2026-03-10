import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
rock
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
paper
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
scissors
'''

game_image = [rock,paper,scissors]
ngacak = random.choice(game_image)

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for paper or 2 for scissors.\n"))
if user_choice <0 or user_choice > 2:
    print("Invalid Number")
if user_choice == 0 :
    print(rock)
    if ngacak == rock:
        print(ngacak)
        print("It's draw")
    elif ngacak == paper:
        print(ngacak)
        print("You lose")
    else:
        print("You win !")
elif user_choice == 1:
    print(paper)
    if ngacak == rock:
        print(ngacak)
        print("You win!")
    elif ngacak == paper:
        print(ngacak)
        print("It's draw")
    else:
        print(ngacak)
        print("You lose")
elif user_choice == 2:
    print(scissors)
    if ngacak == rock:
        print(ngacak)
        print("You lose")
    elif ngacak == paper:
        print(ngacak)
        print("You win!")
    else:
        print(ngacak)
        print("It's draw")
