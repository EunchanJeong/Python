# 정규분포의 랜덤값 구하기

import matplotlib.pyplot as plt
import numpy as np
import random

x = []
y1 = []
y2 = []

for i in range(1, 1001):
    x.append(i)

for i in range(1000):  # randint로 랜덤값을 얻는다.
    y1.append(random.randint(0, 100))

while True:  # normal로 랜덤값을 얻는다.
    a = np.random.normal(50, 25, 1)
    if a[0] >= 0 and a[0] <= 100:
        y2.append(a[0])
    if len(y2) == 1000:
        break


fig = plt.figure(figsize=(8, 8))
fig.set_facecolor('white')

plt.hist(y1, 15, density=True, label = 'randint', color='g', alpha=0.75, edgecolor='k')
plt.hist(y2, 15, density=True, label = 'normal', color='b', alpha=0.75, edgecolor='k')
plt.legend()
plt.show()



