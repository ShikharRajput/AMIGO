def main():
    import webbrowser,os
    z=""
    while "TURE":
        usermessage = input("Enter your message : ")
        usermessage = usermessage.lower()
        web=usermessage.split()
        #print(web)

        for i in web:
            if i=="open":
                a=web.index(i)
                #print(a)
                for j in range(a+1,len(web)):
                    if j == len(web)-1:
                        z+= web[j]
                    else:
                        z+=web[j]+" "
                print(z)
                #w=web.split()[a+1:]
                #print(w)
                #os.startfile("Mozilla Firefox")
                webbrowser.open(z+'.com')
        else:
            webbrowser.open(usermessage)
            break
    


