import numpy as np


class Integrate:

    def __init__(self, func, start, end, method="lower_r", n=100):
        """
        Constructor
        """
        self.func = func
        self.start = start
        self.end = end
        self.n = n
        self.method = method
        self.res = Integrate.solve(self)

    def __repr__(self):
        return str(self.res)

    def __str__(self):
        return 'The value of the integral is: {}'.format(self.res)

    def lower_r(self):
        n = (self.end - self.start) / self.n
        i = np.arange(self.start, self.end, n)
        res = self.func(i)
        return np.sum(n * res)

    def comp_trap(self):
        k = np.arange(1, self.n, 1)
        tot = np.sum(self.func(self.start + k * (self.end - self.start) / self.n))
        tot = (tot + self.func(self.start) / 2 + self.func(self.end) / 2) * (self.end - self.start) / self.n
        return tot

    def simpson(self):
        if self.n % 2 != 0:
            self.n = self.n + 1

        c = np.tile(np.array([2, 4]), int(self.n / 2) - 1)
        c = np.append(1, c)
        c = np.append(c, 1)
        d = (self.end - self.start) / self.n
        i = np.arange(self.start, self.end, d)
        res = (d / 3) * np.sum(c * self.func(i))
        return res

    def mc(self):
        i = np.random.uniform(self.start, self.end, self.n)
        d = self.end - self.start
        return d * np.average(self.func(i))

    def solve(self):
        if self.method == "lower_r":
            return Integrate.lower_r(self)
        elif self.method == "comp_trap":
            return Integrate.comp_trap(self)
        elif self.method == "simpson":
            return Integrate.simpson(self)
        elif self.method == "mc":
            return Integrate.mc(self)
        else:
            return "Please input a valid method"