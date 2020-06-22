from tkinter import *
from tkinter import messagebox

# 함수 => function(기능)
# 기능에 대한 정의를 하기 때문에 def

'''
def login():
    print('login 함수 호출됨.')
    id = id_text.get()  # get/set  세트 ( 함께 사용)
    pw = password_text.get()
    if (id == 'root' and pw == '1234'):
        messagebox.showinfo('결과', '로그인 ok!')
    else:
        messagebox.showinfo('결과', '로그인 not...')
'''


def login2():  # 특정한 객체에 함수를 연결 (bind)
    # 1. 입력한 id , pw 를 가지고 온다.
    id = id_text.get()
    pw = password_text.get()
    # 2. 입력한 id 에 해당하는 파일을 읽기 전용으로 스트림을 만든다.
    file_name = id + '.txt'
    file = open(file_name, 'r')
    # 3. 파일에서 id,pw 를 차례대로 읽는다.
    id_saved = file.readline()
    pw_saved = file.readline()
    file.close()  # 스트림을 닫아줌


    # 4. 읽어온 후 , 비교하기 전에 데이터에 문제가 있으면 미리 처리해 줄것. (전처리)

    id_saved2 = id_saved.strip()  # 공백 없는게 2
    pw_saved2 = pw_saved.strip()

    # 5. 비교 처리 하여 결과 출력
    if (id == id_saved2 and pw == pw_saved2):
        messagebox.showinfo('결과', '로그인 ok!')
    else:
        messagebox.showinfo('결과', '로그인 not...')


w = Tk()  # 로그인 창을 만들어 줌.   #import 시켰는데 안뜨고 에러나면 alt + enter 치면 도와줌. (자동 import)
w.geometry('640x320')  # 크기 조절
w.configure(bg='lime')  # 수많은 색중에 lime 을 선택해서 불러오는 건가?
# 그림위에 언져진 글씨 => 라벨
# 아이디 라벨
id_label = Label(w,
                 text='사용자 ID 입력',
                 font=('맑은 고딕', 30),  # 튜플형태로 넣으라고 이미 지정되어 있음.
                 bg='lime',
                 fg='white'  # 포 그라운드 앞쪽 색깔
                 )
id_label.pack()  # 기본으로 가운데 정렬해서 들어감.   => 변수 전 (id_label 이전에 들어가면 안됨. 변수 지정이 안됬기 때문)
# pack 포장하다. 위치 중요
# 어느 곳에 얹을 거니 ? , 어떤 글을 얹을거니? , 백그라운드 색깔은? , 포그라운드 색깔은?
id_text = Entry(w,
                font=('맑은 고딕', 30),
                bg='yellow',
                fg='red'
                )
id_text.pack()

# 패스워드 라벨
password_label = Label(w,
                       text='사용자 PW 입력',
                       font=('맑은 고딕', 30),
                       bg='lime',
                       fg='white')
password_label.pack()

password_text = Entry(w,
                      font=('맑은 고딕', 30),
                      bg='yellow',
                      fg='red'
                      )

password_text.pack()

# button = Button(w, text = 'me' )
# 이미지로 부품화 (객체화) 시켜줌
icon = PhotoImage(file='naver.png')
button = Button(w, image=icon, command=login2)  # 이미지로 인식을 못하면 이미지 부품화를 시켜줘야함.
button.pack()

# 버튼을 처리할 때 하나의 처리로 함수를 만들어줌.

w.mainloop()  # 눈에 보이면서 너 계속 떠있어.   w. => 저 기능에 접근하는 방법 .은 접근 연산자.
