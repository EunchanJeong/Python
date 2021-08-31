# 기후 분석

import matplotlib.pyplot as plt

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

def draw_graph(Korea_name, English_name, user_total):   # 해의 월별 평균 기온 그래프를 그리는 함수

    year2016, weather2016 = [], []
    year2017, weather2017 = [], []
    year2018, weather2018 = [], []
    year2019, weather2019 = [], []
    year2020, weather2020 = [], []

    for i in range(len(user_total)):
        if user_total[i][0] == 2016:
            year2016.append(user_total[i][1])
            weather2016.append(user_total[i][2])
        elif user_total[i][0] == 2017:
            year2017.append(user_total[i][1])
            weather2017.append(user_total[i][2])
        elif user_total[i][0] == 2018:
            year2018.append(user_total[i][1])
            weather2018.append(user_total[i][2])
        elif user_total[i][0] == 2019:
            year2019.append(user_total[i][1])
            weather2019.append(user_total[i][2])
        elif user_total[i][0] == 2020:
            year2020.append(user_total[i][1])
            weather2020.append(user_total[i][2])

    print("%s의 기온 그래프를 출력합니다." % Korea_name)
    print("다른 지역의 기온 그래프를 보고 싶다면 그래프창을 닫아주세요.")
    print()

    plt.figure(figsize=(10, 6))
    plt.plot(year2016, weather2016, label = '2016')
    plt.plot(year2017, weather2017, label = '2017')
    plt.plot(year2018, weather2018, label = '2018')
    plt.plot(year2019, weather2019, label = '2019')
    plt.plot(year2020, weather2020, label = '2020')
    plt.xlabel('Month')
    plt.ylabel('Temperatures')
    plt.title(English_name)
    plt.legend(loc='lower right')
    plt.show()


def draw_ALL_graph(data): # 전지역의 월별 기온 그래프를 그리는 함수
    all_list = []

    for i in range(len(data)):
        tmp = []
        for j in range(len(data[i][2])):
            tmp.append(data[i][2][j][2])
        x = [data[i][0], data[i][1], tmp]
        all_list.append(x)

    plt.figure(figsize=(10, 6))
    for i in range(len(all_list)):
        plt.plot(all_list[i][2], label= all_list[i][1])

    plt.ylabel('Temperatures')
    plt.title('ALL GRAPH')
    plt.legend(loc='lower right')
    print("다른 지역의 기온 그래프를 보고 싶다면 그래프창을 닫아주세요.")
    print()
    plt.show()

f = open("Weather.csv", 'r', encoding='utf-8')

csv_line = f.readline()

info = []
province_codes = []     # 지역 코드를 저장할 리스트
province_names = ["서울", "부산", "대구", "광주", "인천", "대전", "울산", "경기도", "강원도",
                 "충청북도", "충청남도", "전라북도", "전라남도", "경상북도", "경상남도", "제주도"]

English_province_names = []

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

    if csv_line[1] not in English_province_names:
        English_province_names.append(csv_line[1])

f.close()

while True:
    print("(1:Seoul, 2.Pusan, 3:Daegu, ..... , 15: Gyeongsangnam-do, 16: Jeju-do, 0: All, exit: 종료)")
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



    if user_input == 0:  # 모든 지역의 그래프를 그리고 싶을 때
        print("정보를 가져오는데 시간이 걸릴 수 있습니다. 잠시만 기다려주세요.")

        ALL_info = []

        while True:  # 지역별로 월별 기온을 구한다.
            user_info = []
            user_input += 1

            if user_input == 17:
                break
            for i in range(len(info)):
                if province_codes[user_input - 1] == info[i][0]:  # 입력된 지역의 코드와 info리스트에 저장된 코드가 같으면
                    user_info.append(info[i])

            changed_info, years = split_year_and_month(user_info)  # 날짜를 제외하고 해와 월만 표시해주고 파일에 저장된 해들을 리턴받는다.

            user_temp = average_temp(changed_info, years)  # 해의 월별 평균 기온을 리스트로 리턴받는다.

            user_precipitation = sum_precipitation(changed_info, years)  # # 해의 월별 강수량을 리스트로 리턴받는다.

            user_total = make_total(user_temp, user_precipitation)  # 해의 월별 평균기온과 강수량 합친 리스트를 리턴받는다.
            Korea_name = province_names[user_input - 1]
            English_name = English_province_names[user_input - 1]

            tmp_list = [Korea_name, English_name, user_total]
            ALL_info.append(tmp_list)

        draw_ALL_graph(ALL_info)    # 모든 지역의 기온 그래프를 그린다.

    else:    # 특정 지역의 그래프를 그리고 싶을 때
        user_info = []
        for i in range(len(info)):
            if province_codes[user_input-1] == info[i][0]:    # 입력된 지역의 코드와 info리스트에 저장된 코드가 같으면
                user_info.append(info[i])

        changed_info, years = split_year_and_month(user_info)  # 날짜를 제외하고 해와 월만 표시해주고 파일에 저장된 해들을 리턴받는다.


        user_temp = average_temp(changed_info, years)       # 해의 월별 평균 기온을 리스트로 리턴받는다.
        user_precipitation = sum_precipitation(changed_info, years)  # # 해의 월별 강수량을 리스트로 리턴받는다.

        user_total = make_total(user_temp, user_precipitation)       # 해의 월별 평균기온과 강수량 합친 리스트를 리턴받는다.
        Korea_name = province_names[user_input-1]
        English_name =  English_province_names[user_input-1]
        draw_graph(Korea_name, English_name, user_total)        # 특정지역의 해의 월별 평균기온을 그래프로 그린다.