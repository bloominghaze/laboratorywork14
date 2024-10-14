import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(1, 10, 100)

y = (1/x) * np.cos(x**2 + 1/x)

plt.plot(x, y, label=r'$\frac{1}{x} \cdot \cos(x^2 + \frac{1}{x})$', color="green", linewidth=3)

plt.xlabel('x', fontsize=12, color='blue')
plt.ylabel('Y(x)', fontsize=12, color='blue')

plt.title('Графік функції', fontsize=15)

plt.grid(True)

plt.legend()

plt.show()
