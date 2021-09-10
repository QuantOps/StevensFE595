import matplotlib.pyplot as plt
import numpy as np


def waveplot(self, x, y, z):
    self.x = x
    self.y = y
    self.z = z


if __name__ == '__main__':
    x = np.arange(0, 4 * np.pi, 0.1)
    y = np.sin(x)
    z = np.cos(x)
    plt.plot(x, y, x, z)
    plt.xlabel('X from Zero (0) - 4PI')
    plt.ylabel('Sin(x) & Cos(x)')
    plt.title('Sin Vs Cos Graph')
    plt.legend(['Sin(x)','Cos(x)'])
    plt.show()
