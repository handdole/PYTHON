'''
while True:
    data = input('지금 먹고 싶은 것? 물 , 아메리카노 , 맥주 >>')
    if data == '물':
        print('밖으로 나가서 정수기로 갑니다.')
    elif data == '아메리카노':
        print('카페로가세요~')
    elif data == '맥주':
        pass
    else:
        print('다시제대로입력해주세요')
'''

'''
지금시각은 ? 
11시 이전이면 굿모닝
17시 이전이면 굿애프터눈
22시 이전이면 굿이브닝
나머지는 굿나잇
'''

while True :
    time = int(input("지금 시각은 ? : "))
    if time < 11 :
        print("굿모닝")
    elif time < 17 :
        print("굿에프터눈")
    elif time < 22 :
        print("굿이브닝")
    else :
        print("굿나잇")




