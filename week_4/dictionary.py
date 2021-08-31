
f = open('dict_test_utf8.TXT', 'r', encoding = 'UTF8')
dic = {}
i = 1

while True:
    line = f.readline()

    if not line:
        break

    word, mean = line.split(' :')
    mean = mean.replace(mean[0], '')
    mean = mean.replace('\n', '')

    dic[word] = mean

f.close()

while True:
    user_input = input("단어? ")
