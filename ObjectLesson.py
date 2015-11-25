__author__ = 'mattc_000'
def banner( title, border="-"):
    line = border * len(title)
    print(line)
    print(title.upper())
    print(line)


banner("Integer Compare")
x = 1
y = 1

print("x = 1\ny = 1\n\nx == y:\n" + str(x == y))
print("\nx is y:\n" + str(x is y))
print("\nId(x)\n" + str(id(x)))
print("\nId(y)\n" + str(id(y)))

banner("Array Compare")
a = [1,2,3]
b = [1,2,3]

print("a = [1,2,3]\nb = [1,2,3]\n\na == b:\n" + str(a == b))
print("\na is b:\n" + str(a is b))
print("\nId(a)\n" + str(id(a)))
print("\nId(b)\n" + str(id(b)))

r = [2,4,6]
s = r
print("\ns = [2,4,6]\nr = s\n\ns == r:\n" + str(s == r))
print("\ns is r:\n" + str(s is r))
print("\nId(r)\n" + str(id(r)))
print("\nId(s)\n" + str(id(s)))
s[1] = 78
print("\ns[1] = 78\nprint r\n" + str(r))
