# pylint: disable-all
# Problem 9
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, a2 + b2 = c2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc


def main():
    d = 1000

    for a in range(1, d + 1):
        for b in range(a, d + 1):
            c = d - a - b
            if (a * a + b * b) == c * c:
                product = a * b * c
                return [a, b, c, product]


if __name__ == "__main__":
    print(main())
