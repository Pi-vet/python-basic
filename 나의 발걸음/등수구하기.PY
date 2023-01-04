lt = []
name = []
print('입력할 숫자의 수를 알려주세요')
CountN = int(input())
A = CountN

for f in range(CountN):
    lt.append(int(input('숫자를 입력해주세요.\n')))
    lt.sort(reverse=True)
    if int(CountN) == 1:
        print(lt)
    CountN = CountN - 1
    
B = A - 1
C = int(A) - int(B)
for i in range(A):
    print(C, '등')
    C = C + 1
    #name.append(input('이름을 입력해주세요.'))

#while CountN != 0:
    #Max1 = list.index(max(lt))
    #prirnt(Max1)