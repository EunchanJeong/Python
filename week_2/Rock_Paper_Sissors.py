# 가위바위보게임

import random

game = ("가위", "바위", "보")

result = [["무승부" , "승", "패"],       # row = player, colum = computer                                       
             ["패", "무승부", "승"],        #( 컴퓨터 기준으로 승, 패 결과를 보여주는 리스트) 
             ["승", "패", "무승부"]]        


print("가위바위보 게임")
print("")

computer_win, computer_lose = 0, 0
player_win, player_lose = 0, 0


round = 0

while True:
    round += 1
  
    print("(라운드 {0})".format(round))
    print("")
    
    com_choice = random.randint(0, 2)         # 0~2중 하나를 고른다.
    
    print("컴퓨터가 결정했습니다.")
    print("")

    player = input("무엇을 내시겠습니까? ({0}, {1}, {2}) ".format(game[0], game[1], game[2]))
    print("")

    print("컴퓨터는 ", game[com_choice], " 당신은 ", player, ", ", sep = "", end ="")

    if player == game[0]:
        player = 0
    elif player == game[1]:
        player = 1
    else:
        player = 2

    if result[player][com_choice] == "승":         # 컴퓨터가 이겼으므로 컴퓨터 1승, 당신 1패
        print("컴퓨터가 이겼습니다.")
        print("")
        computer_win += 1
        player_lose += 1
        
    elif result[player][com_choice] == "패":      # 컴퓨터가 패했으므로 컴퓨터 1패, 당신 1승
        print("당신이 이겼습니다")
        print("")
        computer_lose += 1
        player_win   += 1
    else:
        print("무승부입니다.")                            # 무승부
        print("")

    print("컴퓨터 : ", computer_win, "승 ", computer_lose, "패,  ", sep = "", end = "")
    print("당신 : ", player_win, "승 ", player_lose, "패", sep = "")
    print("")

    if computer_win == 3 or player_win == 3:      # 3승을 하면 경기를 마친다.
        print("경기를 마칩니다.")
        break
