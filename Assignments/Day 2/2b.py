#Coding Exercise 4:

#Problem 1
print("Problem 1:")
print([1, "two", 3.0])
print("")

#Problem 2
print("Problem 2:")
nested = [1,1,[1,2]]
print(nested[2][1])
print("")

#Problem 3
print("Problem 3:")
lst = ['a', 'b', 'c']
print(lst[1:])
print("")

#Problem 4
print("Problem 4:")
dict = {"Monday":1, "Tuesday":2, "Wednesday":3, "Thursday":4, "Friday":5, "Saturday":6, "Sunday":7}
print(dict)
print("")

#Problem 5
print("Problem 5:")
d = {'k1':[1,2,3]}
print(d['k1'][1])
print("")

#Problem 6
print("Problem 6:")
l = [1,[2,3]]
tup = tuple(l)
print(tup)
print("")

#Problem 7
print("Problem 7:")
print(list('Mississippi'))
print("")

#Problem 8
print("Problem 8:")
miss = list('Mississippi')
miss.append('X')
print(miss)
print("")

#Problem 9
print("Problem 9:")
tmp = ([1,1,2,3])
print(tmp)
print(([1,1,2,3]))
print("")
print("")
print("")

#Question
print("Question 1:")
answers = []
for num in range(2000, 3201):
    if num%7 == 0 and num%5 != 0:
        answers.append(str(num))
print(",".join(answers))
print("")

#Question 2
print("Question 2:")
value = int(input())
product = 1
while value > 0:
    product *= value
    value -= 1
print(product)
print("")

#Question 3
print("Question 3:")
max = int(input())
d = {}
for i in range(1, max+1):
    d[i] = i*i
print(d)
print("")

#Question 4
print("Question 4:")
lst = input().split(',')
tup = tuple(lst)
print(lst)
print(tup)
print("")

#Question 5
print("Question 5:")
class StringStuff:
    s = ""

    def getString(self):
        self.s = input()

    def printString(self):
        print(self.s)

ss = StringStuff()
ss.getString()
ss.printString()
ss.getString()
ss.printString()
print("")