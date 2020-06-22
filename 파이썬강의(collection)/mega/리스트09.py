import datetime

'''
1)
2월 전이면 아직은 조금 춥겠군요.
2월 이면 조금 있으면 봄이 오겠군요.
아니면 새해의 시작이 되겠군요.
'''
now = datetime.datetime.now()
m = now.month

if m < 2:
    print("아직은 조금 춥겠군요")
elif m == 2:
    print("조금 있으면 봄이 오겠군요")
else:
    print('아니면 새해의 시작이 되겠군요')

'''
2)
3-5까지는 봄
6-8까지는 여름
9-11까지느 가을
나머지는 겨울
'''
if 3 < m <= 5:
    print('봄')
elif 5 < m <= 8:
    print('여름')
elif 9 < m <= 11:
    print('가을')
else:
    print('겨울')

'''
2월은 28일이나 29일까지 입니다.
나머지달은 30일인지 31일인지 프린트
'''

if m == 2:
    print("2월은 28일이나 29일까지 입니다.")
elif m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
    print('이번달은 31일 이군요')
else:
    print("이번달은 30일 이군요")
