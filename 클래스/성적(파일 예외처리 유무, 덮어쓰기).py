# 성적, 예외처리, 덮어쓰기

import os.path

def cal_score(score_list):   # 점수의 합, 평균 그리고 석차를 계산하는 함수
    info = score_list
    sum = []
    rank = []

    for i in range(len(info)):    # 총합과 평균을 구하여 리스트에 저장한다.
        tmp = 0
        for j in range(1, 4):
            tmp += int(info[i][j])
        info[i].append(tmp)
        info[i].append(tmp/3)
        sum.append(tmp)

    for i in range(len(sum)):    # 석차를 구한다.
        r = 1
        for j in range(len(sum)):
            if sum[i] < sum[j]: r += 1
        rank.append(r)

    for i in range(len(info)):
        info[i].append(rank[i])

    return info

def write_file(score_list,file):  # 파일을 쓰는 함수
    info = score_list

    f = open(file, 'w', encoding='utf-8')

    f.write("    학번\t\t국어\t영어\t수학\t총점\t평균\t석차\n")
    f.write("======================================================\n")

    for i in range(len(info)):
        f.write("%s\t %s\t%s\t%s\t%3d\t%.1f\t %2d\n" % (info[i][0], info[i][1], info[i][2], info[i][3], info[i][4], info[i][5], info[i][6]))

    f.close()

def equal_check(name, file_name):   # 파일이름을 정확히 입력했는지 확인하는 함수
    if name != file_name:
        raise Exception("파일이름을 잘못입력하셨습니다.")

user_input = ''
file_name = 'score.csv'  # 입력 받을 파일 이름: score.csv
input_file = None

while True:
    while True:
        print("파일이름을 입력하세요 (exit:종료)")
        user_input = input("입력: ")
        print()

        if user_input == 'exit':
            break
        try:
            equal_check(user_input, file_name)    # 파일이름을 정확히 입력했는지 확인한다.
            input_file = open("%s" % file_name, 'r', encoding='utf-8')

        except FileNotFoundError:    # 파일이 존재하지 않을 때
            print("파일이 존재하지 않습니다.")
            print()

        except Exception as e:    # 파일이름을 잘못입력했을 때
            print(e)
            print()

        else:
            break

    if user_input == 'exit':
        print("종료합니다.")
        break

    student_score = []

    while True:
        csv_line = input_file.readline()
        csv_line = csv_line[:-1]

        if csv_line == '':
            break
        csv_line = csv_line.split(',')
        student_score.append(csv_line)
        code = csv_line[0]

    input_file.close()

    output_file = "report.txt"

    if os.path.isfile(output_file) == True:   # 같은 이름의 파일이 존재할 때
        print("같은 이름의 파일이 존재합니다.")
        choice = input("덮어쓰기를 하겠습니까? (Y/N) ")
        print()

        if choice.upper() == "Y":
            student_info = cal_score(student_score)
            write_file(student_info ,output_file)
            print("%s 덮어쓰기 완료" % output_file)
            print()
        else:
            print("덮어쓰지 않습니다.")
            print()

    else:       # 같은 이름의 파일이 존재하지 않을 때
        student_info = cal_score(student_score)
        write_file(student_info, output_file)
        print("%s 저장 완료" % output_file)
        print()


