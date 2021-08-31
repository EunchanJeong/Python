# 전자사전 만들기

f = open('dict_test_utf8.TXT', 'r', encoding = 'utf-8')
dic = {}

while True:
    line = f.readline()      # dict_test_utf8.TXT 파일을 읽는다.

    if not line:
        break

    word, mean = line.split(' :')  # 단어와 뜻을 나누어 저장한다.

    line = line.replace('\n', '')
    line = line.replace(' :', '')

    dic[word] = line     # 단어를 딕셔너리에 저장한다.

f.close()

while True:
    user_input = input("단어? ")

    if user_input == '0':      # '0'을 입력하면 종료된다.
        print('사전을 종료합니다.')
        break

    if dic.get(user_input) == None:      # 찾는 단어가 사전에 없을 때
        print("단어가 사전에 없습니다.")
        print()
    else:
        print(dic[user_input])
        print()