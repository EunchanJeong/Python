# 득표율 그래프 그리기

import matplotlib.pyplot as plt


input_file = open("elec.csv", 'r', encoding='utf-8')   # 선거 파일을 읽는다.
csv_line = input_file.readline()
csv_line = input_file.readline()
csv_line = csv_line[:-1]

values = csv_line.split(',')

input_file.close()

plt.figure(1, figsize=(8, 8))
ax = plt.axes([0.1, 0.1, 0.8, 0.8])

labels = 'Gildong Hong', 'Gamchan Kang', 'Sunsin Lee', 'Cheong Shim', 'Children Park'
explode =[0.1, 0.1, 0.1, 0.1, 0.1]

plt.pie(values, explode = explode, labels = labels, autopct = '%.1f%%', startangle=67)
plt.title('20th election')

plt.show()    # 파이그래프를 그린다.

