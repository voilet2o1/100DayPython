print ("!! WELCOME TO THE DRAGON RIDE !!")
height = int(input("Enter your height: "))
bill = 0

if(height >= 120):
    print ("You are tall enough to ride the dragon.")
    age = int(input("What is your age: "))
    if(age <12):
        print("pay $5")
        bill = 5
    elif(age >=12 and age <18):
        print("pay $10")
        bill = 10
    else:
        print("pay $15")
        bill = 15
    photo = input("Do you want to take photo 'y' or 'n' ")
    if photo == "Y":
        bill += 5
        print(f"Your total amount will be {bill}")

else:
    print ("You are not tall enough to ride the dragon.")