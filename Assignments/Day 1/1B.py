#Coding Exercise 2:

#Problem 1
print ("Problem 1:")
print (50+50)
print (100-10)
print ("")

#Problem 2
print ("Problem 2:")
print (30+0*6)
print (6^6)
print (6**6)
print (6+6+6+6+6+6)
print ("")

#Problem 3
print ("Problem 3:")
print ("Hello World")
print ("Hello World : 10")
print ("")

#Problem 4
print ("Problem 4:")
def months(loan, rate, desired, min, max):
    loan2 = loan
    median = int((min + max) / 2)
    monthCount = 0
    while loan2 > 0:
        interest = loan2 * rate
        loan2 += interest
        loan2 -= median
        monthCount+=1
    if(monthCount == desired):
        return median
    elif (monthCount < desired):
        return months(loan, rate, desired, min, median)
    else:
        return months(loan, rate, desired, median, max)

userInput = input()
splitInput = userInput.split()

loan = int(splitInput[0])
rate = (int(splitInput[1])/12)/100
desired = int(splitInput[2])

print ("answer:")
print (months(loan, rate, desired, 1, loan))