# 2.계산기 만들기

class Calc:
    def __init__(self, value = 0):  # 초기값
        self.value = value

    def setValue(self, num):  # 값 설정
        self.value = num

    def getvalue(self):     # 값 리턴
        return self.value

    def add(self, num):     # 더하기
        self.value = self.value + num

    def minus(self, num):   # 빼기
        self.value = self.value - num

    def print(self):        # 값 출력
        print(self.value)


cal1 = Calc()       # 객체 생성
cal2 = Calc(5)      # 5를 초기화하여 객체 생성
cal1.setValue(10)   # 10 설정
cal1.add(20)        # 20 더하기
cal1.minus(5)       # 5 빼기
cal1.print()        # 값 표시하기
cal2.add(cal1.getvalue())  # cal1의 값을 cal2에 더하기
cal2.print()        # 값 표시하기