from tkinter import *

#기본설정
adder = Tk()
adder.title('계산기')
adder.config(background='black')
adder.config(height=400, width=260)

#함수정의
def Number(value):
    print(value)

#버튼 0 ~ 9 + =
keyboard_1 = Button(text='1', font='맑은고딕 20', command=lambda:Number('1'))
keyboard_1.place(x=50, width=50, height=50, y=100)

keyboard_2 = Button(text='2', font='맑은고딕 20')
keyboard_2.place(x=100, width=50, height=50, y=100)

keyboard_3 = Button(text='3', font='맑은고딕 20')
keyboard_3.place(x=150, width=50, height=50, y=100)

keyboard_4 = Button(text='4',font='맑은고딕 20')
keyboard_4.place(x=50, width=50, height=50, y=150)

keyboard_5 = Button(text='5',font='맑은고딕 20')
keyboard_5.place(x=100, width=50, height=50, y=150)

keyboard_6 = Button(text='6',font='맑은고딕 20')
keyboard_6.place(x=150, width=50, height=50, y=150)

keyboard_7 = Button(text='7',font='맑은고딕 20')
keyboard_7.place(x=50, width=50, height=50, y=200)

keyboard_8 = Button(text='8',font='맑은고딕 20')
keyboard_8.place(x=100, width=50, height=50, y=200)

keyboard_9 = Button(text='9',font='맑은고딕 20')
keyboard_9.place(x=150, width=50, height=50, y=200)

keyboard_0 = Button(text='0',font='맑은고딕 20')
keyboard_0.place(x=100, width=50, height=50, y=250)

keyboard_plus = Button(text='+',font='맑은고딕 20')
keyboard_plus.place(x=50, width=50, height=50, y=250)

keyboard_result = Button(text='=',font='맑은고딕 20')
keyboard_result.place(x=150,y=250,width=50,height=50)

#입력창
result_screen = StringVar(adder, )
    
#마지막
adder.mainloop()