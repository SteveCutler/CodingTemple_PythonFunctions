# Objective:
# The aim of this assignment is to build a basic calculator 
# that can perform addition, subtraction, multiplication, and division.

# Task 1: Create functions for each arithmetic operation.

def addition(*args):
    response  = 0
    for x in args:
        response += x
    return response
answer = addition(2,6,2)
print(answer)

def subtraction(*args):
    response  = 0
    for y in args:
        response -= y
    return response
answer = subtraction(10,6,2)
print(answer)

def multiplication(*args):
    response  = args[0]
    for z in args[1:]:
        response *= z
    return response
answer = multiplication(10,6,2)
print(answer)

def division(*args):
    response  = args[0]
    for z in args[1:]:
        response /= z
    return response
answer = division(10,6,2)
print(answer)



# Task 2: Implement user input to receive numbers and an operation choice.

numbers = input("Input as many numbers as you want, use this format: 1 7 23 12 etc.\n").split()
numList = []

for x in numbers:
    numList.append(float(x))

operation = input("Select a mathematical operation from this list: addition, subtraction, multiplication, division\n")

print(numList)
print(operation)

def addition(*args):
    response  = 0
    for x in args:
        response += x
    return response

def subtraction(*args):
    response  = 0
    for y in args:
        response -= y
    return response

def multiplication(*args):
    response  = args[0]
    for z in args[1:]:
        response *= z
    return response

def division(*args):
    response  = args[0]
    for z in args[1:]:
        response /= z
    return response

if operation == "addition":
    result = addition(*numList)
    print(f"the result is: {result}")
elif operation == "subtraction":
    result = subtraction(*numList)
    print(f"the result is: {result}")
elif operation == "multiplication":
    result = multiplication(*numList)
    print(f"the result is: {result}")
elif operation == "division":
    result = division(*numList)
    print(f"the result is: {result}")
else:
    print("Make sure you correctly enter one of the operations!")


# Task 3: Ensure your program can handle division by zero and other potential errors.
    
numbers = input("Input as many numbers as you want, use this format: 1 7 23 12 etc.\n").split()
numList = []
for x in numbers:
    try:
        numList.append(float(x))
    except:
        print(f"Make sure all entries are numbers! Removing {x} from your numbers list.")
        continue

operation = input("Select a mathematical operation from this list: addition, subtraction, multiplication, division\n")

def addition(*args):
    response  = 0
    for x in args:
        response += x
    return response

def subtraction(*args):
    response  = 0
    for y in args:
        response -= y
    return response

def multiplication(*args):
    response  = args[0]
    for z in args[1:]:
        response *= z
    return response

def division(*args):
    response  = args[0]
    for z in args[1:]:
        response /= z
    return response

if operation == "addition":
    result = addition(*numList)
    print(f"the result is: {result}")
elif operation == "subtraction":
    result = subtraction(*numList)
    print(f"the result is: {result}")
elif operation == "multiplication":
    result = multiplication(*numList)
    print(f"the result is: {result}")
elif operation == "division":
    for x in numList:
        if x == 0:
            print("You can't divide by 0!")
            break
        else:
            continue
    else:    
        result = division(*numList)
        print(f"the result is: {result}")
else:
    print(f"For operation type you entered: {operation}. Make sure you correctly enter one of the operations!")
