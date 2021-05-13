#1. równanie: x1 = 1, x2 = -2
#2. równanie: x=0
#Rozwiązanie równań: x1=-5.6334, x2=-1.2315, x3=0.86489

import numpy as np
from matplotlib import pyplot as plt


def func1(x):
    return x*x+x-2

def func2(x):
    return -2*x*x/(x+3)


if __name__ == "__main__":
    
    x_1 = np.arange(-2.99, 10, 0.01, dtype=float)
    x_2 = np.arange(-10, -3, 0.01, dtype=float)
    x = np.arange(-10, 10, 0.01, dtype=float)

    y1 = func1(x)
    y2_1 = func2(x_1)
    y2_2 = func2(x_2)

    plt.plot(x,y1,'b')
    plt.plot(x_1,y2_1,'r')
    plt.plot(x_2,y2_2,'r')
    plt.ylim(top=300,bottom=-300)
    
    plt.show()
    