
me = {0:'가위',1:'바위',2:'보'}
com = {0:'가위',1:'바위',2:'보'}

def win() :
    if me.get(0) and com.get(1):
        print('WIN')
    if me.get(1) and com.get(0):
        print('WIN')
    if me.get(2) and com.get(1):
        print('WIN')

def draw() :
    if me.get(0) and com.get(0):
        print('draw')
    if me.get(1) and com.get(1):
        print('draw')
    if me.get(0) and com.get(0):
        print('draw')

def lose():
    if me.get(0) and com.get(1):
        print('lose')
    if me.get(1) and com.get(2):
        print('lose')
    if me.get(2) and com.get(0):
        print('lose')

