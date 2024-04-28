
class Box:
    def __init__(self, name , roll = 12 , osmarks = 45 ):
        self.name = name
        self.roll= roll
        self.osmarks = osmarks

obj1 =Box("shubham",22,97)
obj2 =Box("shivu")

print(obj1.osmarks)
print(obj1.roll)
print(obj2.osmarks)

print(obj2.roll)
