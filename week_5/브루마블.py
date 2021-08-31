# 3.우리의 마블

import random

class Player:   # 플레이어 클래스

    def __init__(self, name): # 플레이어 객체 초기값

        self.name = name           # 플레이어 이름
        self.balance = 5000        # 초기 잔액
        self.location = 0          # 초기 위치
        self.result = ""           # 결과

    def what_name(self):    # 이름을 리턴한다.
        return self.name
    
    def throw_dice(self):   # 주사위를 던지고 위치를 최신화한다.
        num = random.randint(1, 6)

        print("%s got %d" % (self.name, num))

        self.location += num

        if self.location >= 10:
            self.location -= 10

        return self.location

    def how_balance(self):    # 잔액을 리턴한다.
        return self.balance

    def buy_city(self, city):    # 도시를 구매한다. 잔액에서 300원을 빼준다.
        self.balance -= 300

    def pay_fee(self):           # 통행료를 지불한다. 잔액에서 600원 빼준다.
        self.balance -= 600

    def get_fee(self):          # 통행료를 얻는다. 잔액에서 600원을 더해준다.
        self.balance += 600

    def lose(self, value):      # 졌을 때 결과를 저장한다.
        self.result = "lose"

    def what_result(self):   # 게임결과를 리턴한다.
        return self.result


class City:     # 도시 클래스
    
    def __init__(self, name):  # 초기값

        self.name = name           # 도시이름
        self.owner = None          # 초기 주인 (없음)
        self.owner_name = ""       # 초기 주인의 이름 (없음)

        self.map_name = name       # 지도에 표시할 이름

    def what_name(self):   # 도시이름을 리턴한다.
        return self.name

    def isEmpty(self):      # 주인의 유무를 알려준다.
        if self.owner == None:
            print("%s(empty)" % (self.name))
            return True
        else:
            print("%s(%s)" % (self.name, self.owner_name))
            return False

    def buyed(self, player):    # 도시가 구매되어졌을 때 주인과 주인이름을 저장한다.
        self.owner = player
        self.owner_name = player.what_name()

        self.map_name = str(self.name + "(" + self.owner_name + ")" ) # 지도이름을 최신화한다.

    def who_owner(self):    # 주인의 이름을 리턴한다.
        return self.owner_name

    def get_fee(self):   # 통행료를 얻는다.
        self.owner.get_fee()

    def write_map_name(self):    # 지도에 표시할 이름을 리턴한다.
        return self.map_name




def play_game(player, city):  # 게임을 하는 함순
    
    if city == "start":  # 플레이어가 start에 위치했을 때
        print("%s is at *start*" % (player.what_name()))
        
    else:  # 플레이어가 도시에 위치했을 때
        if city.isEmpty() == True:     # 도시에 주인이 없을 때
            
            if player.how_balance() > 300:   # 플레이어가 도시를 살 정도의 잔액이 남아있을 때
                print("%s buys %s" % (player.what_name(), city.what_name()))
                player.buy_city(city)
                city.buyed(player)
                
            else:  # 도시를 살 수 없을 때
                print("can't buy %s" % city.what_name())
                
        else:    # 도시에 주인이 있을 때
            if city.who_owner() != player.what_name():   # 플레이어가 도시의 주인이 아닐 때
                player.pay_fee()
                city.get_fee()
 

    print("%s's balance is %d" % (player.what_name(), player.how_balance()))   # 플레이어의 잔액을 보여준다.

    if player.how_balance() <= 0:  # 플레이어가 잔액을 모두 소진했을 때
        player.lose('lose')

def draw_map(p1_move, p2_move, map):
    x1 = p1_move
    x2 = p2_move
    m = map

    print("~~지도~~")
    for i in range(5, 10):
        tmp = m[i].write_map_name()

        if x1 == i:
            tmp += "*위치:p1*"
        if x2 == i:
            tmp += "*위치:p2*"

        if i != 9:
            print("[%s]\t" % (tmp), end='')
        else:
            print("[%s]" % (tmp))

    for i in range(4, 0, -1):
        tmp = m[i].write_map_name()
        if x1 == i:
            tmp += "*위치:p1*"
        if x2 == i:
            tmp += "*위치:p2*"
        print("[%s]\t\t" % (tmp), end='')

    tmp = m[0]
    if x1 == 0:
        tmp += "*위치:p1*"
    if x2 == 0:
        tmp += "*위치:p2*"
    print("[%s]\t" % (tmp))


print("-----------------------------------------------")

map = []   # 지도 리스트

# 플레이어 객체를 생성한다.
p1 = Player("player 1")
p2 = Player("player 2")

map.append("start")

# 도시 객체들을 생성하고 지도에 저장한다.
seoul = City("seoul")
map.append(seoul)

tokyo = City("tokyo")
map.append(tokyo)

sydney = City("sydney")
map.append(sydney)

LA = City("LA")
map.append(LA)

cairo = City("cairo")
map.append(cairo)

phuket = City("puket")
map.append(phuket)

newdelhi = City("newdelhi")
map.append(newdelhi)

hanoi =  City("hanoi")
map.append(hanoi)

paris = City("paris")
map.append(paris)

count = 0

while True:
    count += 1

    if count > 30:
        break

    print("(Turn %d)" % count)
    print()

    p1_move = p1.throw_dice()   # p1이 주사위를 던진다. (p1의 위치를 리턴받는다.)
    c1 = map[p1_move]    # p1이 위치한 도시

    play_game(p1, c1)   # 게임을 한다.
    print()

    p2_move = p2.throw_dice()   # p2가 주사위를 던진다. (p2의 위치를 리턴받는다.)
    c2 = map[p2_move]    # p2가 위치한 되시

    play_game(p2, c2)   # 게임을 한다.
    print()

    draw_map(p1_move, p2_move, map)

    if p1.what_result() == "lose":   # p1이 졌을 때
        print()
        print("p1 : lose")
        print("p2 : win")
        print("-----------------------------------------------")
        break
    elif p2.what_result() == "lose":   # p2가 졌을 때
        print()
        print("p1 : win")
        print("p2 : lose")
        print("-----------------------------------------------")
        break

    print("-----------------------------------------------")
