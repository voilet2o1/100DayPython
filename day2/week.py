# Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.

age = int(input("Enter your current age: "))

year = int(90 - age)
days = int(year *365)
weeks =int( year *52)
months=int(year * 12)

print(f"You have {days} days, {weeks} weeks, {months} months left.")