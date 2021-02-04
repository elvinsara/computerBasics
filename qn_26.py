d = {}
e = {}
n1 = int(input("enter the number of elements in d:"))
for i in range(n1):
    key = input("enter the key:")
    value = input("enter the value:")
    d[key] = value
n2 = int(input("enter the number of elements in e:"))
for i in range(n2):
    key = input("enter the key:")
    value= input("enter the value:")
    e[key] = value

for key in d:
    if key in e:
        d[key] = int(d[key])+int(e[key])

e.update(d)
print(e)

