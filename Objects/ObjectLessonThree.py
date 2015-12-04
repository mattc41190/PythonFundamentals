__author__ = 'mattc_000'


def banner(title, border="-"):
    line = border * len(title)
    print(line)
    print(title.upper())
    print(line)


banner("Default Arguments")

print("\nFirst we create a method that adds spam to an argument called menu whose default value is an empty")
print("def addSpam(menu=[]):\n   menu.append('Spam')\n   print(menu))\n")
print("breakfast= ['Eggs', 'Bacon, 'Orange Juice']")
print("addSpam(breakfast)\n")


def add_spam(menu=[]):
    menu.append('Spam')
    print(menu)


breakfast = ['Eggs', 'Bacon', 'Orange Juice']
add_spam(breakfast)
