#영화보기 함수

def info():
    name = input("영화를 같이 볼 사람의 이름 : ")
    re = input("함께 볼 사람의 관계를 입력하세요. :")
    print("함께 볼 사람의 이름은",name,"관계는",re,"입니다.")

def pay():
    price = 10000
    p = int(input("인원수를 입력해 주세요 : "))
    print("지불할 금액은",price*p)