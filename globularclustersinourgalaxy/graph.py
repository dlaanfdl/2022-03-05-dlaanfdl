# 우리 은하 구상상단 3D그래프
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd

data = pd.read_csv('globularclustersinourgalaxy\\globular2.csv')
x = data['x']
y = data['y']
z = data['z']

# 그래프 표현
fig = plt.figure(figsize=(5, 5))
ax = fig.add_subplot(projection='3d')  # 3D그래프로 지정
ax.view_init(10, 60)  # 그래프가 보이는 각도 지정
ax.scatter(x, y, z, marker='o', s=15, c='darkgreen')

# 3차원 그래프에 점으로 표현하라는 의미
ax.scatter(0, 0, 0, marker='o', s=35, c='red')  # 태양의 위치
plt.show()
