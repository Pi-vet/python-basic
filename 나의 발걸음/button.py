from tkinter import *
a = 0
Window = Tk()
Window.title('button')
Window.config(background='black')

def event():
    global a
    a = int(a) + 1
    print(a)
    button['text'] = str(a) + '번 누르셨습니다.'
    
button = Button(Window,text='버튼',font="맑은고딕",width=30, height=30 , command=event)
button.pack(side=TOP,padx=10,pady=10)
Window.mainloop()