import itertools

# カウントし続ける
# 引数（初期値, 間隔）小数も可
# itertools.count(1, 2) -> 1 3 5 7 9 ...
for i in itertools.count():
    if i > 10:
        break
    print(i)

# 渡した配列の要素をコピー(文字列も可)
# itertools.cycle(['ABCD']) -> A B C D A B C D ...
l = [1, 2, 3, 4]
cnt = 0
for i in itertools.cycle(l):
    if cnt > 10:
        break
    print(i)
    cnt += 1


# 渡した配列の中で条件が真の間はスキップ、そのあとはすべての要素をコピー
l1 = [1, 2, 4, 6, 3, 5]
l2 = list(map(int, itertools.dropwhile(lambda x: x < 4, l1)))
print(l2)  # 4, 6, 3, 5

l1 = ['apple', 'orange', 'banana']
l2 = list(map(str, itertools.dropwhile(lambda x: x != 'orange', l1)))
print(l2)  # orange, banana

l1 = 'abcabc'
l2 = list(map(str, itertools.dropwhile(lambda x: x != 'c', l1)))
print(l2)  # c, a, b, c


# 条件が真の要素を除外する
l = list(map(int, itertools.filterfalse(lambda x: x % 2 != 0, range(10))))
print(l)  # 0, 2, 4, 6, 8
l = list(map(str, itertools.filterfalse(lambda x: x == 'a', 'abcabc')))
print(l)  # b, c, b, c
l = list(map(str, itertools.filterfalse(lambda x: x != 'a', 'abcabc')))
print(l)  # a, a


# グループ化
l = [0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1]
gr = itertools.groupby(l)
for k, g in gr:
    print(f'{k}: {list(g)}')
    # 0: [0, 0]
    # 1: [1, 1, 1]
    # 0: [0, 0, 0]
    # 1: [1]
    # 0: [0, 0]
    # 1: [1, 1, 1]

l = 'AABBBCCBBA'
gr = itertools.groupby(l)
for k, g in gr:
    print(f'{k}: {list(g)}')
    # A: ['A', 'A']
    # B: ['B', 'B', 'B']
    # C: ['C', 'C']
    # B: ['B', 'B']
    # A: ['A']

# 要素の切り出し
l = list(itertools.islice('ABCDEFG', 2))
print(l)  # A, B
l = list(itertools.islice('ABCDEFG', 2, 4))
print(l)  # C, D
l = list(itertools.islice('ABCDEFG', 2, None))
print(l)  # C, D, E, F, G
l = list(itertools.islice('ABCDEFG', 0, None, 2))
print(l)  # A, C, E, G


# 順列列挙(第２引数で要素数指定)
l = list(itertools.permutations(range(3)))
print(l)  # [(0, 1, 2), (0, 2, 1), (1, 0, 2), (1, 2, 0), (2, 0, 1), (2, 1, 0)]
l = list(itertools.permutations(range(3), 2))
print(l)  # [(0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1)]
l = list(itertools.permutations('ABB'))
print(l)  # [('A', 'B', 'B'), ('A', 'B', 'B'), ('B', 'A', 'B'), ('B', 'B', 'A'), ('B', 'A', 'B'), ('B', 'B', 'A')]
# 重複削除
x = list(k for k, g in itertools.groupby('ABB'))
l = list(itertools.permutations(x))
print(l)  # [('A', 'B'), ('B', 'A')]


# 積和
print(list(itertools.product('ABCD', 'xy')))
print(list(itertools.product(range(2), repeat=3)))
