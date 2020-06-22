"""
콘솔에서 당신의 짝 이름을 입력받으세요.
콘솔에서 당신이 짝 관심사를 입력받으세요.
메세지 박스로 당신의 짝이름과 관심사를 확인하여 출력
관심사가 파이썬이라고 한다면 , "프로그래머가 되실 거군요"
아니라면 , "데이터 분석가가 되실 거군요" 출력

★★★★ messagebox 에서는 문자열을 받을 수 없고 예 아니오 취소 같은 버튼 기능만 가능하다. ★★★★
콘솔은 오른쪽에 있는게 콘솔
"""
from tkinter import messagebox

name = input("당신의 이름은?")
good = input("당신의 관심사는?")

messagebox.showinfo("확인" , name+good)
if good == "파이썬" :
    print("프로그래머가 되고싶으시군요")
else :
    print("데이터분석가가 되실거군요0")


'''
메세지 박스로 파이썬이 확실한가요?
맞다라고 하면, 열심히 하세요!
아니라고 하면, 그럼 생각중이시군요!
'''

from tkinter import messagebox

result = messagebox.askquestion("파이썬이 확실한가요?", "맞으면 o 틀리면 x ")
print(result)
if result == "yes":
    messagebox.showinfo("야스", "열심히하세요")
else:
    messagebox.showinfo("노", "생각중이시군요")

