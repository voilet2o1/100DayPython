# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(",")
# 🚨 Don't change the code above 👆

chances = len(names)

choice = random.randint(0, chances-1)
#Write your code below this line 👇
person = names [choice]
print (f"{person} will pay the bill")