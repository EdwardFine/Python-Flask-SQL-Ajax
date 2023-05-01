num1 = 42 #Variable Declaration, number
num2 = 2.3 # Variable declaration, number
boolean = True # variable declaration, boolean
string = 'Hello World' #Variable declaration, string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #variable declaration, initialize list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #Variable declaration, initialize dictionary
fruit = ('blueberry', 'strawberry', 'banana') #Variable declaration, initialize Touple
print(type(fruit)) #Type check of touple
print(pizza_toppings[1]) # Accessing list value
pizza_toppings.append('Mushrooms') # Adding list value
print(person['name']) # Accessing Dictionary Value
person['name'] = 'George' # Changing dictionary value
person['eye_color'] = 'blue'# Adding dictionary value
print(fruit[2]) # Accessing touple value

if num1 > 45: #if conditional
    print("It's greater") #Log statement
else: # else conditional
    print("It's lower") # Log statement

if len(string) < 5: # length check, if conditional
    print("It's a short word!") # log statement
elif len(string) > 15: # length check, else if conditional
    print("It's a long word!")# log statement
else: # else conditional
    print("Just right!") # log statement

for x in range(5): # For loop stop
    print(x) # log statement, continue for loop
for x in range(2,5): # For loop start, stop
    print(x)
for x in range(2,10,3):# For loop start, stop, increment 
    print(x) # Log statement
x = 0 # variable declaration,while loop start
while(x < 5): # while loop stop
    print(x) # log statement
    x += 1 # while loop increment

pizza_toppings.pop() # delete list value
pizza_toppings.pop(1) # delete list value

print(person) # log statement
person.pop('eye_color') # delete dictionary value
print(person) # log statement

for topping in pizza_toppings: # for loop start, stop, increment
    if topping == 'Pepperoni':# if conditional
        continue # for loop continue
    print('After 1st if statement') # log statement
    if topping == 'Olives': #if conditional
        break # for loop break

def print_hello_ten_times(): #function declaration
    for num in range(10): # For loop stop
        print('Hello')# log statment

print_hello_ten_times() # function usage

def print_hello_x_times(x): # function declaration, parameters
    for num in range(x):#for loop stop
        print('Hello')# log statement

print_hello_x_times(4) # function usage with parameter

def print_hello_x_or_ten_times(x = 10): # function declaration, argument
    for num in range(x): # for loop stop
        print('Hello')# log statment

print_hello_x_or_ten_times() # function usage, print via argument
print_hello_x_or_ten_times(4) # function usage, print via parameter


"""
Bonus section
"""

# print(num3) --- NameError
# num3 = 72 --- Variable declaration.
# fruit[0] = 'cranberry' --- TypeError
# print(person['favorite_team']) --- KeyError
# print(pizza_toppings[7]) --- IndexError
#   print(boolean) --- IndentationError
# fruit.append('raspberry') --- AttributeError
# fruit.pop(1) --- AttributeError