
1.
solution:-
    word = input()
    n = len(word)
    # n = 8
    # 0 1 2 3 4 5 
    for index in range(0, n, 2):
        print(word[index], end = " ")
 
 
 
2. 
solution:-
    word = input()
    vowels = "aeiou"
 
    for ch in word:
        if ch not in vowels:
            print(ch)
 
 
3. 
solution:-
    word = input()
    reverseWord = word[::-1]
    if word == reverseWord:
        print("Palindrome")
    else:
        print("Not a palindrome")
 
 
 
 
4.
 # abcDEF@#def 
 no.of upper-case characters: 3
 no.of lower-case characters: 6
 no.of special characters: 2 
 
 solution:-
     word = input()
     upperCount, lowerCount, specialCount = 0, 0, 0
     for ch in word:
         # some logic 
         if ch.isalpha():
             if ch.islower():
                 lowerCount += 1 
             else:
                 upperCount += 1 
         else:
             specialCount += 1 
 
     print("no.of upper-case characters", upperCount)
     print("no.of lower-case characters", lowerCount)
     print("no.of special characters", specialCount)
 
 
 
 
 
 
 
5.
 
solution:-
word = input()
result = 0 
n = len(word)
# n = 8
 
for index in range(n - 1):
    if word[index] == 'a' and word[index + 1] == 'b':
        result += 1 
 
print(result)
 
 
