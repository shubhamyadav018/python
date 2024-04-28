def totalEvennumbers(listofNumbers):
        result=0
        n=len(listofNumbers)
        for index in range(n):
                if listofNumbers[index] % 2 == 0 :
                    result =result + 1
        return result 


listofNumbers = [12,34,21,-12,34,55,56,34,12]


result = totalEvennumbers(listofNumbers)
print("total even numbers are :",result)
