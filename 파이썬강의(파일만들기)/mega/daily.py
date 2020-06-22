# 일기를 입력 ( 날씨 , 제목 , 날씨 , 내용)
# 파일이름 : 날짜.txt , 위치는 mega
# 일기를 쓸때마다 날짜 다르니 파일 이름 다르게 설정

if (input('id : ') == 'root' and input('pw: ') == '1234'):
    date = input('오늘의 날짜 : ')
    title = input('오늘의 제목 : ')
    weather = input('오늘의 날씨 : ')
    content = input("오늘의 내용 :")

    diary = open(date + 'txt', 'w')
    diary.write(date + '\n')
    diary.write(title + '\n')
    diary.write(weather + '\n')
    diary.write(content + '\n')

else:
    print('아이디와 비밀번호가 맞지않습니다.')
