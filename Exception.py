
print("starting line")
a=[11,22,33]
print(a)

try:
    print(a[5])
    a=10 / 5
except:
    print("same exception raised")
else:
    print("NO exception raised . everything worked perfrectly")
finally:
    print("this is a final block")
print("outside the try block")

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
