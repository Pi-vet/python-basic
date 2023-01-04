import random

a = ['가위', '바위', '보']

b = random.choice(a)
#print(b)

c = input()

if b == c:
    print("무승부")
    
if b == '가위':
    if c == '바위':
        print('우승')
    if c == '보':
        print('패배')
        
if b == '보':
    if c == '바위':
        print('패배')
    if c == '가위':
        print('우승')

if b == '바위':
    if c == '가위':
        print('패배')
    if c == '보':
        print('우승')
    
    
        
        