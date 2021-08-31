# 전화번호부

tel = {'홍길동': '010-4444-5555', '김중앙': '010-9191-8181', '심청': '010-3232-5454'}

while True:

    name = input("이름>> ")

    if name == '종료':     # 종료
        break
    
    if (name in tel) == True:                # 전화번호부에 이름이 있을 때
        print(name, tel.get(name))
        
    elif name == "add":                      # 전화번호부에 사람을 추가할 때
        new_name = input("이름은? ")
        new_number = input("전화번호는? ")
        tel[new_name] = new_number
        print(new_name, "전화번호가 추가되었습니다.")
        
    elif (name in tel) == False:          # 전화번호부에 이름이 없거나 정확히 입력이 되지 않았을 때   
        exist_name = False
        saved_name = list(tel.keys())
        divided_name = []
        
        for i in range(len(saved_name)):    # 전화번호부에 있는 이름들을 쪼개준다.
            div_1 = []
            count = len(saved_name[i])
            while True:
                if count == -1:
                    break
                for j in range(len(saved_name[i])):
                    temp = saved_name[i]

                    if len(temp[j:j+(count+1)]) == count+1:
                        div_1.append(temp[j:j+(count+1)])
                        
                count -= 1
            divided_name.append(div_1)

        for i in range(len(divided_name)):
            if name in divided_name[i]:
                print(saved_name[i], tel.get(saved_name[i]))  # 전화번호부에 비슷한 이름이 있을 때
                exist_name = True
                
        if exist_name == False:         # 전화번호부에 이름이 없을 때
            print("찾을 수 없습니다.")


    
