list = [100,200,300,400,500,600,700,800,900]

'''
for 문을 사용하세요.
1. 전체목록을 프린트
2. 홀수번째 있는 요소들을 프린트
3. 홀수번재 있는 요소들을 다 더해서 프린트
4. 짝수번째 있는 요소들을 프린트


for 문을 이용해서 풀어보세요
1. 1부터 1000까지 더해보세요

'''

for x in list :
     print(x,end=" ")
print('---------------------------')

for x in range(0,len(list),2) :
     print(list[x],end=" ")

print('---------------------------')
sum = 0
for x in range(0,len(list),2):
     sum = sum + int(list[x])
     if int(list[x]) == list[-1]:
          print(sum,end=" ")

print('---------------------------')

for x in range(1,len(list),2):
     print(list[x],end=" ")
print('---------------------------')

sum2 = 0
for x in range(0,1001):
     sum2 = sum2 + x
     if x == 1000 :
          print(sum2,end=" ")
