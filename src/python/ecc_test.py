import unittest
from ecc import *


class ECCTest(unittest.TestCase):
    def test_eq(self):
        a = FieldElement(44, 57)
        self.assertEqual(a == a, True)  # add assertion here

    def test_eq_diff(self):
        a = FieldElement(44, 57)
        b = FieldElement(33, 57)
        self.assertEqual(a == b, False)  # add assertion here

    def test_eq_diff(self):
        a = FieldElement(44, 57)
        b = FieldElement(33, 57)
        self.assertEqual(a != b, True)  # add assertion here

    def test_ex1_2_1(self):
        a = FieldElement(44, 57)
        b = FieldElement(33, 57)
        c = FieldElement(20, 57)
        self.assertEqual(a + b, c)

    def test_ex1_2_2(self):
        a = FieldElement(9, 57)
        b = FieldElement(29, 57)
        c = FieldElement(-20, 57)
        self.assertEqual(a - b, c)

    def test_ex1_2_3(self):
        a = FieldElement(17, 57)
        b = FieldElement(42, 57)
        c = FieldElement(49, 57)
        self.assertEqual(a + b + c, FieldElement(51, 57))

    def test_ex1_2_4(self):
        a = FieldElement(52, 57)
        b = FieldElement(30, 57)
        c = FieldElement(38, 57)
        self.assertEqual(a - b - c, FieldElement(41, 57))

    def test_ex1_3_1(self):
        a = FieldElement(95, 97)
        b = FieldElement(45, 97)
        c = FieldElement(31, 97)
        self.assertEqual(a * b * c, FieldElement(23, 97))

    def test_ex1_3_2(self):
        a = FieldElement(17, 97)
        b = FieldElement(13, 97)
        c = FieldElement(19, 97)
        d = FieldElement(44, 97)
        self.assertEqual(a * b * c * d, FieldElement(68, 97))

    def test_ex1_3_3(self):
        a = FieldElement(12, 97)
        b = FieldElement(77, 97)
        self.assertEqual(pow(a, 7) * pow(b, 49), FieldElement(63, 97))

    def test_ex1_5(self):
        for i in [1, 3, 7, 13, 18]:
            FieldList = [FieldElement(i * k, 19) for k in range(19)]
            print(FieldList)

    def test_ex1_7(self):
        for p in [7, 11, 17, 31]:
            FieldList = [pow(FieldElement(i, p), p - 1) for i in range(1, p)]
            print(FieldList)

    def test_ex1_8_1(self):
        a = FieldElement(3, 31)
        b = FieldElement(24, 31)
        self.assertEqual(a / b, FieldElement(4, 31))

    def test_ex1_8_2(self):
        a = FieldElement(17, 31)
        self.assertEqual(pow(a, -3), FieldElement(29, 31))

    def test_ex1_8_3(self):
        a = FieldElement(4, 31)
        b = FieldElement(11, 31)
        self.assertEqual(pow(a, -4) * b, FieldElement(13, 31))

    def test_ex2_1(self):
        for i, xy in enumerate([(2, 4), (-1, -1), (18, 77), (5, 7)]):
            x, y = xy
            if i == 0 or i == 3:
                with self.assertRaises(ValueError):
                    Point(x, y, 5, 7)
            else:
                point = Point(x, y, 5, 7)
                print(point)

    def test_ex2_4(self):
        a = Point(2, 5, 5, 7)
        b = Point(-1, -1, 5, 7)
        print((a + b).x, (a + b).y)

    def test_ex2_6(self):
        a = Point(-1, -1, 5, 7)
        print((a + a).x, (a + a).y)

    def test_ex3_1(self):
        prime = 223
        a = FieldElement(0, prime)
        b = FieldElement(7, prime)
        valid_points = [(192, 105), (17, 56), (1, 193)]
        invalid_points = [(200, 119), (42, 99)]
        for x_raw, y_raw in valid_points:
            x = FieldElement(x_raw, prime)
            y = FieldElement(y_raw, prime)
            Point(x, y, a, b)
        for x_raw, y_raw in invalid_points:
            x = FieldElement(x_raw, prime)
            y = FieldElement(y_raw, prime)
            with self.assertRaises(ValueError):
                Point(x, y, a, b)

    def test_ex3_2(self):
        prime = 223
        a = FieldElement(0, prime)
        b = FieldElement(7, prime)
        points = [[(170, 142), (60, 139)], [(47, 71), (17, 56)], [(143, 98), (76, 66)]]
        for x_raw, y_raw in points:
            x1 = FieldElement(x_raw[0], prime)
            y1 = FieldElement(x_raw[1], prime)
            x2 = FieldElement(y_raw[0], prime)
            y2 = FieldElement(y_raw[1], prime)
            c = Point(x1, y1, a, b)
            d = Point(x2, y2, a, b)
            ans = c + d
            print(ans.x, ans.y)

    def test_ex3_4(self):
        prime = 223
        a = FieldElement(0, prime)
        b = FieldElement(7, prime)
        points = [
            (2, 192, 105),
            (2, 143, 98),
            (2, 47, 71),
            (4, 47, 71),
            (8, 47, 71),
            (21, 47, 71),
        ]
        for c, x_raw, y_raw in points:
            x = FieldElement(x_raw, prime)
            y = FieldElement(y_raw, prime)
            d = Point(x, y, a, b)
            ans = c * d
            print(ans.x, ans.y)

    def test_ex3_5(self):
        prime = 223
        a = FieldElement(0, prime)
        b = FieldElement(7, prime)
        x = FieldElement(15, prime)
        y = FieldElement(86, prime)
        p = Point(x, y, a, b)
        print(7 * p)


if __name__ == "__main__":
    unittest.main()
