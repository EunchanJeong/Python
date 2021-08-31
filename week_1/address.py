# 리스트에서 데이터 찾기

address = ['모현읍', '문형리', '분당동', '서현동', '규동']

while True:
    str1 = input("동을 입력하세요. ")

    if str1 == '종료':
        print("종료합니다.")
        break
    
    if str1 in address:
        print(address.index(str1)+1, "번째 동입니다.", sep ="")
    else:
        print("새로운 동명입니다. ", len(address)+1, "번째 동으로 등록합니다.", sep="")
        address.append(str1)
