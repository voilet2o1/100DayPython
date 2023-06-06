# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name = name1+name2
low_name = name.lower()

t = low_name.count("t")
r = low_name.count("r")
u = low_name.count("u")
e = low_name.count("e")

true = t+r+u+e 

l = low_name.count("l")
o = low_name.count("o")
v = low_name.count("v")
e = low_name.count("e")

love = l+o+v+e 

loveCal = int(str(true)+str(love))

if (loveCal < 10) or (loveCal > 90):
    print(f"Your score is {loveCal}, you go together like coke and mentos.")
elif (loveCal >= 40) and (loveCal <= 50):
    print(f"Your score is {loveCal}, you are alright together.")
else:
    print(f"Your score is {loveCal}")



