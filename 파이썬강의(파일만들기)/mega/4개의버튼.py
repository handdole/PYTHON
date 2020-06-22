from tkinter import *

subject = []
original = [50, 40, 30, 20]
plus = []
items = ['광고', '마케팅', '그로스해킹']



def one():
    for _ in range(0, 4):
        sub = input('배우고 싶은 과목 입력 >> ')
        subject.append(sub)
    for x in subject:
        print(x, end=' ')
    print("")
    print(subject)


def two():
    for x in range(0, len(original)):
        plus2 = original[x] + 10
        plus.append(plus2)
    print(plus)


def three():
    file = open('hongbo.txt', 'w')
    for x in range(0, len(items)):
        file.write(items[x] + '\n')
        print(items[x])
    print(items)

    file.close()


def four():
    file1 = open('hongbo.txt', 'r')

    for _ in range(0, 3):
        data = file1.readline()
        data1 = data.strip()  # strip 은 readline 다음에 사용
        print(data1 + '짱')

    file1.close()

# tkinter 이용 4개의 버튼 만듬

w = Tk()
w.geometry('450x350')
w.configure()

save_print = Button(w,
                    text='저장하고 프린트',
                    font=('맑은고딕', 30),
                    bg='blue',
                    fg='black',
                    command=one    # 함수 one을 호출하는 버튼
                    )

save_print.pack()

plus_ = Button(w,
               text='플러스해서 출력',
               font=('맑은고딕', 30),
               bg='blue',
               fg='black',
               command=two # 함수 two을 호출하는 버튼
               )

plus_.pack()

save_print2 = Button(w,
                     text='저장하고프린트2',
                     font=('맑은고딕', 30),
                     bg='blue',
                     fg='black',
                     command=three  # 함수 three을 호출하는 버튼
                     )

save_print2.pack()

jjang = Button(w,
               text='짱짱짱',
               font=('맑은고딕', 30),
               bg='blue',
               fg='black',
               command=four  # 함수 four을 호출하는 버튼
               )

jjang.pack()

w.mainloop()
