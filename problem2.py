a = 1
b = 2
s = 2
while b < 4000000:
    b = a + b
    a = b - a
    if not b%2:
        s += b

print(s)

