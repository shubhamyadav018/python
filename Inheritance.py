class Box:
    def __init__(self,name,roll):
        self.name = name
        self.roll = roll

class student:
    def __init__(self,fees):
        self.fees = fees

class Box2(Box,student):
    def __init__(self,name,roll,marks,fees):
        self.marks = marks
        student.__init__(self,fees)
        Box.__init__(self,name,roll)

class Box3(Box2):
    def __init__(self,sem):
        self.sem = sem
        Box2.__init__(self,"ufffff",12,89,20000)

obj = Box3("2-1")
print(obj.sem)
print(obj.name)
obj2 = Box2("ufffff",12,89,20000)
print(obj2.name)
print(obj2.roll)
print(obj2.marks)
print(obj2.fees)
