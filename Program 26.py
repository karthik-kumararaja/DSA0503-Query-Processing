import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = x**2

plt.figure(figsize=(10, 5))

plt.subplot(131)
plt.plot(x, y1, label='sin(x)')
plt.title('Sine Wave')


plt.subplot(132)
plt.plot(x, y2, label='cos(x)')
plt.title('Cosine Wave')


plt.subplot(133)
plt.plot(x, y3, label='x^2')
plt.title('Quadratic Function')


plt.legend()

plt.tight_layout()


plt.show()
