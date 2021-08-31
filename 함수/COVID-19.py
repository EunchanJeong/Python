# 코로나 확진자 통계

"""
사용자는 지역별 확진자 수를 입력한다.

ex)
23 0 2 10 0 7 0 0 28 14 0 1 3 0 5 3 0
"""

def count_COVID_19(cities, yesterday, today):  # 도시별 어제와 오늘의 확진자 수를 보여주는 함수

    print("%s"% "   " , end = '')
    for i in cities:     # 도시별 이름을 출력한다.
        print("\t%4s"% i, end = '')
    print()

    print("%2s" % "어제", end = '')
    for i in yesterday:             # 어제의 확진자 수를 출력한다.
        print("\t%5s"%str(i), end = '')

    print()

    print("%2s" % "오늘", end='')
    for i in today:           # 오늘의 확진자 수를 출력한다.
        if i == max(today):
            print("\t%5s"%('(' + str(i) + ')'), end = '')     # 도시중 가장 많은 확진자 수에 괄호를 붙여준다.
        else:
            print("\t%5s"%str(i), end ='')
    print()

    return today

def count_change(yesterday, today):   #도시별 변동(오늘-어제)의 수를 보여주는 함수

    change = []

    for i in range(len(today)):
        change.append(today[i]-yesterday[i])

    print("%2s" % "변동", end = '')
    for i in change:           # 변동의 수를 출력한다.
        if i > 0:
            print("\t%5s"%('+' + str(i)), end = '')
        else:
            print("\t%5s"%str(i), end = '')
    print()


def count_total(total, today):     # 도시별 확진자 수의 총합을 보여주는 함수

    for i in range(len(today)):
        total[i] += today[i]

    print("%s" % "누계", end='')

    for i in total:            # 확진자의 총합을 출력한다.
        if i == max(total):
            print("\t%5s"%('(' + str(i) + ')'), end = '')  # 도시중 가장 많은 총합에 괄호를 붙여준다.
        else:
            print("\t%5s"%str(i), end ='')
    print()

    return total


cities = ['서울', '부산', '대구', '인천', '광주', '대전', '울산', '세종', '경기', '강원',
          '충북', '충남', '전북', '전남', '경북', '경남', '제주']

total = [0 for i in range(len(cities))]
yesterday = [0 for i in range(len(cities))]

while True:
    today = input()    # 도시별 확진자 수를 입력해준다.

    while True:
        if today == '-1':
            break
        else:
            today = today.split()

        if len(today) != len(cities):
            print("개수(총 17개)가 부족한 입력 : %d개의 데이터만 입력되었습니다." % len(today))
            today = input()
        else:
            for i in range(len(today)):
                today[i] = int(today[i])
            break

    if today == '-1':  # -1을 입력하면 종료된다.
        break

    new_yesterday = count_COVID_19(cities, yesterday, today)    # 도시별 어제와 오늘의 확진자 수를 출력한다.
    count_change(yesterday, today)                              # 도시별 어제와 오늘의 변동(오늘-어제)을 출력한다.
    total = count_total(total, today)                           # 도시별 확진자수의 총합을 출력한다.
    
    yesterday = new_yesterday
