__author__ = '804'

from Binomial import Binomial

class FieldEnquationSolver:
    def __init__(self, a, b, c, q):
        self.a = a
        self.b = b
        self.c = c
        self.q = q

    def solve(self):
        disk = self.discriminant()
        if disk == 0:
            return ((((-self.b) % self.q)*self.inverse((2*self.a) % self.q, self.q)), (((-self.b) % self.q)*self.inverse((2*self.a) % self.q, self.q)))
        sqrt_disc = self.cipolla_sqrt(disk)
        return ((((-self.b + sqrt_disc) % self.q)*self.inverse((2*self.a) % self.q, self.q)) % self.q, (((-self.b - sqrt_disc) % self.q)*self.inverse((2*self.a) % self.q, self.q)) % self.q)

    def inverse(self, a, p):
        first_coef = [1, 0]
        second_coef = [0, 1]
        first = p
        second = a
        q = 0
        b = 0
        b_coef = [0, 0]
        while a != 1:
            q = (p - (p % a)) / a
            b = p % a
            p = a
            a = b
            b_coef[0] = (first_coef[0] - q*second_coef[0]) % self.q
            b_coef[1] = (first_coef[1] - q*second_coef[1]) % self.q
            first_coef[0] = second_coef[0]
            first_coef[1] = second_coef[1]
            second_coef[0] = b_coef[0]
            second_coef[1] = b_coef[1]
        return second_coef[1]

    def discriminant(self):
        return (self.b ** 2 - 4 * self.a * self.c) % self.q

    def cipolla_sqrt(self, a):
        found = False
        i = 1
        t = 0
        while (not found) and (i < self.q):
            if self.lejandrs_sign((i**2 - 4*a) % self.q, self.q) == -1:
                found = True
                t = i
            i += 1

        degree = (self.q + 1) / 2
        i = 1
        res = Binomial(0, 1, self.q, t, (-a) % self.q)
        prom = Binomial(1, 0, self.q, t, (-a) % self.q)
        if degree % 2 == 1:
            res.multiply(prom)
            degree = (degree - 1) / 2
        else:
            degree /= 2
        while degree != 0:
            prom.sqr()
            if degree % 2 == 1:
                res.multiply(prom)
                degree = (degree - 1) / 2
            else:
                degree /= 2
        return res.b

    def lejandrs_sign(self, a, p):
        b = 0
        lejandr = 1
        while p != 1:
            a %= p
            while a % 4 == 0:
                a /= 4
            if a % 2 == 0:
                if (p % 8 == 3) or (p % 8 == 5):
                    lejandr *= -1
                a /= 2
            if (a % 4 == 3) and (p % 4 == 3):
                lejandr *= -1
            b = a
            a = p
            p = b
        return lejandr