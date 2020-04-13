import numpy as np
import matplotlib.pyplot as plt
# x = np.arange(0, 3*np.pi, 0.1)
# y = np.tan(x)
x = np.linspace(0,20,2)
y1 = [0,117]
y2 = [0,96]
y3 = [0,46]
data1 = 117
data2 = 87
data3 = 43

# COVID INDONESIA
ax = plt.gca()
# for data in range(data1):
#     ax.scatter(x=[data,data], y=[data,data], label='Data')
plt.plot(x, y1, "-b", label='y1')
plt.plot(x, y2, "-r", label='y2')
plt.plot(x, y3, "-y", label='y3')
plt.legend(loc="best")
# plt.ylim(-1.5, 2.0)
ax.set_xlabel("")
ax.set_ylabel("Jumlah")
plt.title("COVID - INDONESIA")
plt.show()

print("debug")
