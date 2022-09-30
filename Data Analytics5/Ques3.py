# Q3
username = 'xyz@domain.com'
password = 'somename'
a = input("Enter Username : ")
b = input("Enter Password : ")
count = 0
while((a!=username) | (b!=password)):
    count+=1
    print("Wrong!!!")
    print()
    a = input("Enter Username : ")
    b = input("Enter Password : ")
print(f"It took {count+1} times to enter the correct email & password!!")