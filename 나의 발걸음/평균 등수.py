#여러명 국영수 성적 입력하면 평균나오는거랑 배열써서 등수 나오는것두 해보고

import random
lt = []
plus = 0
print('입력할 숫자의 수를 알려주세요')
randomA = int(input())
for f in range(randomA):
    lt.append(int(input()))
    plus += lt[f]
k = int(plus)/int(randomA)
print('평균은 ', round(k,1))
 