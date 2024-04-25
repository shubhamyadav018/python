n = int(input())
l = list(map(int,input().split()))

fixThis = n - 1
while fixThis > 0:
    for index in range(fixThis):
        if l[index] > l[index + 1]:
            l[index], l[index + 1] = l[index + 1],l[index]
    fixThis -= 1
print(*l)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Selection-Sort Algorithm:-

def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Input
n = int(input())
numbers = list(map(int, input().split()))

# Sorting
selection_sort(numbers)

# Output
print(*numbers)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Insertion-Sort Algorithm:-

def insertion_Sort(arr):
    for i in range(1 , len(arr)):
        key = arr[i]
        j =  i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key 
            
n = int(input())
arr = list(map( int , input().split()))

insertion_Sort(arr)

print(*arr)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Merge-Sort Algorithm:-

def merge_Sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr)//2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    
    left_half = merge_Sort(left_half)
    right_half = merge_Sort(right_half)
    
    return merge(left_half,right_half)
def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0
    
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
            
    merged += left[left_index:]
    merged += right[right_index:]
    
    return merged

n = int(input())
arr = list(map(int, input().split()))

sorted_arr = merge_Sort(arr)

print(*sorted_arr)


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Quick-Sort Algorithm :-

def quick_Sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        Pivot = arr[0]
        less_Then_Pivot = [x for x in arr[1:]if x<= Pivot]
        greater_Then_Pivot = [x for x in arr[1:]if x > Pivot]
        return quick_Sort(less_Then_Pivot) + [Pivot] + quick_Sort(greater_Then_Pivot)

n = int(input())
arr = list(map(int , input().split()))

Sorted_arr = quick_Sort(arr)

print(*Sorted_arr)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`
