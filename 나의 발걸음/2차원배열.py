a,b = map(int, input().split())
c = int(input())

b += c // 60
a += c % 60
    
print(a, b)