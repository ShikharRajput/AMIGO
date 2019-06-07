usermessage = input("Enter the message : ")
a=''
b=''
for i in usermessage:
    #print(i)
    if i == "+":
        c=usermessage.index(i)
        a+=usermessage[0:c]
        b+=usermessage[c+1:]
        #print(a,b)
        print(int(a)+int(b))

    if i == "-":
        c=usermessage.index(i)
        a+=usermessage[0:c]
        b+=usermessage[c+1:]
        #print(a,b)
        print(int(a)-int(b))

    if i == "*":
        c=usermessage.index(i)
        a+=usermessage[0:c]
        b+=usermessage[c+1:]
        #print(a,b)
        print(int(a)*int(b))

    if i == "/":
        c=usermessage.index(i)
        a+=usermessage[0:c]
        b+=usermessage[c+1:]
        #print(a,b)
        print(int(a)/int(b))
