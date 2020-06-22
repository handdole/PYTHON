# 리스트 , 집합 , 사전 , 튜플 => 모음 (collection)
team = {'디자이너', '프로그래머', 'DB관리자'}
print(team)
team.add('사무부장')
print(team)

rank = ['박스키', '송스키', '김스키', '정스키']
del rank[1]
print(rank)

dial = {1: '엄마', 2: '아빠', 3: '형', 4: '동생'}
print(dial.get(2))
print(len(dial))