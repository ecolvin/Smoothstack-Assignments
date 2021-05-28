#Coding Exercise 7

#Problem 1
print("Problem 1:")
answers = []
for num in range(1500, 2701):
    if num%7 == 0 and num%5 == 0:
        answers.append(str(num))
print(",".join(answers))
print("")

#Problem 2
print("Problem 2:")
def toCelsius(temp):
    return int((temp-32)*(5/9))

def toFahrenheit(temp):
    return int((temp*(9/5))+32)

print("60 degrees Celsius is " + str(toFahrenheit(60)) + " in Fahrenheit")
print("45 degrees Fahrenheit is " + str(toCelsius(45)) + " in Celsius")
print("")

#Problem 3
from random import randint
print("Problem 3:")
num = randint(1,9)
print("Guess a number between 1 and 9:")
guess = input()
while(guess != str(num)):
    print("That is incorrect. Please try again.")
    print("Guess a number between 1 and 9:")
    guess = input()
print("Well guessed!")
print("")

#Problem 4
print("Problem 4:")
line = ""
for i in range(1, 10):
    line = ""
    if(i <= 5):
        for j in range(1, i+1):
            line += '*'
    else:
        for j in range(1, 6-(i-5)):
            line += '*'
    print(line)
print("")

#Problem 6
print("Problem 6:")
word = input();
newWord = ""
for c in word:
    newWord = c + newWord
print(newWord)
print("")

#Problem 7
print("Problem 7:")
numbers = (1,2,3,4,5,6,7,8,9)
count = 0
for n in numbers:
    if(n%2 == 0):
        count+=1

print("Number of even numbers: " + str(count))
print("Number of odd numbers: " + str((len(numbers)-count)))
print("")

#Problem 8
print("Problem 8:")
datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0,-1), [5,12], {"class":'V',"section":'A'}]

for d in datalist:
    print("data: " + str(d) + "; type: " + str(type(d)))

print("")

#Problem 9
print("Problem 9:")
for i in range(0, 7):
    if(i == 3 or i == 6):
        continue
    print(i, end=" ")
print("")