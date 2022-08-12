class FieldElement(object):
    def __init__(self, num, prime):
        # if num < 0 or num >= prime:
        #     raise ValueError('Num {} not in field range 0 to {}'.format(num, prime-1))
        self.num = num % prime
        self.prime = prime

    def __repr__(self):
        return "FieldElement_{}({})".format(self.prime, self.num)

    def __eq__(self, other):
        return self.num == other.num and self.prime == other.prime

    def __ne__(self, other):
        return not (self.num == other.num and self.prime == other.prime)

    def __add__(self, other):
        return self.__class__((self.num + other.num) % self.prime, self.prime)

    def __sub__(self, other):
        return self.__class__((self.num - other.num) % self.prime, self.prime)

    def __mul__(self, other):
        return self.__class__((self.num * other.num) % self.prime, self.prime)

    def __pow__(self, n):
        return self.__class__(pow(self.num, n, self.prime), self.prime)

    def __truediv__(self, other):
        return self.__mul__(other.__pow__(self.prime - 2))

    def __floordiv__(self, other):
        return self.__truediv__(other)


class Point:
    def __init__(self, x, y, a, b):
        self.a = a
        self.b = b
        self.x = x
        self.y = y
        # secp256k1 curve
        if self.y**2 != self.x**3 + a * x + b:
            raise ValueError("({}, {}) is not on the curve".format(x, y))

    def __eq__(self, other):
        return (
            self.x == other.x
            and self.y == other.y
            and self.a == other.a
            and self.b == other.b
        )

    def __ne__(self, other):
        return (
            self.x != other.x
            or self.y != other.y
            or self.a != other.a
            or self.b != other.b
        )
