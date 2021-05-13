import numpy as np
from matplotlib import pyplot as plt


def func_iter(x):
    return x*x*x+6*x*x+x-6

def func_der(x):
    return 3*x*x+12*x+1

def newton_rhapson(x0):

    eps = 0.000000000001
    xi =x0 - func_iter(x0)/func_der(x0)
    for i in range(1000):
        xi = xi - func_iter(xi)/func_der(xi)
        if xi < eps:
            return xi
    return xi        





if __name__ == "__main__":

    # Metoda podstawiania iteracyjnego
    # Udaje znaleźć się wszystkie pierwiastki z pewnym błędem dokładności
    # Stąd dodatkowe wartości
    x = np.arange(-6.0, 1.0, 0.0000001,dtype=float)
    y = func_iter(x)
    rozw = x[(y < 0.000001)*(y>-0.000001)]
    print("Rozwiązanie iteracyjne:")
    print(rozw)
    plt.plot(x,y)
    plt.show()
    print("Newton-Rhapson:")
    x1 = newton_rhapson(-6)
    x2 = newton_rhapson(-2)
    x3 = newton_rhapson(4)
    print(x1)
    print(x2)
    print(x3)
    