import numpy as np
import matplotlib
matplotlib.use('WebAgg')
import matplotlib.pyplot as plt

def f0(x: float) -> float:
    return (x**4) - (3*x**3) + (2*x) - 6

def f1(x: float) -> float:
    return (4*x**3) - (9*x**2) + 2

def f2(x: float) -> float:
    return -3*x**2 + 7*x + 10*x

def f3(x: float) -> float:
    return -127*x - 28

if __name__ == "__main__":
    data = np.linspace(-1.5, 3.2, 2000)
    F0 = f0(data)
    F1 = f1(data)
    # F2 = f2(data)
    # F3 = f3(data)
    # F4 = [201069/32258]*2

    plt.plot(data, F0, label='f0')
    plt.plot(data, F1, label='f1')
    # plt.plot(data, F2, label='f2')
    # plt.plot(data, F3, label='f3')
    # plt.plot([-1.26, 7], F4, label='f4')
    plt.legend()

    plt.plot([data[0], data[-1]], [0, 0], color='black', linewidth=0.5)
    plt.plot([0, 0], [f1(data[0]), f1(data[-1])], color='black', linewidth=0.5)

    plt.show()