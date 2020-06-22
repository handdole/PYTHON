if result == 'no':
    messagebox.showinfo("정보", "키가작으시군요")
    break
a = a + 10
if result == 'no':
    while True:
        result = messagebox.askquestion("물음", str(a + b) + "이십니까?")
        if result == 'no':
            b = b + 1
        if result == 'yes':
            messagebox.showinfo("정보", str(a + b) + "이시군요")
            break




