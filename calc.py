#simple div

str_input = input("Plese type command a + b or a - b: ")

str_a = ''
str_b = ''
operation = ''
'''
2+3
2^3
0.5-4
'''
for letter in str_command:
    print(letter)
    if letter == '+' or letter == '-' or letter == '*'or letter == '-' or letter == '/' or letter == '^':
        operatin = letter
    else:
        if operation == '':
            str_a = str_a + letter
        else:
            str_b = str_b + letter

str_a = str_a.strip()
str_b = str_b.strip()           
print(str_a)
print(str_b)        

#str_input = input("a: ")

a = float(str_input)
#print(type(a))

operation = input ("+ / * - ^: ")

str_input2 = input("b: ")
b = float(str_input2)
#print(type(b))
result = None

if operation == '+':
 result = a / b
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