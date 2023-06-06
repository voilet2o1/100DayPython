# even
total = 0
for number in range(2,101,2):
    total += number
print(total)

# another way
total2 = 0
for number in range(1,101):
    if number % 2 == 0:
        total2 += number
print(total2)

# odd
total1 = 0
for number in range(1,101,2):
    total1 += number
print(total1)

# another way
total3 = 0
for number in range(1,101):
    if number % 2 == 1:
        total3 += number
print(total3)