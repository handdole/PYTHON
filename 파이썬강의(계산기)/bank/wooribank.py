from cal.계산기 import mul, add
#cal패키지에 있는 계산기 모듈로 부터
#사용하고자 하는 mul,add함수를 import 해준다.

이자율 = 0.2  #이자가 아니라 이자율로 변수를 선언해야함.
money = int(input('예금액을 입력하시오. >> '))  #money는 int값임으로 int를 선언해주어야 함.
이자 =  mul(money, 이자율)
total_money = add(money, 이자)
print('예금 최종 지불 금액은 %d' %total_money)
