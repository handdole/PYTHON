#예금 만기시 , 만기 지급액은 원금과 이자를 합하여 계산한다.
def add(money  , interests):
    #원금과 이자를 합하여 계산하고 출력하는 것이 아니라 값을 리턴해야한다.
    result = money + interests
    return  result
#이자는 원금에 이자율을 곱하여 계산한다.
def mul(money , rates):
    #원금과 이자를 합하여 계산하고 출력하는 것이 아니라 값을 리턴해야한다.
    result = money * rates
    return result