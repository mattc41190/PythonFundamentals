__author__ = 'mattc_000'


def banner( title, border="-"):
    line = border * len(title)
    print(line)
    print(title.upper())
    print(line)

banner("Argument Passing: Part One")

print("\nm = [9, 15, 24]")
print("def modify(k):\n   k.append(39)\n   print('k = ' + str(k))\n")
print("modify(m)")
print("print('m = ' + str(m))")

m = [9, 15, 24]


def modify(k):
    k.append(39)
    print("k = " + str(k))

modify(m)
print('m = ' + str(m))
print("\nNote:\nOriginal object modified in this case.")


banner("Argument Passing: Part Two")

print("\nr = [10, 20, 36]")
print("def replace(s):\n   s = [6, 8, 14]\n   print('s = ' + str(s))\n")
print("replace(r)")
print("print('r = ' + str(r))")

s = [10, 20, 36]


def replace(r):
    r = [6, 8, 14]
    print("r = " + str(r))

replace(s)
print('s = ' + str(s))
print("\nNote:\nOriginal object left unmodified in this case (we are not modifying, but replacing altogether).")

