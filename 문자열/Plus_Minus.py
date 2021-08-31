# 수식 계산기

while True:

    cal = input("수식을 입력하세요 : ")

    if cal == "종료":     # '종료'를 입력하면 반복문이 멈춘다.
        break
    
    num = []
    operator = ''
    
    n = ''
    
    for i in range(len(cal)):
        if cal[i] == '+' or cal[i] == '-':     # 문자열이 연산자인 경우
            num.append(int(n))
            n = ''
            
            if operator == '':
                operator = cal[i]
            else:
                n1=num[0]
                n2 = num[1]

                del num[1]
                del num[0]

                if operator == '+':
                    num.append(n1+n2)
                else:
                    num.append(n1-n2)
                operator = cal[i]
        else:                           # 문자열이 연산자가 아닌 경우
            n += cal[i]

            if i == len(cal)-1:
                num.append(int(n))

                n1=num[0]
                n2 = num[1]

                del num[1]
                del num[0]

                if operator == '+':
                    num.append(n1+n2)
                else:
                    num.append(n1-n2)
                    
    print("결과는 {0}".format(num[0]))

    
        

       
            
