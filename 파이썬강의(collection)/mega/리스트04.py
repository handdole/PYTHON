movies = [] # 빈 리스트

# movies[0] = 100
# print(movies)

# 삽입 => 중간에 , 추가 +>끝에
'''
movies.append(100)
print(movies)
movies.append(200)
print(movies)
movies.append(300)
print(movies)
'''
# 점수 입력 80 , 90 , 70 / 정수의 합계는 ?  점수의 평균은 ?
point = []  # 빈 리스트 생성
i = 0 # idex 변수 값 생성
sum = 0 # sum 변수 값 생성
while i < 3 :  # 조건문 실행 T 경우 순환 F경우 정지
     data = input("점수 입력 : ")  # 점수를 입력 받아서 DATA에 저장
     point.append(int(data))   # 저장 받은 데이터를 INT 함수로 정수화 시키고 빈 리스트 POINT 에 APPEND
     sum = sum + point[i]   # 처음 총합은 0 에서 새로 입력되는 리스트 값을 누적 합산
     i = i+1 #다음 입력값을 받기위해 인덱스 값 1증가

avg = sum / len(point)  # 평균구하는 공식

print(avg) #평균 출력
print(sum) #누적 합 출력력
print(point)    # 원본을 안 건드렸나요? 비파괴적 함수
point.sort()    # 원본을 건드렸나요 ? 넵.                      -> 자바에서 더 정확하게 잡음.
                # 원본을 건드리는 함수 = 파괴적 함수

print(point)

'''
while True :
    data = input("점수 입력 : ")
    point.append(int(data))
'''