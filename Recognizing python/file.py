num1 = 42               #variable declaration
num2 = 2.3              #variable declaration
boolean = True          #variable declaration
string = 'Hello World'  #variable declaration
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']  #variable declaration
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #variable declaration
fruit = ('blueberry', 'strawberry', 'banana') #variable declaration
print(type(fruit))   #log statement
print(pizza_toppings[1]) #log statement
pizza_toppings.append('Mushrooms') #list add value
print(person['name'])  #log statement
person['name'] = 'George'  #dictionary change value
person['eye_color'] = 'blue' #dictionary change value 
print(fruit[2])  #log statement 

if num1 > 45:               #conditional if / print
    print("It's greater")
else:                        #conditional else / print
    print("It's lower")

if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:      #conditional else if / print
    print("It's a long word!")
else:
    print("Just right!")

for x in range(5):      #for loop , 0 to 5
    print(x)
for x in range(2,5):    #for loop , 2 to 5
    print(x)
for x in range(2,10,3): #for loop , 2 to 10 , increments by 3
    print(x)
x = 0                   #variable declaration
while(x < 5):           #while loop 
    print(x)            #log statement
    x += 1              #increment

pizza_toppings.pop()    #delete last value
pizza_toppings.pop(1)   #delete selected value

print(person)           #log statement
person.pop('eye_color') #dictionary delete value
print(person)           

for topping in pizza_toppings:         #for loop start
    if topping == 'Pepperoni':        #conditional if
        continue
    print('After 1st if statement')  #log statement
    if topping == 'Olives':           #conditional if  
        break                          #for loop stop

def print_hello_ten_times():           #function declaration
    for num in range(10):               #for loop 0 to 10
        print('Hello')                  #log statement

print_hello_ten_times()                 #calling function

def print_hello_x_times(x):             #function declaration
    for num in range(x):                #for loop
        print('Hello')                  #log statement

print_hello_x_times(4)                  #executing the function with 4 as an entry

def print_hello_x_or_ten_times(x = 10): 
    for num in range(x): #for loop until x/10
        print('Hello')  #log statement

print_hello_x_or_ten_times()    #executing function with 10
print_hello_x_or_ten_times(4)   #executing function with 4


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)