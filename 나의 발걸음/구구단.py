P = 10
X = 1
I = input()

while P != 0:
    if I == '그만':
        print("작동을 멈춥니다")
        break
    print(int(I)*X)
    X = X + 1
    P = P - 1
    if P == 1:
        X = 1
        P = 10
        I = input()
        continue
