import string
w = input()
W = w.upper()
l = list(string.ascii_uppercase)
b = list(map(lambda x: W.count(x), l))
c = b.index(max(b))
if b.count(c) == 1:
    d = l[c]
    print(d)
else:
    print("?")