# 극장 예매 시스템
# 1. 화면을 만든다.  0이 10 개들어간 list 필요
seat = [0] * 10  # 0 을 10개 만든다. [0,0,0,0,0,0,0,0,0,0] 이렇게 쓸 필요 없음.
name = input('이름을 입력해주세요. >>')
count = 0  # 몇매 예매했는지 누적합 하기 위해 변수 지정
price = 10000  # 영화 티켓 장당 가격 지정
while True:

    print("-----------------------------")
    print('좌석 번호')
    for x in range(0, len(seat)):
        print(x + 1, end=' ')
    print("\n-----------------------------")
    # 자리 자리예약 상태 프린트 => 0 은 빈자리 아니고 1은 있는자리
    print("예매현황")
    for x in range(0, 10):
        print(seat[x], end=" ")
    print("\n-----------------------------")
    print('참고 0 => 예약가능 좌석 1 => 예약 불가능 좌석 ')
    choice = int(input('\n원하는 좌석번호 입력(종료 : x) >> '))

    # 예매 프로그램 종료
    if choice == -1:
        a = count * price
        print("\n-----------------------------")
        print(name + '님의 예매확인 영수증 입니다.')
        print("\n-----------------------------")
        print('전체 예매된 좌석수는' + str(count) + '좌석')
        print('예매하신 좌석번호는 : ',end= " ")
        for index in range(1, len(seat)+1):
            if seat[index-1] == 1:
                print(index, '번', end=' ')
        print("")
        print('결제 금액은', a, '입니다.')
        print("\n-----------------------------")
        print('예매프로그램을 종료합니다. ')
        print("\n-----------------------------")
        break

    #선택 좌석 알림
    print(str(choice + 1), "번을 선택하셨습니다.")
    print('.')
    print('.')
    print('.')

    # 이미 예매처리가 된 경우 불가능하다고 처리
    if seat[choice] == 1:
        print('이미 예매가 된 좌석입니다.')
        print('다른 좌석을 선택해주세요.')


    # 입력받은 좌석번호로 예매 처리
    else:
        seat[choice] = 1
        print('예매 처리를 완료하였습니다.')
        print(choice + 1, '번 자리가 예매되었습니다.')
        # 좌석수 카운트 및 가격 곱하기 좌석수 카운트 => 총 가격
        if seat[choice] == 1:
            count = count + 1
        print('현재 예매 좌석수 : ', count, '석')
        print("\n-----------------------------")

    # 입력값은 리스트의 index로 사용될 예정 # index는 좌석번호
