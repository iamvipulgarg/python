a=1767676767
b=1767676767
c=1767676767
print(a)
print(b)
print(c)
print(id(a))
print(id(b))
print(id(c))
b=11
print()
print(b)
print(id(a))
print(id(b))
print(id(c))

print(len(str(id(c))))