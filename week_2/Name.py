# 2. 자기소개서 이름 추출

while True:

    sentence = input("문장을 입력하세요 : ")

    if sentence == '종료':     # '종료'를 입력하면 반복문이 멈춘다. 
        break
    word = sentence.split()

    if len(word) >=2:
        if word[0] == '저는':            # '저는'과 '제 이름은'을 구분한다.
            if word[2] == '합니다.':    # '합니다'와 '이라고 합니다'를 구분한다.   
                temp = word[1]
                name = temp[0:len(temp)-3]    #슬라이싱을 통해 이름을 추출한다.
            else:
                temp = word[1]
                name = temp[0:len(temp)-4]
        else:
            temp = word[2]
            name = temp[0:len(temp)-4]
            
    print("이름 :", name)
