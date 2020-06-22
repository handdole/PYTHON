name = ['홍길동','박길동','송길동']
print(name[0])   # index 가 증가 한다고 볼 수 있다.
print(name[1])
print(name[2])
print("--------------------------")

index = 0   # start 값
while index < 3 :   # 조건식
    print(name[index])
    index = index + 1   #증감식
print("--------------------------")
print(name)
print("---------------------------")

#팀원의 나이의 리스트를 만들어서
#반복문으로 찍어보고 리스트의 전체목록 확인

name = ['이주엽씨','박재영씨','박한솔']
age = [30,28,26]
i = 0    # 리스트 값을 맞춰주면 굳이 변수를 두개 만들 필요가 없다.
length = len(age)

while i < length :   #while i < len(age)
    print(name[i],age[i])
    i = i+1
print('+++++++++++++++++++++++++++++')
print(name,age)
print(len(age))      #리스트의 총 개수 len(리스트 명)

print(age[len(age)-1]) # ★★★★계수보다 하나 작은것이 마지막 인덱스이기 때문에 이런 표현식이 가능하다.★★★★