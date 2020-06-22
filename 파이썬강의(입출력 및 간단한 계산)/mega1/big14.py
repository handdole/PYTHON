'''
네이버 로그인
판단을 할 때 조건을 가지고 판단을 한다.
조건이 하나가 아닌 경우 논리적으로 어떻게 판단할 것인가?
지하철을 타는 경우 1) 편해서 2) 저렴해서
조건들이 모두 true 여야 / 논리적으로 판단하는경우  -> and 조건
조건들 중에 하나만 맞아도 / 논리적으로 판단하는 경우 -> or 조건
'''

from tkinter import messagebox

id = "root"
password = "pass"

id2 = input("아이디 입력 : ")
pw2 = input("패스워드 입력 :")

if (id == id2 and password == pw2) :
    print("로그인이 되었습니다.")
elif id == id and password != pw2 :
    print("비밀번호를 확인해주세요.")
else :
    print("아이디 혹은 비밀번호를 확인해주세요.")





