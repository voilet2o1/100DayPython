import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# declare the above in nested list 👇
game_img = [rock,paper,scissors]
#Write your code below this line 👇


# take input from the user
user_choice = int(input("Choose '0' for Rock '1' for Scissors '2' for paper:  \n"))

# { randomly generating user input
# user_choice = random.randint(0,2)
# print("User choose")
# }

# make sure it does does fit within the range
if(user_choice >= 3 or user_choice < 0):
    print("invalid choice")
else:
    print(game_img[user_choice])

# use random to genrate computer choice know the bound
comp_choice = random.randint(0,2)
print("computer choose")
print (game_img[comp_choice])


# imply the conditions
if(user_choice == 1 and comp_choice == 0 ):
    print("you win")
elif(user_choice == 2 and comp_choice == 1):
    print("you win")
elif(user_choice == 0 and comp_choice == 2):
    print("you win")
elif(user_choice == comp_choice):
    print("Try again")

else:
    print("you loose")