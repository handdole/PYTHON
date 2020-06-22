food = ['불족발', '틈새라면', '곱창', '소고기', '라면']

print(food[0])
print(food[-1])
print(food[-2])
"""
인덱싱은 인덱스 하나 정해서 불러오는거고 
슬라이싱은 범위를 지정해서 가져오는것
"""
print(food[1:3])
print(food[2:])  # 생략하면 범위가 끝까지 된다.
print(food[:3])  # 생략하면 범위가 끝까지 된다.

print("--------------------------------------")
drink = ['물', '아메리카노', '맥주']
all = food + drink
print(all)
print("--------------------------------------")
drink3 = drink * 3
print(drink3)

print("--------------------------------------")
drink.insert(0, '라떼')  # 파괴형 함수
print(drink)

print(drink.index('라떼') + 1)  # 비파괴형 함수
