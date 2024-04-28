class Box:
    def _init_(self,currname,currRollnum,currjavamarks,currosmarks,currmathsmarks,currdsmarks):
       self.name = currname
       self.rollNumber = currRollnum
       self.javamarks = currjavamarks
       self.osmarks = currosmarks
       self.mathsmarks=currmathsmarks
       self.dsmarks=currdsmarks


student1 = Box("shiv",34,45,66,77,98)
print(student1.name)
print(student1.rollNumber)
print(student1.dsmarks)
    

student2 = Box("xxx",333,44,23,67,98)
print(student2.name)
print(student2.rollNumber)
print(student2.dsmarks)




student3 = Box("yyy",332,75,69,74,67)
print(student3.name)
print(student3.rollNumber)
print(student3.dsmarks)



student4= Box("zzz",343,32,63,71,99)
print(student4.name)
print(student4.rollNumber)
print(student4.dsmarks)



student5= Box("www",35,22,83,75,92)
print(student5.name)
print(student5.rollNumber)
print(student5.dsmarks)
