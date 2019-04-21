import numpy as np
import matplotlib.pyplot as plt


class Polynomial:

    def __init__(self, *coefficients):
        """ input: coefficients are in the form a_n, ...a_1, a_0
        """
        # for reasons of efficiency we save the coefficients in reverse order,
        # i.e. a_0, a_1, ... a_n
        self.coefficients = coefficients[::-1]  # tuple is also turned into list

    def __repr__(self):
        """
        method to return the canonical string representation
        of a polynomial.

        """
        # The internal representation is in reverse order,
        # so we have to reverse the list
        return "Polynomial" + str(self.coefficients[::-1])

    def __call__(self, x):
        res = 0
        for index, coeff in enumerate(self.coefficients):
            res += coeff * x ** index
        return res

    def degree(self):
        return len(self.coefficients)

    @staticmethod
    def zip_longest(iter1, iter2, fillchar=None):
        for i in range(max(len(iter1), len(iter2))):
            if i >= len(iter1):
                yield (fillchar, iter2[i])
            elif i >= len(iter2):
                yield (iter1[i], fillchar)
            else:
                yield (iter1[i], iter2[i])
            i += 1

    def __add__(self, other):
        c1 = self.coefficients
        c2 = other.coefficients
        res = [sum(t) for t in Polynomial.zip_longest(c1, c2)]
        return Polynomial(*res)

    def __sub__(self, other):
        c1 = self.coefficients
        c2 = other.coefficients

        res = [t1 - t2 for t1, t2 in Polynomial.zip_longest(c1, c2)]
        return Polynomial(*res)


p1 = Polynomial(4, 0, -4, 3, 0)
p2 = Polynomial(-0.8, 2.3, 0.5, 1, 0.2)
p_sum = p1 + p2
p_diff = p1 - p2
X = np.linspace(-3, 3, 50, endpoint=True)
F1 = p1(X)
F2 = p2(X)
F_sum = p_sum(X)
F_diff = p_diff(X)
plt.plot(X, F1, label="F1")
plt.plot(X, F2, label="F2")
plt.plot(X, F_sum, label="F_sum")
plt.plot(X, F_diff, label="F_diff")
plt.legend()
plt.show()