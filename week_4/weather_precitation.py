# 3. 기후 분석

def split_year_and_month(user_info):  # 파일의 날짜를 일을 제외하고 해와 월만 표시하는 함수
                                      # 그리고 파일에 저장된 해들을 리스트에 저장해준다.
    if len(user_info[0][2]) == 2:
        years = []

        for i in range(len(user_info)):
            if user_info[i][2][0] not in years:
                years.append(user_info[i][2][0])
        return user_info, years
    years = []
    tmp_info = user_info
    for i in range(len(tmp_info)):
        x = str(user_info[i][2]).split('-')
        x = x[:-1]
        tmp_info[i][2] = [int(x[0]), int(x[1])]
        if int(x[0]) not in years:
            years.append(int(x[0]))
    return tmp_info, years

def average_temp(user_info, years):    # 해의 월별로 평균 기온을 계산하는 함수

    avg_temp = []    # 해의 월별로 평균 기온을 저장하기위한 리스트

    for i in years:
        for j in range(12):
            sum = 0
            day = 0
            for k in range(len(user_info)):
                if user_info[k][2][0] == i and user_info[k][2][1] == j+1:
                    sum += float(user_info[k][3])
                    day += 1
            if day != 0:
                avg_temp.append([i, j+1, sum/day])

    return avg_temp

def sum_precipitation(user_info, years):    # 해의 월별로 강수량을 계산하는 함수

    avg_precipitation = []    # 해의 월별로 평균 강수량을 저장하기위한 리스트
    for i in years:
        for j in range(12):
            sum = 0
            day = 0
            for k in range(len(user_info)):
                if user_info[k][2][0] == i and user_info[k][2][1] == j+1:
                    sum += float(user_info[k][6])
                    day += 1
            if day != 0:
                avg_precipitation.append([i, j+1, sum])

    return avg_precipitation

def make_total(user_temp, user_precipitation): # 해의 월별 평균기온과 강수량를 합쳐주는 함수

    total = []
    for i in range(len(user_temp)):
        if user_temp[i][0] == user_precipitation[i][0] and user_temp[i][1] == user_precipitation[i][1]:
            total.append([user_temp[i][0], user_temp[i][1], user_temp[i][2], user_precipitation[i][2]])

    return total

def print_total(province_name, user_total):   # 해의 월별 평균 기온과 강수량을 출력하는 함수

    if len(province_name) >= 4:
        print("[%4s 기후 분석]\t[평균 기온]\t[평균 강수량(mm)]" % province_name)

        for i in range(len(user_total)):
            print(" %d년 %2d월\t\t\t %5.1f\t\t\t%5.1f" % (user_total[i][0], user_total[i][1], user_total[i][2], user_total[i][3]))
        print("___________________________________________________________________________________")
        print()
    else:
        print("[%s 기후 분석]\t[평균 기온]\t[평균 강수량(mm)]" % province_name)

        for i in range(len(user_total)):
            print(" %d년 %2d월\t\t %5.1f\t\t\t%5.1f" % (user_total[i][0], user_total[i][1], user_total[i][2], user_total[i][3]))
        print("___________________________________________________________________________________")
        print()

f = open("Weather.csv", 'r', encoding='utf-8')

csv_line = f.readline()

info = []
province_codes = []     # 지역 코드를 저장할 리스트
province_names = ["서울", "부산", "대구", "광주", "인천", "대전", "울산", "경기도", "강원도",
                 "충청북도", "충청남도", "전라북도", "전라남도", "경상북도", "경상남도", "제주도"]

while True:
    csv_line = f.readline()
    csv_line = csv_line[:-1]

    if csv_line == '':
        break
    csv_line = csv_line.split(',')
    info.append(csv_line)
    code = csv_line[0]
    if code not in province_codes:
        province_codes.append(code)

while True:
    print("(1:Seoul, 2.Pusan, 3:Daegu, ..... , 15: Gyeongsangnam-do, 16: Jeju-do, exit: 종료)")
    user_input = input("*** 도시를 선택하세요: ")

    while True:
        if user_input != "exit" and user_input.isdigit() == False:
            print("잘못 입력하셨습니다. 다시 입력해주세요.")
            print("___________________________________________________________________________________")
            print()
            print("(1:Seoul, 2.Pusan, 3:Daegu, ..... , 15: Gyeongsangnam-do, 16: Jeju-do, exit: 종료)")
            user_input = input("도시를 선택하세요: ")
        elif user_input != "exit" and (int(user_input) < 0 or int(user_input) > 16):
            print("잘못 입력하셨습니다. 다시 입력해주세요.")
            print("___________________________________________________________________________________")
            print()
            print("(1:Seoul, 2.Pusan, 3:Daegu, ..... , 15: Gyeongsangnam-do, 16: Jeju-do, exit: 종료)")
            user_input = input("도시를 선택하세요: ")
        else:
            break

    if user_input == "exit":  # exit를 입력하면 종료된다.
        print("종료합니다.")
        break
    else:
        user_input = int(user_input)

    user_info = []

    for i in range(len(info)):
        if province_codes[user_input-1] == info[i][0]:    # 입력된 지역의 코드와 info리스트에 저장된 코드가 같으면
            user_info.append(info[i])

    changed_info, years = split_year_and_month(user_info)  # 날짜를 제외하고 해와 월만 표시해주고 파일에 저장된 해들을 리턴받는다.


    user_temp = average_temp(changed_info, years)       # 해의 월별 평균 기온을 리스트로 리턴받는다.
    user_precipitation = sum_precipitation(changed_info, years)  # # 해의 월별 강수량을 리스트로 리턴받는다.

    user_total = make_total(user_temp, user_precipitation)       # 해의 월별 평균기온과 강수량 합친 리스트를 리턴받는다.
    name = province_names[user_input-1]

    print_total(name, user_total)        # 해의 월별 평균기온과 강수량을 출련한다.

