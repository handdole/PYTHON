import random

jumsu = []

random.seed(3)
for x in range(0,10001):
    jumsu.append(random.randint(1,1000))

print(jumsu)

conut = jumsu.count(343)
print(conut)


count2 = 0
for x in jumsu:
    if x == 345:
        count2 = count2 + 1
print(count2)

print(jumsu.index((555)))

for x in range(0,len(jumsu)):
    if jumsu[x] == 555 :
        print('위치는:',x)