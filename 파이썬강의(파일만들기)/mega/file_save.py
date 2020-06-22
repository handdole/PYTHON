movie = ['정직한 후보', '작은 아씨들', '클로젯', '기생충', '수퍼소닉']

# for each 반복문
for data in movie:
    print(data, end=" ")

print()

# for 반복문
for index in range(0, len(movie)):
    print(movie[index])

# 리스트, 딕셔너리등과 같은 collection 계열 내용 확인
print(movie)

# 파이썬에서 어떠한 파일로 빨대를 꼽는 것을 스트림이라고 한다.
file = open('movie.txt', 'w')  # 강물(stream ,스트림)을 열다.
# finamce.naver.com site로 연결
# 사이트 , 네트워크 , DB , file연결 등 외부 자원을 연결
# => stream을 만들어야 한다.

# file.write('내용이 들어갑니다.')
for data2 in movie:
    file.write(data2+'\n')

