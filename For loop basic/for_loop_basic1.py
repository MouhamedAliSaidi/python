#Basic - Print all integers from 0 to 150.
print("basic print all integers")

for i in range(150):
    print(i)

#Multiples of Five - Print all the multiples of 5 from 5 to 1,000
print("Multiplies of five")

for i in range(5, 1000, 5):
    print(i)


#Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
print("print integers")

for i in range(1, 100):
    if i % 10 == 0:
        print("Coding Dojo")
    elif i % 5 == 0:
        print("Coding")
    else:
        print(i)


#Whoa. That Sucker's Huge
print("whoa")
sum_odds = 0
for i in range(1, 500001, 2): 
    sum_odds += i
print(sum_odds)

#countdown by fours
print("countdown by fours")
for i in range(2018, 0, -4):  
    print(i)

#Flexible Counter
print("flexible counter")
lowNum = 11
highNum = 19
mult = 3
for i in range(lowNum, highNum + 1):
    if i % mult == 0:
        print(i)
