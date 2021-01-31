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
