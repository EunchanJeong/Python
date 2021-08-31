# 2. 끝말 잇기

f = open('dict_test_utf8.TXT', 'r', encoding = 'utf-8')
dic = {}

while True:
    line = f.readline()    # dict_test_utf8.TXT 파일을 읽는다.

    if not line:
        break

    word, mean = line.split(' :')    # 단어와 뜻을 분리한다.
    mean = mean.replace(mean[0], '')
    mean = mean.replace('\n', '')

    dic[word] = mean     # 단어와 뜻을 딕셔너리에 저장한다.

f.close()

same_words = []   # 중복된 단어를 찾기위한 리스트
pre_word = 'apple'
same_words.append(pre_word)

while True:
    start_alphabat = pre_word[len(pre_word)-1].lower()   # 전 단어의 끝 알파벳

    input_word = input("%s 끝말잇기? " % pre_word)

    if input_word == '0':                  # 0을 입력하면 종료된다.
        print("끝말 잇기를 종료합니다.")
        break

    if len(input_word) > 5:      # 단어의 길이가 5보다 클 때
        print("단어가 길어요(%s 의 끝말을 이으세요)." % pre_word)
        print()
    elif len(input_word) < 5:   # 단어의 길이가 5보다 작을 때
        print("단어가 짧아요(%s 의 끝말을 이으세요)." % pre_word)
        print()
    else:       # 단어의 길이가 5일 때
        if input_word[0].lower() != start_alphabat:   # 단어가 끝말과 다를 떄
            print("끝말과 다른 단어입니다(%s 의 끝말을 이으세요)." % pre_word)
            print()
        elif dic.get(input_word) == None:    # 단어가 사전에 없을 때
            print("사전에 없는 단어입니다(%s 의 끝말을 이으세요)." % pre_word)
            print()
        elif dic[input_word].find('n.') == -1:   # 단어가 명사가 아닐 때
            print("명사가 아닙니다.(%s 의 끝말을 이으세요)"% pre_word)
            print()
        elif input_word in same_words:      # 단어가 중복일 때
            print("중복된 단어입니다(%s 의 끝말을 이으세요)." % pre_word)
            print()
        else:      # 단어가 정답일때
            print("정답입니다.(%s 의 끝말을 이으세요)." % input_word)
            print()
            same_words.append(input_word)
            pre_word = input_word