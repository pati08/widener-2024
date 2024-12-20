from math import factorial, sqrt
from collections import deque
import re

def p1():
    ins = input().split(" ")
    a = float(ins[0])
    b = float(ins[1])
    c = float(ins[2])

    s = (a + b + c) / 2.0

    r = sqrt(s * (s - a) * (s - b) * (s - c))
    print(round(r, 2))

def p2():
    ins = input().split(" ")
    a = float(ins[0])
    b = float(ins[1])

    print(round(a / b, 2))

def p3():
    ins = input().split(" ")
    a = float(ins[0])
    b = float(ins[1])
    c = float(ins[2])

    price = a * c
    nod = 1.0 - (0.2 * b)
    print(round(price * nod, 2))

def p4():
    ins = input().split(" ")
    a = float(ins[0])
    b = float(ins[1])

    res = str(round(a / b, 2)) + " "
    if a / b > 0.75:
        res += "NO"
    else:
        res += "YES"
    
    print(res)

def p5():
    ins = list(input())
    total = 0
    for c in ins:
        if c == 'y': total += 2
        if c == 'g': total += 1
        if c == 'r': total += 3
    print(total)

def p6():
    txt = input()
    while True:
        m = re.search(r"\b([A-Z][a-z]+ )+[A-Z][a-z]+\b", txt)
        if m is None: break
        s = m.span()
        txt = txt[0:s[0]] + str.join("", [w[0] for w in m.group().strip().split(" ")]) + txt[s[1]:]
    print(txt)

def p7():
    ins = [int(i) for i in input().split(" ")]
    ins.pop(0)
    sortedins = ins.copy()
    sortedins.sort()
    total = 0
    for i in range(len(ins)):
        idx = sortedins.index(ins[i])
        total += abs(idx - i)
    print(total)

def p8():
    def arrange_seats(seats: int, aisles: int):
        # res =  [seats // (aisles + 1) + max(0, ((seats % (aisles + 1)) - i + 1)) for i in range(1, aisles + 2)]
        # res.insert(0, res.pop())
        res = [1 for _ in range(0, aisles + 1)]
        seats -= aisles + 1

        for i in range(1, aisles):
            if seats == 0: break
            res[i] += 1
            seats -= 1

        while seats >= 1:
            res[0] += 1
            seats -= 1
            if seats >= 1:
                res[-1] += 1
                seats -= 1

            for _ in range(2):
                for i in range(1, aisles):
                    if seats == 0: break
                    res[i] += 1
                    seats -= 1

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
    # print(f"There are {num_possibilities} ways to achieve {inconvenience} inconvenience!")
    print(f"{int(inconvenience)} {num_possibilities}")

def p9():
    def get_cost_and_actions(current_state, target_state):
        d = len(current_state)
        cost = 0
        actions = []
        # Check if current_state is subset of target_state
        can_reach_without_reset = True
        for cs_bit, ts_bit in zip(current_state, target_state):
            if cs_bit == '1' and ts_bit == '0':
                can_reach_without_reset = False
                break
        if can_reach_without_reset:
            # Need to press buttons where current_state is 0 and target_state is 1
            buttons_to_press = []
            for i, (cs_bit, ts_bit) in enumerate(zip(current_state, target_state)):
                if cs_bit == '0' and ts_bit == '1':
                    buttons_to_press.append(str(i))
            cost = len(buttons_to_press)
            actions = buttons_to_press
        else:
            # Need to reset and then press buttons where target_state is 1
            buttons_to_press = []
            for i, ts_bit in enumerate(target_state):
                if ts_bit == '1':
                    buttons_to_press.append(str(i))
            cost = 1 + len(buttons_to_press)
            actions = ['R'] + buttons_to_press
        return cost, actions

    # Input handling
    d, n = map(int, input().split())
    passwords = set(input().strip() for _ in range(n))

    # Algorithm implementation
    initial_state = '0' * d
    current_state = initial_state
    presses = []
    passwords_left = passwords.copy()

    while passwords_left:
        min_cost = None
        next_password = None
        next_actions = []
        for pw in passwords_left:
            cost, actions = get_cost_and_actions(current_state, pw)
            if min_cost is None or cost < min_cost:
                min_cost = cost
                next_password = pw
                next_actions = actions
        presses.extend(next_actions)
        current_state = next_password
        assert(next_password is not None)
        passwords_left.remove(next_password)

    # Output results
    print(len(presses))
    print(' '.join(presses))


def p10():
    ins = input().split(" ")
    b = float(ins[0])
    d = float(ins[1])

    total = 0
    for i in range(int((b * b) / d)):
        a = i + 1
        c = round(((b / d) - (a / b)) * d, 6)
        if c == 0: continue
        if int(c) == c:
            total += 1
    print(total)

p9()
