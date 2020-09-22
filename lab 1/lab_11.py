import numpy as np

def f0(x: float) -> float:
    return (x**4) - (3*x**3) + (2*x) - 6

def f1(x: float) -> float:
    return (4*x**3) - (9*x**2) + 2

def f2(x: float) -> float:
    return -3*x**2 + 7*x + 10*x

def f3(x: float) -> float:
    return -127*x - 28

def sign(x: float) -> str:
    if x < 0:
        return '-'
    elif x > 0:
        return '+'
    else:
        return '0'

if __name__ == "__main__":
    # x = float(input("X = "))
    # print("f0: " + sign(f0(x)))
    # print("f1: " + sign(f1(x)))
    # print("f2: " + sign(f2(x)))
    # print("f3: " + sign(f3(x)))
    # print("f4: +")

    signs = []
    j = 0
    for i in np.linspace(-0.432, -0.431, 500):
        signs.append([
            sign(f0(i)),
            sign(f1(i)),
            sign(f2(i)),
            sign(f3(i)),
            '+'])
        j+=1
    
    signs = np.array(signs).transpose()
    output = open('signs.txt', 'w')
    
    for row in signs:
        output.write(" ".join(row) + "\n")