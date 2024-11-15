from math import factorial
import re

def p6():
    txt = input()
    while True:
        m = re.search(r"((?:[A-Z][a-z]+ )+(?:[A-Z][a-z]+))", txt)
        if m is not None:
            s = m.span()
            txt = txt[0:s[0]] + str.join("", [w[0] for w in m.group().split(" ")]) + txt[s[1]:]
        else:
            break
    print(txt)

def p8():
    def arrange_seats(seats: int, aisles: int):
        if aisles == 1: return [(seats + 1) // 2, seats // 2]
        res = [0 for _ in range(aisles + 1)]

        for i in range(1, aisles + 2):
            row = (i % (aisles + 1)) - 1
            res[row] += 1
            seats -= 1

        for i in range(1, min(aisles, seats + 1)):
            row = i % (aisles - 1) + 1
            res[row] += 1
            seats -= 1

        for i in range(1, seats + 1):
            row = (i % (aisles + 1)) - 1
            res[row] += 1

        return res

    def side_incon(n):
        return (n * (n - 1)) / 2

    def calculate_inconvenience(seating) -> int:
        total = side_incon(seating[0]) + side_incon(seating[-1])
        if len(seating) == 2: return total
        for i in range(1, len(seating) - 1):
            # print(f"Total now: {total}")
            x = seating[i]
            if x % 2 == 1:
                plus = ((x - 1) / 2) ** 2
                total += plus
            else:
                plus = (x / 2) * ((x / 2) - 1)
                total += plus
        return total

    def comb(n, r):
        return int(factorial(n) / (factorial(r) * factorial(n - r)))

    def calculate_num_possibilities(seats: int, aisles: int) -> int:
        if seats > 2 * aisles:
            n = aisles + 1
            r = (seats - (2 * aisles)) % (aisles + 1)
            return comb(n, r)
        else:
            n = aisles - 1
            r = seats - aisles - 1
            return comb(n, r)

    p8in = [int(i) for i in input().split(" ")]
    arrangements = arrange_seats(*p8in)
    inconvenience = calculate_inconvenience(arrangements)
    num_possibilities = calculate_num_possibilities(*p8in)
    print(f"There are {num_possibilities} ways to achieve {inconvenience} inconvenience!")
