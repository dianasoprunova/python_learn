#simple div

str_command = input("Plese type command a + b or a - b: ")

Znachenie1 = ''
str_A = ''

Znachenie2 = ''
str_B = ''

operation = ''

i = 0

while i < len(str_command):
    if str_command[i] == '+' or str_command[i] == '-' or str_command[i] == '*'or str_command[i] == '^' or str_command[i] == '/':
        if str_A == '':
            Znachenie1 = str_command[i]
        elif operation != '':
            Znachenie2 = str_command[i]
        else:
            operation = str_command[i]
    else:
        if operation == '':
            str_A += str_command[i]
        else:
            str_B = str_command[i]
            
    i += 1

str_A = Znachenie1 + str_A.strip()
str_B = Znachenie2 + str_B.strip()           
        

#str_input = input("A: ")

delimoe = float(str_A)
#print(type(delimoe))

#operation = input ("+ / * - ^: ")

#str_input2 = input("B: ")
delitel = float(str_B)
#print(type(delitel))
result = None

if operation == '/':
    if delitel == 0: 
        result= 'inf'
    else:
        result = delimoe / delitel
#print(type(result))
elif operation == '-':
 result = delimoe - delitel
elif operation == '+':
 result = delimoe + delitel
elif operation == '*':
 result = delimoe * delitel
elif operation == '^':
 result = delimoe ** delitel

else:
 result = "unknown"
#print(type(result))

print("Result: " + str(result))