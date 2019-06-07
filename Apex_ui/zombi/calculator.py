import math
usermessage = input("Enter your message : ")
operation = usermessage.split()[0]
operation2=usermessage.split()[1]
operand1 = int(usermessage.split()[1])
operand2= int(usermessage.split()[3])
#operand3=    (usermessage.split()[4])
if operation=='add':
    Addition=operand1+operand2
    print(Addition)
elif operation=='multiply':
    Multiplication=operand1*operand2
    print(Multiplication)
elif operation=='divide':
    divide=operand1/operand2
    print(divide)



