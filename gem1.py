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
papper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
papper
'''
sciccors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
sciccors
'''

list = [rock,papper,sciccors]
ngacak = random.choice(list)

user_choise = int(input("What do you choose? Type 0 for Rock, 1 for Papper or 2 for Sciccors.\n"))
if user_choise == 0 :
    print(rock)
    if ngacak == rock:
        print(ngacak)
        print("It's draw")
    elif ngacak == papper:
        print(ngacak)
        print("You lose")
    else:
        print("You win !")
elif user_choise == 1:
    print(papper)
    if ngacak == rock:
        print(ngacak)
        print("You win!")
    elif ngacak == papper:
        print(ngacak)
        print("It's draw")
    else:
        print(ngacak)
        print("You lose")
elif user_choise == 2:
    print(sciccors)
    if ngacak == rock:
        print(ngacak)
        print("You lose")
    elif ngacak == papper:
        print(ngacak)
        print("You win!")
    else:
        print(ngacak)
        print("It's draw")

# print(ngacak)