def numbersgreaterThenTarget(listofNumbers,target):
        result=0
        n=len(listofNumbers)
        for index in range(n):
                if listofNumbers[index] >  target:
                    result = result + 1
        return result 


listofNumbers = [12,34,21,-12,34,55,56,34,12]
target = 35

result = numbersgreaterThenTarget(listofNumbers,target)
print("Total number of grater then target:",result)
