# 구구단을 외자

import time
import random

def multiply_quiz(score):   # 구구단 문제를 만들고 문제풀이 시간을 재는 함수

    num1 = random.randint(1, 9)
    num2 = random.randint(1, 9)

    print("%d * %d = " % (num1, num2), end = '')
    quiz_time = time.time()    # 문제 출제 시간

    user_input = int(input())
    input_time = time.time()    # 답 입력 시간

    solve_time = int((input_time - quiz_time)*1000)/1000    # 문제 풀이 시간

    if solve_time >= 3:   # 제한시간이 지났을 때
        print("(제한시간이 지났습니다) %.3f초 소요 : Score = %d" % (solve_time, score))
    else:
        if user_input == num1 * num2:    # 답이 맞았을 때
            score += int(3000 - (solve_time * 1000))
            print("(맞았습니다.) %.3f초 소요 : Score = %d" % (solve_time, score))

        else:  # 답이 틀렸을 때
            print("(틀렸습니다.) %.3f초 소요 : Score = %d" % (solve_time, score))

    return score


max_score = 0   # 최고 점수
round = 0      # 라운드

while True:
    round += 1
    print("(%d 라운드)" % round)
    print("구구단을 외자. 문제출력 후 3초 이내에 입력하세요.")
    score = 0
    for i in range(10):  # 문제 출제 및 풀이 시간 측정
        print(i+1, ") ", sep = '', end = '')
        score = multiply_quiz(score)

    if (round != 1) and (score > max_score):   # 최고점을 얻었을 때
        max_score = score
        print("---최고 기록 갱신---")
    print()


