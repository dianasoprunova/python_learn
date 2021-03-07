#simple div
str_input = input("a: ")

a = float(str_input)
#print(type(a))

operation = input ("+ / * - ^: ")

str_input2 = input("b: ")
b = float(str_input2)
#print(type(b))
result = None

if operation == '+':
 result = a + b
#print(type(result))
elif operation == '/':
    if b != 0: 
        result= a / b
    else:
        result= 'inf'
elif operation == '-':
 result = a - b
elif operation == '*':
 result = a * b
elif operation == '^':
 result = a ** b

else:
 result = "unknown"
#print(type(result))

print("Result: " + str(result))