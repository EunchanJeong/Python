# 5. 숫자 표시

han1 = ["","일","이","삼","사","오","육","칠","팔","구"]
han2 = ["","십","백","천"]
han3 = ["","만","억"]

while True:
    num = int(input("숫자는? "))

    if num == 0:        # 0을 입력하면 종료한다.
        break
    
    print(format(int(num), ','))      # format함수를 사용하여 천단위로 ","를 표시한다.
    
    num = str(num)
    save_han = []
    result = ''
    for i in reversed(range(len(num))):
        if han1[int(num[len(num)-i-1:len(num)-i])] == "일" and (len(num)-i) != len(num):  # 십단위이상의 1을 구분한다.
            save_han.append(han1[0])
        else:
            save_han.append(han1[int(num[len(num)-i-1:len(num)-i])])
    
        if int(num[len(num)-i-1:len(num)-i]) > 0:   # 백단위이상 숫자를 구분한다.
            save_han.append(han2[i%4])
            
        if i%4 == 0:                # 만단위이상 숫자를 구분한다.
            save_han.append(han3[i//3])
            
    for i in save_han:
        result  += i

    if result[0] == "억":
        result = "일" + result
    
    print(result)

