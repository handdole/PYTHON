import random

li = []

a = 0

while len(li) <= 6:
    num = random.randint(1, 45)
    print(num)
    if num not in li:
        li.append(num)

print(li)
