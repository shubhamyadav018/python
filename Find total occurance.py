def findTotaloccurances(listofNumbers,target):
        result=0
        n=len(listofNumbers)
        for index in range(n):
                if listofNumbers[index] ==  target:
                    result = result + 1
        return result 


listofNumbers = [12,34,21,-12,34,55,56,34,12]
target = 34 

result = findTotaloccurances(listofNumbers,target)
print("Total number of occurances:",result)

lis2 = [12,13,23,54,56,4,3,2,1,23,43,23]
target2 = 23
result2 = findTotaloccurances(lis2,target2)
print(result2)
