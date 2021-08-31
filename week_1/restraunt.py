# 2. 식당 메뉴표

menu =[['noodle', 500], ['ham', 200], ['egg', 100], ['spaghetti', 900]]

while True:
    print("안녕하세요 다음의 메뉴 중 원하는 메뉴를 선택하세요")

    print("(", end = "")
    
    for i in range(len(menu)):
        print(menu[i][0],", ", sep = "", end ="")

        if i == len(menu)-1:
          print(menu[i][0],") ", sep = "", end ="")

    choice = input()                     # 음식명 입력

    Have_MENU = False                # 메뉴 유무 판단을 위한 변수

    if choice == '종료':
        print("종료합니다.")
        break

    for i in range(len(menu)):          # 메뉴가 있을 때
        if  choice in menu[i][0]:
            print(menu[i][1], "원입니다.", sep="")
            print("")
            Have_MENU = True
            break
    
    if Have_MENU == False:          # 메뉴가 없으면
        print("그런 메뉴는 없습니다.")
        print("")

