# 로또 번호 생성기

import random

def lotto_generator( ):   # 로또번호 생성 함수
    lotto_nums =[]

    for i in range(6):
        while True:
            num = random.randint(1, 45)
            if num not in lotto_nums:
                lotto_nums.append(num)
                break


    return lotto_nums

a = int(input("몇 번째 로또 번호를 고를까요?(1~100) "))

for i in range(a):
    selectednum = lotto_generator()
    print("%3d"%(i+1), "회 : ", selectednum)
    # 앞쪽 로또 번호는 버리고 마지막 로또 번호만 남는다.

print("이번주의 로또 번호입니다. ", end = "")
for i in selectednum:
    print(i, end = " ")