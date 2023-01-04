import random as rm
a = rm.randrange(1, 100)
#print(a) #정답확인용

while True:
    b = input()
    if int(a) < float(b):
        print('down')
    elif int(a) > float(b):
        print('up')
    else:
        print('answer')
        break