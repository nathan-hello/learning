# pylint: disable-all
# Couldn't paste problem 14. possible skill issue


def collatz(a):
    def even(n):
        return int(n / 2)

    def odd(n):
        return int((3 * n) + 1)

    results = [a]

    while True:
        a = results[-1]
        if int(a) == 1:
            return len(results)
        if results[-1] % 2 == 0:
            results.append(int(a / 2))
        elif results[-1] % 2 != 0:
            results.append(odd(a))


if __name__ == "__main__":
    most = 1

    for x in range(1, 1_000_000):
        res = collatz(x)
        if res > most:
            most = res
            print(f"{res} WINS WITH THEIR TEAMMATE GIGACHAT {x}")
    print(most)
