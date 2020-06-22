from tkinter import *
from tkinter import messagebox


def insert():
    id = id_text.get()  #entry 에 들어온 id_text를 get을 써서 변수로 저장
    pw = password_text.get()
    name = name_text.get()
    pn = pn_text.get()
    print(id)
    login_file = open(id + 'txt', 'w')
    login_file.write(id + '\n')
    login_file.write(pw + '\n')
    login_file.write(name + '\n')
    login_file.write(pn + '\n')
    messagebox.showinfo('결과', '회원가입이 완료되었습니다.')
    login_file.close()  # 스트림을 닫아주어야한다.


i = Tk()
i.geometry('550x700')
i.configure(bg='white')

# 최상단 아이콘 라벨

icon = PhotoImage(file='naver1.png')
icon_label = Label(i,
                   image=icon
                   )
icon_label.pack()

# 아이디 입력 라벨
id_label = Label(i,
                 text='사용자 ID 입력',
                 font=('맑은 고딕', 30),  # 튜플형태로 넣으라고 이미 지정되어 있음.
                 bg='white',
                 fg='black'  # 포 그라운드 앞쪽 색깔
                 )
id_label.pack()

# 아이디 입력 란
id_text = Entry(i,
                font=('맑은 고딕', 30),
                bg='white',
                fg='black'
                )
id_text.pack()

# 패스워드 입력 라벨
password_label = Label(i,
                       text='사용자 PW 입력',
                       font=('맑은 고딕', 30),
                       bg='white',
                       fg='black')
password_label.pack()

# 패스워드 입력 란
password_text = Entry(i,
                      font=('맑은 고딕', 30),
                      bg='white',
                      fg='black'
                      )

password_text.pack()

# 이름 입력 라벨
name_label = Label(i,
                   text='사용자 이름 입력',
                   font=('맑은 고딕', 30),
                   bg='white',
                   fg='black')
name_label.pack()

# 이름 입력 란
name_text = Entry(i,
                  font=('맑은 고딕', 30),
                  bg='white',
                  fg='black'
                  )

name_text.pack()

# 전화번호 입력 라벨
pn_label = Label(i,
                 text='사용자 핸드폰 번호 입력',
                 font=('맑은 고딕', 30),
                 bg='white',
                 fg='black')
pn_label.pack()

# 전화번호 입력 란
pn_text = Entry(i,
                font=('맑은 고딕', 30),
                bg='white',
                fg='black'
                )

pn_text.pack()

icon1 = PhotoImage(file='naver2.png')
button = Button(i, image=icon1, command=insert)  # 이미지로 인식을 못하면 이미지 부품화를 시켜줘야함.
button.pack()

i.mainloop()
