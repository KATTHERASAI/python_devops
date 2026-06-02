import sys
def addition(a, b):
    add = a+b
    return add

def subtraction(a, b):
    sub = a-b
    return sub

a = float(sys.argv[1])
operation = sys.argv[2]
b = float(sys.argv[3])

# if operation == "add":
#     output = addition(a, b)
#     print(output)


# if operation == "sub":
#     output = subtraction(a, b)
#     print(output)

if operation == "add":
    output = addition(a, b)
elif operation == "sub":
    output = subtraction(a, b)

print(output)