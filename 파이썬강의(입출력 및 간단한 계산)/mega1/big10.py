from tkinter import messagebox

messagebox.showinfo("하위","나임ㅋ") #(a,b)   a가 위에 나오는거고 b가 본문에 나오는거
messagebox.showwarning("지금은 오후임!!" , "졸음주의")
result = messagebox.askquestion("지금은 오후인가연?"," 맞으면 ㅇ 아니면 x ")
print(result)
if result == "yes" :
    messagebox.showwarning("경고","자면안됨")
else :
    messagebox.showwarning("경고","놀면안됨")


