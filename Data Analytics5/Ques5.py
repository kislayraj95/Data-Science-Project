# Q5
iban = input("Enter the IBAN : ")
if(len(iban)!=22):
    while(len(iban!=22)):
        print("The Entered IBAN is not of length 22!!!")
        iban = input("Re-Enter the IBAN : ")
for i in range(22):
    if((i==2) or (i==4) or (i==8) or (i==14)):
        print(" ",end="")
        print(iban[i],end="")
    else:
        print(iban[i],end="")