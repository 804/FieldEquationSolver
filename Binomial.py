__author__ = '804'

class Binomial:
    def __init__(self, a, b, q, t1, t0):
        self.a = a
        self.b = b
        self.q = q
        self.t0 = t0
        self.t1 = t1

    def addition(self, bin):
        self.a = (self.a + bin.a) % self.q
        self.b = (self.b + bin.b) % self.q

    def const_multiply(self, const):
        self.a = const*self.a % self.q
        self.b = const*self.b % self.q

    def multiply(self, bin):
        a0 = self.a
        b0 = self.b
        self.a = (a0*bin.b + b0*bin.a + self.t1*a0*bin.a) % self.q
        self.b = (b0*bin.b + self.t0*a0*bin.a) % self.q

    def sqr(self):
        a0 = self.a
        b0 = self.b
        self.a = (a0*b0*2 + self.t1*a0*a0) % self.q
        self.b = (b0*self.b + self.t0*a0*a0) % self.q