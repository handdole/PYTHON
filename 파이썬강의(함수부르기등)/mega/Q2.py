# Q10

for x in range(1, 21):
    print(x)
print("-----------------------")

for x in range(1, 21):
    print(x, end=' ')

# 14
while True:
    food = input("먹고 싶은 음식 입력 (종료 x ) >> ")
    if food == 'x':
        print('------------------------')
        print('입력을 종료합니다.')
        break

# 15

list1 = []

while True:
    com = input('기업 리스트 입력 (종료 x입력) >> ')
    list1.append(com)
    if com == 'x':
        print('------------------------')
        print('입력값을 출력합니다.')
        list1.remove('x')
        break
print(list1)

# 16

point = []

while True:
    x = 1
    sum = 0
    while True:
        a = int(input(str(x) + '학기의 총점을 입력하세요.(총학기 평균 출력 버튼은 0) >> '))
        point.append(a)
        x = x + 1
        if a == 0:
            point.remove(0)
            break
    for y in point:
        sum = sum + y
    avg = sum / len(point)
    print('---------------------------------')
    print('총학기 평균은', str(avg) + '점입니다.')
    break

# 17

print('정답은 77입니다.')

while True:
    a = int(input('당신이 생각한 정답 >> '))
    if a == 77:
        print('정답입니다.')
        break
    else:
        print('정답이 아닙니다.')

# 17 응용 -> 생각하는 숫자 맞추기
import random

print("제가 생각하는 숫자를 맞춰보세요.")
print('업,다운으로 힌트를 드리겠습니다.')
print('숫자는 1에서 100까지의 정수입니다.')

random_N = random.randint(1, 100)
i = 0 #초기화 변수는 항상 반복문 밖에 넣는다.

while True:
    i = i+1
    n = int(input('제가 생각하는 숫자는 ? >> '))
    if n == random_N:
        print('정답입니다!!!!!')
        q = input('게임을 다시 시작하겠습니까?')
        if q == 'Y':
            print('게임을 다시 시작합니다.')
        elif q == 'n':
            print('==========================')
            print('수고하셨습니다. 게임을 종료합니다.')
            break

    elif n > random_N:
        print('다운!')

    else:
        print('업!')


# 18
print('은행 시스템 입니다.')

a = int(input('입금액을 입력해주세요 >> '))
b = float(input('이자율을 입력해주세요 >> '))

print('================================')

print('1년후 받게될 금액은' + str(a + (a * b)) + '입니다.')
# 19

dic = {'키': '163', '몸무게': 60, '사는곳': '파주', '취미': '운동', '좋아하는 색': '검정색'}

print(dic.get('좋아하는 색'))

# 20
loc = []
while True:
    loc2 = input(" 장소 입력 (종료 : x ) >>")
    loc.append(loc2)
    if loc2 == 'x':
        loc.remove('x')
        break
for x in range(0, len(loc)):
    print(loc[x], end=" ")
print("")

print("---------------------------------------")
loc.remove("강남")

if '강남' in loc:
    print("강남있음")
    # 인덱스 필요!
    idx = loc.index('강남')
    # 인덱스를 가지고 del
    del loc[idx]

for x in range(0, len(loc)):
    print(loc[x], end=" ")
print("")
print("=========================================")

for a in range(0, len(loc)):
    if loc[a] == '제주도':
        loc[a] = '제주시'
for x in range(0, len(loc)):
    print(loc[x], end=" ")
print("")
print("+++++++++++++++++++++++++++++++++++++++++")
for x in range(0, len(loc)):
    print(str(x + 1) + "위", loc[x])
