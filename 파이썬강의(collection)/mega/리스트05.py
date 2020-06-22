'''
입력 : 홍길동
입력 : 파이썬
입력 : 프로그래머
입력 : 데이터 분석가

홍길동 파이썬 프로그래머 데이터 분석가

sum 이라는 변수에 입력값 누적하여 sum을 프린트
'''

sum = ""

while True :
     data = input("입력 (종료는 x) : ")
     if data == 'x' or data == 'X' :
          print("종료되었습니다.")
          break
     sum = sum +" "+data

print(sum)