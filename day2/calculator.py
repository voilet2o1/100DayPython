print("!! Your bill split calculator !!")
print("Please enter the bill amount: ")
bill = float(input())
print("Please enter the number of people splitting the bill: ")
num_people = int(input())
print("The bill is: ", bill)
print("The number of people splitting the bill is: ", num_people)
print("The bill is split into ", num_people, " people.")
print("Each person will pay: ", round((bill / num_people)*1.12), " dollars.")
