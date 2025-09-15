# Note: everything in Python is an object, everything is always pass-by-refernece

a = []
b = a # Assignment of reference
assert id(a) == id(b)
a.append(1)
assert b[0] == 1
print(a, b)

import copy
a = [[]]
b = copy.copy(a) # Byte-for-byte copy of a, aka shallow copy
assert id(a) != id(b)
a.append(1)
assert len(b) == 1
a[0].append(1)
assert len(b[0]) == 1
print(a, b)

a = [[]]
b = copy.deepcopy(a) # Deep copy
assert id(a) != id(b)
a.append(1)
assert len(b) == 1
a[0].append(1)
assert len(b[0]) == 0
print(a, b)
