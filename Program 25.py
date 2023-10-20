import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]
y2 = [1, 3, 5, 7, 9]
y3 = [10, 8, 6, 4, 2]

plt.plot(x, y1, color='blue', linewidth=2, label='Line 1')
plt.plot(x, y2, color='red', linewidth=2, label='Line 2')
plt.plot(x, y3, color='green', linewidth=2, label='Line 3')

plt.legend()

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Multiple Lines with Legends')

plt.show()
