import os

t1 = {"20200420", "20200421"}
t2 = {"20200420", "20200421"}

t3 = t2 - t1
t2.add("20200420")
print(t2)
t2.add("20200425")
print(t2)
print(t3)

if not t3:
    print("ok")



motoer = ["hell", "wath"]

motoer.sort()
print(type(motoer))

print(motoer)
del motoer[0]

print(motoer)


f = True

g = False

result = f==g
print(result)
