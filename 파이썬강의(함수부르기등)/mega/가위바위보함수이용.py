import random

list1 = ['가위!', '바위!', '보!']

while True:
    print('가위 바위 보 게임 시작.')
    print("------------------------------")
    print("종료는 9 번을 눌러주세요")
    my = int(input('가위 0 바위 1 보 2 ! >> '))
    if my not in (0,1,2,9):
        print("제대로 입력해주세요.")
    cum = random.randint(0, 2)

    if my == 0:
        print("나는 가위!")
        print("컴퓨터는",list1[cum])
        print("------------------------------")

        if my == cum:
            print("무승부군요")
            print("------------------------------")
        elif my + 1 == cum:
            print("지셨군요...")
            print("------------------------------")

        else:
            print("이기셨군요!")
            print("------------------------------")

    if my == 1:
        print("나는바위!")
        print("컴퓨터는", list1[cum])
        print("------------------------------")

        if my == cum:
            print("무승부군요")
            print("------------------------------")

        elif my - 1 == cum:
            print("이기셨군요!")
            print("------------------------------")

        else:
            print("지셨군요...")
            print("------------------------------")

    if my == 2:
       print("나는보!")
       print("컴퓨터는", list1[cum])
       print("------------------------------")

       if my == cum:
           print("무승부군요")
           print("------------------------------")

       elif my - 1 == cum:
           print("이기셨군요!")
           print("------------------------------")

       else:
          print("지셨군요...")
          print("------------------------------")

    elif my == 9 :
        print('게임을 종료합니다.')
        break

