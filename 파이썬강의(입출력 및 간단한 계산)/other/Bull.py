#계산기 세부기능

def div():
    print("나누기 기능 처리")
    data1 = int(input("숫자1을 입력하세요."))
    data2 = int(input("숫자2를 입력하세요."))
    print("두 수의 나누기값은", data1/data2, "입니다.")


def mul():
    print("곱하기 기능 처리")
    #두 수를 입력받아서 덧셈 처리
    data1 = int(input("숫자1을 입력하세요."))
    data2 = int(input("숫자2를 입력하세요."))
    print("두 수의 덧셈값은",data1*data2,"입니다.")

def plus():
    print("더하기 기능 처리")
    #두 수를 입력받아서 덧셈 처리
    data1 = int(input("숫자1을 입력하세요."))
    data2 = int(input("숫자2를 입력하세요."))
    sum = data1 + data2
    print("두 수의 덧셈값은",sum,"입니다.")

def minus():
    print("빼기 기능 처리")
    #두 수를 입력받아서 빼기 처리
    n3 = input("숫자1을 입력하세요: ")
    n4 = input("숫자2를 입력하세요: ")
    b = int(n3) - int(n4)

    print("두 수의 덧셈값은", b, "입니다.")