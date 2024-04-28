word = input()
print(word)
store = dict()
for ch in word:
    if ch in store:
        store[ch] = store[ch] + 1
    else:
        store[ch] = 1
print(store)

resultchar = '#'
resultfrequency = 0
   
allkeys = store.keys()
for ele in allkeys:
    if store[ele] > resultfrequency:
            resultfrequency = store[ele]
            resutchar = ele
print(resultchar,resultfrequency)






~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



input:
abcdeabcde
