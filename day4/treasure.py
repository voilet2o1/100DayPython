# 🚨 Don't change the code below 👇
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3] 
# ☝️this is the nested list 
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# ☝️this will print the out put in strng ("2+3 = 23") so convert it into int
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
# 👇covert the value in int with specifying the positions horizontal and vertical
horizontal = int(position[0])
vertical = int(position[1])

# 👇 declare the row and column and what you want to mark the treasure
selected_row = map[vertical-1]
selected_row[horizontal-1] = "x"

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")

