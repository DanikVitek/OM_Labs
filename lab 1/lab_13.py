class Polynom:
    def __init__(self, func, a: float, b: float, epsilon: float, method: str, output: open):
        self.a = a
        self.b = b

        self.max_attempts = 10000
        import sys
        sys.setrecursionlimit(self.max_attempts)
        self.eps = epsilon
        
        self.f = func
        self.root=float()
        
        self.iterations = 0
        import time
        start = time.time()
        if method == 'b':
            self.bisection_method(output)
        elif method == 'c':
            self.chord_method(output)
        elif method == 't':
            self.tangent_method(output)
        self.duration = time.time() - start

    def bisection_method(self, output): #метод бісекції
        from numpy import sign
        def iteration(start, end):
            output.write("[{0} ; {1}]\nf({0}) = {2}\nf({1}) = {3}\n\n".format(start, end, self.f(start), self.f(end)))
            c = (start + end) / 2
            self.iterations += 1
            if abs(end - start) < self.eps and abs(self.f(c)) < self.eps:
                return c
            if sign(self.f(c))*sign(self.f(start)) < 0:
                return iteration(start, c)
            else:
                return iteration(c, end)
        
        self.root = round(iteration(self.a, self.b), ndigits=5)

    def chord_method(self, output): #метод хорд
        def iteration(start, end, prev_c):
            output.write("[{0} ; {1}]\nf({0}) = {2}\nf({1}) = {3}\n\n".format(start, end, self.f(start), self.f(end)))
            c = (start*self.f(end) - end*self.f(start))/(self.f(end) - self.f(start))
            self.iterations += 1
            if abs(c - prev_c) < self.eps and abs(self.f(c)) < self.eps:
                return c
            from numpy import sign
            if sign(self.f(start))*sign(self.f(end)) > 0:
                return iteration(start, c, c)
            else:
                return iteration(c, end, c)

        self.root = round(iteration(self.a, self.b, self.a), ndigits=5)

    def tangent_method(self, output): #метод дотичних(Ньютона)
        from scipy.misc import derivative
        f2 = lambda x: derivative(self.f, x, dx=1e-10, n=2)
        x0 = float()
        from numpy import sign
        if sign(self.f(self.a))*sign(f2(self.a)) > 0:
            x0 = self.a
        else:
            x0 = self.b

        def iteration(xn):
            output.write("x0 = {0}\nf({0}) = {1}\n\n".format(xn, self.f(xn)))
            f1 = lambda x: derivative(self.f, x, dx=1e-10)
            xn1 = xn - self.f(xn)/f1(xn)
            self.iterations += 1
            if abs(xn1 - xn) < self.eps and abs(self.f(xn1)) < self.eps:
                return xn1
            return iteration(xn1)
        
        self.root = round(iteration(x0), ndigits=5)
