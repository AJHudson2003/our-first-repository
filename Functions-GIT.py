# 4.13.3: greetings
# Aj Hudson
# 2.6.19
name = input("What is your name: ")
def greeting():
    print(" hi there " + name + "!")
    print("nice to meet you")

greeting()

# 4.13.4: Functions and Variables
# AJ
# 2.14.19
x = 676867

def print_something():
    x = 15
    print(x)

print_something()

print(x)

# 4.13.5: functions and variables pt2
# aj
# 2.14.19
my_variables = 4.5659

def something():
    print(my_variables + 10)

something()

# 4.13.6: functions & Variables pt 3
# 2.18.19
# aj hudson
def print_number(x):
    print(str(x))
print_number(15)
print_number('\n' + "hello their")

#  4.14.4. name and age
# aj / 2.18.19
def name_age(name, age):
    print('\n' 'helllo their, my name is ', name,  ' also i am ', str(age), 'years old.')
name_age('AJ Hudson', 15)
name_age('jeff', 44)
name_age("james", 33)

# 4.14.5: default parameter values
# aj 2.19.19
def print_two_numbers(x, y = 20):
    print('first number: ', x)
    print('second number: ', y)
print_two_numbers(15, 36)
print_two_numbers(56)

# 4.14.7 print multiple times
# aj 2.19.19
def print_multiple_times(string, times):
    for i in range(times):
        print(string)

print_multiple_times('I like games', 5)

# 4.14.7 print multiple times
# aj 2.19.19
def print_multiple_times(string, times):
    for i in range(times):
        print(string)

print_multiple_times('I like games', 5)

# 4.16.3: enter a number
# 2.20.19
# AJ hudson

try:
    my_number = int(input('enter an number: '))
    print('your number: ' + str(my_number))
except ValueError:
    print('that was not an integer')
