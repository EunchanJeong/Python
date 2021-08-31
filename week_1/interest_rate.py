# 5. 이자 원금 계산하기

money  = int(input("원금을 입력하세요(원). "))
interest_rate = int(input("금리를 입력하세요(%). "))

print("원금 ", money, "원   금리 ", interest_rate, "% 입니다.", sep = "")

print("기간       합계")

for i in range(20):
    year = i + 1
    total = money * (1+ (interest_rate * 0.01))**year    #총액

    if (year / 10) < 1:
        print(year, "년      ", '%.1f' % total, sep="")
    else:
       print(year, "년    ", '%.1f' % total, sep="") 
