#Coding Exercise 3

#Problem 1
print("Problem 1:")
print('Hello World'[8])
print("")

#Problem 2
print("Problem 2:")
print('thinker'[2:5])
s = 'hello'
print(s[1])
print("")

#Problem 3
print("Problem 3:")
s = 'Sammy'
print(s[2:])
print("")

#Problem 4
print("Problem 4:")
print(list('Mississippi'))
print("")

#Problem 5
print("Problem 5:")
count = int(input())
phrases = []
while count > 0:
    phrase = input()
    stringFilter = filter(str.isalnum, phrase)
    phrase = "".join(stringFilter).lower()
    phrases.append(phrase)
    count-=1

answers = []
for p in phrases:
    index = 0
    counter = -1
    midpoint = int(len(p)/2)
    flag = 1
    while index <= midpoint:
        if p[index] != p[counter]:
            answers.append('N')
            flag = 0
            break  
        index+=1
        counter-=1
    if flag == 1:
        answers.append('Y')

print("answer:")
print(" ".join(answers))