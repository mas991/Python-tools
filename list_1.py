# 配列内の要素数カウント
# input = [0, 1, 3, 0, 2, 2, 0] output = [3, 1, 2, 1]
def count_numbers_in_array(a: list) -> list:

    b = [0] * (max(a)+1)

    for i in a:
        b[i] += 1

    return b

# 約数列挙


def divisor_array(n: int) -> list:

    l1 = []
    sq = int(n ** 0.5)
    for i in range(1, sq+1):
        if n % i == 0:
            l1.append(i)
            if i * i != n:
                l1.append(n//i)
    l1 = sorted(l1, key=lambda x: x)

    return l1
