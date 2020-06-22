# 자판기 프로그램
# 메뉴, 가격 , 수량 표시
select = []
menu = ['포카리', '코카콜라', '레쓰비', '초코송이', '빼빼로', '다이제', '자일리톨']
don = [800, 800, 600, 900, 1000, 1500, 1000]
stock = [7, 6, 4, 5, 7, 0, 8]
sum = 0

# 상품 선택 진행 과정
while True:
    for x in range(0, len(menu)):
        print(x + 1, '번 상품')
        print('상품이름: ', menu[x], end=" / ")
        print('가격 :', don[x], end=" / ")
        print('재고 : ', stock[x], end=" ")
        print("")

    choice = input('상품을 하나씩 선택해주세요. >> ')

    if choice not in menu:  # 메뉴에 없는 것을 선택할 경우 append 안함.
        print("없는 상품입니다.")
        print('다시 선택해주세요.')
    elif stock[menu.index(choice)] == 0:
        print('제고가 없는 상품입니다. 다시 선택해주세요.')
    else:  # 메뉴에 있는 것을 선택하면 append 함.
        select.append(choice)
        yon = input(choice + "를 선택하셨습니다. 더 추가하시겠습니까? (Y/N)")  # 추가여부
        stock[menu.index(choice)] = stock[menu.index(choice)] - 1   # 재고 -1 씩 됨
        if yon == 'y':  # y 누르면 메뉴 추가 가능.
            pass
        elif yon == 'n':  # n 누르면 여태까지 입력한 메뉴 확인 작업.
            for x in range(0, len(select)):
                print(select[x], end=' ')
            print('를 주문하셨습니다.')
            yon1 = input('이대로 주문 하시겠습니까? (Y/N)')  # 주문확인
            if yon1 == 'y':  # 맞을경우 결제 진행
                break
            elif yon1 == 'n':  # 틀릴 경우 다시 처음부터 메뉴 선택
                select.clear()
                print(select)
                continue         # 문제! -1씩 한게 취소하면 안바뀜
            else:  # 다른 것을 고른 경우
                print('Y/N 만 가능합니다.')
        else:  # 다른 것을 고른 경우
            print('Y/N 만 가능합니다.')

# 총 금액 계산 과정

for x in range(0, len(select)):
    index1 = menu.index(select[x])
    sum = sum + don[index1]
print('총 금액은', sum, '입니다.')

# 결제 진행 과정
while True:
    choice2 = int(input("결제를 진행합니다. 카드는 1번 현금은 2번을 눌러주세요 >> "))
    if choice2 == 1:
        print('카드를 태그해주세요')
        print(str(sum) + '원이 결제가 완료되었습니다. 감사합니다.')
        break
    elif choice2 == 2:
        while True:
            don1 = int(input('현금을 넣어주세요 >> '))
            if don1 > sum:
                print(str(sum) + '이 계산되었습니다. 잔돈은' + str(don1 - sum) + '입니다. 감사합니다.')
                break

            elif don1 == sum:
                print(str(sum) + '이 계산되었습니다. 감사합니다.')
                break

            else:
                print('현금이 부족합니다.', sum - don1, '만큼 넣어주세요')
                sum = sum - don1
    else:
        print('1 혹은 2번중에 선택해주세요.')
