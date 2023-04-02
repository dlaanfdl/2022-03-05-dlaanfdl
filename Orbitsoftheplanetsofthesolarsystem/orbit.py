import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import numpy as np
import math
rc('font', family='HCR dotum')
plt.figure(figsize=(7, 7))
radius = [0.4, 0.7, 1, 1.5, 5.2, 9.6, 19.2, 30.1]
planets_name = ['수성', '금성', '지구', '화성', '목성', '토성', '천왕성', '해왕성']
angle = np.arange(0, 360)
cnt = 0

for r in radius:
    x = []
    y = []
    for theta in angle:
        x.append(r*math.cos(math.radians(theta)))
        y.append(r*math.sin(math.radians(theta)))
    plt.plot(x, y, label=planets_name[cnt])
    cnt += 1

plt.legend()
plt.grid(linestyle='--')
plt.xlabel('AU')
plt.ylabel('AU')
plt.title('orbits the planets in the solar system')
plt.show()
