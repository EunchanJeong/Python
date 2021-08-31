# 3. 내림차순 출력

print("데이터를 입력하세요(입력을 마치려면 0을 입력하세요)")

num = []

while True:
    
    a = int(input())

    if a == 0:                  # 0을 입력시 입력종료
        break
    else:
        num.append(a)

num.sort()
num.reverse()

print("결과 : ", end="")

for i in range(len(num)):
    if i == len(num)-1:
        print(num[i], " (", len(num), "개)", sep ="")
    else:
        print(num[i], " ", end="")
