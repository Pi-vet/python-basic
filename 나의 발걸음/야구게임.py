#1.랜덤숫자 1~9를 뽑는다
#2.중복된수는 다시 랜덤
#3.9번 기회
#4.기회 한번마다 출력 스트라이크(위치 숫자 동일) 볼 (위치틀림) 아웃 (다틀림)
#5 전부 스트라이크면 우승 (게임 끝)

#0
strike = 0
ball = 0
out = 0

#0-1 strike ball out
strikeS1 = 0
strikeS2 = 0
strikeS3 = 0

ballS1 = 0
ballS2 = 0
ballS3 = 0

outS1 = 0
outS2 = 0
outS3 = 0

#0-2 unnecessary function
UF = 0

#1
import random
a = random.randrange(1, 10)
b = random.randrange(1, 10)
c = random.randrange(1, 10)
#print(a, b, c) #확인용

#2
while a == b:
    b = random.randrange(1, 10)
    #print(b) #확인용
    
while a == c:
    c = random.randrange(1, 10)
    #print(c) #확인용
    
while b == c:
    c = random.randrange(1, 10)
    #print(c) #확인용

print("숫자 1부터 9까지의 숫자중 3가지의 숫자가 선택되었습니다.\n3가지의 숫자를 입력 해주십시오")
#3

playcount = 9
print(playcount, "만큼의 기회가 남아있습니다.\n", end='')
while int(playcount) != int(0):
    f1, f2, f3 = input().split()
    if int(f1) > 9:
        print("다시입력해주십시오")
        continue
    if int(f2) > 9:
        print("다시입력해주십시오")
        continue
    if int(f3) > 9:
        print("다시입력해주십시오")
        continue
    #print(f1, f2, f3) #확인용
    if int(f1) == int(a):
        strike = strike + 1
        strikeS1 = strikeS1 + 1
    else:
        if int(f1) == int(b):
            ball = ball + 1
            ballS1 = ballS1 + 1
        else:
            if int(f1) == int(c):
                ball = ball + 1
                ballS1 = ballS1 + 1
            else:
                out = out + 1
                outS1 = outS1 + 1
    if int(f2) == int(b):
        strike = strike + 1
        strikeS2 = strikeS2 + 1
    else:
        if int(f2) == int(a):
            ball = ball + 1
            ballS2 = ballS2 + 1
        else:
            if int(f2) == int(c):
                ball = ball + 1
                ballS2 = ballS2 + 1
            else:
                out = out + 1
                outS2 = outS2 + 1
    if int(f3) == int(c):
        strike = strike + 1
        strikeS3 = strikeS3 + 1
    else:
        if int(f3) == int(b):
            ball = ball + 1
            ballS3 = ballS3 + 1
        else:
            if int(f3) == int(a):
                ball = ball + 1
                ballS3 = ballS3 + 1
            else:
                out = out + 1
                outS3 = outS3 + 1

    print(int(strikeS1) + int(strikeS2) + int(strikeS3), '[S]', int(ballS1) + int(ballS2) + int(ballS3), '[B]')


#                                             [Chaos]     
#    if int(strikeS1) == int(1):
#        if int(strikeS2) == int(1):
#            if int(strikeS3) == int(1):
#                print('S', 'S', 'S')
#        elif int(ballS2) == int(1):
#            if int(strikeS3) == int(1):
#                print('S', 'B', 'S')
#            elif int(ballS3) == int(1):
#                print('S', 'B', 'B')
#    elif int(ballS1) == int(1):
#        if int(ballS2) == int(1):
#            if int(ballS3) == int(1):
#                print('B', 'B', 'B')
#    elif int(outS1) == int(1):
#        if int(outS2) == int(1):
#            if int(outS3) == int(1):
#                print('O', 'O', 'O')

    if int(strike) == int(3):
        print(playcount, "의 기회를 남기고 승리하셨습니다.")
        playcount = 0
    else:
        playcount = int(playcount) -1
        print(playcount, '만큼의 기회가 남아있습니다.\n 신중히 골라주세요.')
        if int(playcount) == 0:
            print('당신은 실패하였습니다.')
            break
    strike = 0
    ball = 0
    out = 0
    strikeS1 = 0
    strikeS2 = 0
    strikeS3 = 0

    ballS1 = 0
    ballS2 = 0
    ballS3 = 0

    outS1 = 0
    outS2 = 0
    outS3 = 0

print('정답은',a, b, c,'이였습니다.')