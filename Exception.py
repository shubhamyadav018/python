
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


print("starting line")
a=[11,22,33]

try:
    #a=10 / 5
    #print(a[5])
    print(a)
except zeroDivisionError:
        print("exception raised due to zero division error")
except IndexError:
        print("exception raised due to index out of range")
except NameError:
    print("exception raised due to undefined variable")
except:
    print("same exception raised")
else:
    print("NO exception raised . everything worked perfrectly")
finally:
    print("this is a final block")
print("outside the try block")
