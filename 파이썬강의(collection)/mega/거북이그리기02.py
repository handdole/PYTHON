import turtle

pen = turtle.Pen()
pen.color('red')
pen.shape('turtle')

while True:
    choice = input("왼쪽 : left , 오른쪽 : right , 종료 : x >> ")
    if choice == 'x':
        print("종료합니다")
        break
    if choice == 'left':
        pen.left(54)
        pen.forward(100)
    if choice == 'right':
        pen.right(135)
        pen.forward(100)

# 들여쓰기 : indent (인덴트)
# 코드 자동 정리 => ctrl + shift + f
