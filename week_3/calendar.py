# 달력

def isLeafYear(year): # 윤년인지 알려주는 함수
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def lastDay(year, month):  # 달의 마지막 날짜를 알려주는 함수
    month_lastDay = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if isLeafYear(year) == True:  # 윤년일 때
        month_lastDay[1] = 29

    return month_lastDay[month-1]

def totalDay(year, month, day):  # 1년 1월 1일 부터 지나온 날짜의 합을 알려주는 함수
    total = (year-1) * 365 + (year-1) // 4 - (year-1) // 100 + (year - 1) // 400

    for i in range(1, month):
        total += lastDay(year, i)
    return total + day

def weekDay(year, month, day):  # 요일를 숫자로 리턴하는 함수
    return totalDay(year, month, day) % 7

def draw_calendar(year, month):  # 달력을 출력해주는 함수
    print('\tSUN\tMON\tTUE\tWED\tTUR\tFRI\tSAT')

    for i in range(weekDay(year, month, 1)):
        print('\t', end='')

    for i in range(1, lastDay(year, month)+1):
        print('\t%d' %i, end = '')

        if weekDay(year, month, i) == 6 and lastDay(year, month) != i:
            print()


year = 0
month = 0
while True:
    year, month = input("달력? ").split()
    year = int(year)
    month = int(month)

    if year >= 1921 and year <= 2200:
        break
    else:
        print("1921년 1월부터 2200년 12월까지 달력을 표시할 수 있습니다.")
        print("다시 입력해주세요.")
        print()

draw_calendar(year, month) # 달력을 그려준다.