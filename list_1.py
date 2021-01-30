# 配列内の要素数カウント
# input = [0, 1, 3, 0, 2, 2, 0], output = [3, 1, 2, 1]
def count_numbers_in_array(a: list) -> list:

    b = [0] * (max(a)+1)

    for i in a:
        b[i] += 1

    return b


# 約数列挙
# input = 36, output = [1, 2, 3, 4, 6, 9, 12, 18, 36]
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


# 配列の任意の列でソート
# 1. 第２引数 = 指定なし or 0
# input = [[1, 3], [5, 4], [2, 2]], output = [[1, 3], [2, 2], [5, 4]]
# 2. 第２引数 = 1
# input = [[1, 3], [5, 4], [2, 2]], output = [[2, 2], [1, 3], [5, 4]]
def sort_by_lambda(a: list, b=0) -> list:
    c = sorted(a, key=lambda x: x[b])

    return c
