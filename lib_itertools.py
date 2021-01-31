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
