# 2 ~ 100000 사이의 소수 개수 세기

import time

start = time.time()                     # 현재 시간 측정

n = 100000
num = [False, False] + [True]*(n-1)

prime_count = 0

for i in range(2, n+1):
    if num[i] == True:                 # num[i]가 True이면 소수이다.
        prime_count += 1

        for j in range(2*i, n+1, i):  # num[i]가 소수일 때 num[i]의 배수들을 False로 바꾼다.
            num[j] = False
        
end = time.time()                     # 현재 시간 측정

print(prime_count, "개")
print("수행시간: ", end - start, "초", sep = "")


