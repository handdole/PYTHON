#계산기 모듈을 여기에 사용하겠다는 표현
from other import Bull

select = input("연산을 선택하세요 1.더하기2.곱하기3.나누기4.빼기 >> ")

if select == "1":
    Bull.plus()
elif select =="2":
    Bull.mul()
elif select =="3":
    Bull.div()
elif select == "4" :
    Bull.minus()
else :
    print("잘못입력하셨습니다.")




