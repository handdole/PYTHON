'''
1.
아이디와 이름을 입력받아 프린트
아이디가 root인 홍길동님이 로그인 되었습니다.
'''
'''
id = input('아이디를 입력하세요. >> ')
name = input('이름을 입력하세요. >> ')

print('아이디가',id,'인',name,'님이 로그인 하셨습니다.')
'''

'''

2.
두 수를 입력받아서 산술연산을 하여 프린트 
숫자1 : 33
숫자2 : 7
------------------------------------
두 수의 합은 
두 수의 차는
두 수의 곱은
두 수의 나눗셈은 
나누고 난 너머지 값은 
몫은 
'''

'''
n1 = int(input('숫자1을 입력하세요 >> '))
n2 = int(input('숫자2를 입력하세요 >> '))

print('두수의 합은',n1+n2)
print('두수의 차은',n1-n2)
print('두수의 곱은',n1*n2)
print('두수의 나눗셈은',n1/n2)
print('두수의 나누고 난 나머지는',n1%n2)
print('두수의 나눗셈 후 몫은',n1//n2)

'''

'''
3.
이름과 나이를 입력받아서 다음과 같이 프린트 
홍길동님의 10년 후의 나이는 110세입니다.
'''

'''

name1 = input('당신의 이름은 ? : ')
age = int(input('당신의 나이는 ? : '))

print(name1,'님의 10년 후 나이는',str(age+10)+'입니다.')

'''

'''
4.
다음과 같이 판별되도록 프린트 (10000원 기준)
엄마 용돈 주세요. : 15000(입력)
-> 엄마 너무 용돈이 많아요.

엄마 용돈 주세요. : 8000 입력
-> 엄마 용돈이 너무 적어요.
'''

'''

money = int(input('엄마 용돈주세요 >> '))

if money >= 10000:
    print('엄마 용돈이 너무 많아요')
else:
    print('용돈이 너무 적어여')

'''

'''
5. 
숫자를 입력하여 짝 홀 수를 판별해보세요.
'''
'''

while True:
    a = int(input('정수를 입력하세요 짝수인지 홀수인지 알려드립니다.(숫자 0은 종료) >> '))

    if a % 2 == 0:
        print('짝수입니다.')
    else:
        print('홀수입니다.')

    if a == 0:
        print('종료합니다.')
        break

'''
'''
6.
다음과 같이 처리되도록 코딩 (실적목표 : 1000 ,보너스 : 20% , 단위 : 만원)
실적을 입력하세요 >> 1500

-> 축하합니다. 실적을 달성하셨습니다.!
-> 당신의 이번달 보너스는 300만원 입니다.
'''
'''

good = int(input('실적을 입력하세요 >> '))
b = good*0.2

if good > 1000:
    print('축하합니다. 실적을 달성하셨습니다!')
    print('당신의 이번달 보너스는',b,'만원입니다.')
else :
    print('실적을 달성하시지 못하셨습니다.')
'''


'''
7. 
다음과 같이 처리되도록 코딩
미사일 이름은 : 슛 (입력)
미사일 시작값은 : 200(입력)
미사일 움직이는 값은 : -10.5 (입력)

'''

'''
name = input('미사일의 이름은? >>')
start = int(input('미사일의 시작값은? ??'))
move = float(input('마시일 움직이는 값은?>>'))

print(name,'미사일이',str(start+move)+'로 이동되었습니다.')

'''


'''
8.
다음의 데이터를 입력받아 , 영수증을 출력하세요.
받은 돈 : 10000
상품의 총액 7500
부가세 750
잔돈 : 2500
'''
'''
money = int(input('받은 돈 >> '))
money2 = int(input('상품의 총액 >>'))
a = money2*0.1

print('받은돈 >>',money)
print('상품의총액 >>',money2)
print('부가세 >>',a)
print('잔돈 >>',money-money2)
'''

'''
9.
별을 1000개 프린트
'''
'''
for x in range(0,40) :
    for y in range (0,25):
        print('★',end='')
    print("")
'''

import random

print("제가 생각하는 숫자를 맞춰보세요.")
print('업,다운으로 힌트를 드리겠습니다.')
print('숫자는 1에서 100까지의 정수입니다.')

random_N = random.randint(1, 100)

while True:
    n = int(input('제가 생각하는 숫자는 ? >> '))
    if n == random_N:
        print('정답입니다!!!!!')
        q = input('게임을 다시 시작하겠습니까? (y/n) ')
        if q == 'Y':
            print('게임을 다시 시작합니다.')
            pass
        elif q == 'n':
            print('==========================')
            print('수고하셨습니다. 게임을 종료합니다.')

        break
    elif n > random_N:
        print('다운!')
    else:
        print('업!')