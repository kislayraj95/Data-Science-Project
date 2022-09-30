# Q4
fname = input("Enter the filename : ")

f = open(fname, "r")
a = []
while(True):
    a.append(f.readline())
    if(a[-1]==''):
        a.pop()
        break
a = [int(i) for i in a]
ans = [round(i*3.78541,4) for i in a]
print("1. To save output in a file : ")
print("2. To Display the output : ")
choice = int(input("\nEnter your choice : "))
if(choice==1):
    f1 = open("Output.txt", "a")
    for i in ans:
        f1.write(str(i))
        f1.write('\n')
    f1.close()
    print("File Created, Check your directory with name \"Output.txt\"!!!")
else:
    for i in ans:
        print(i)