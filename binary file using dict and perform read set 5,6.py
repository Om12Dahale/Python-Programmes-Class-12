import pickle
def readfile():
    print("Contents of the file:")
    with open("employee.txt","rb+") as f:
        while True:
            try:
                r=pickle.load(f)
                print(r)
            except EOFError:
                break
        f.close()

def createfile():
    myfile=open("employee.txt","wb")
    n=int(input("\nHow many records do you write:"))
    for i in range(n):
        eno=int(input("Enter employee no:"))
        enm=input("Enter employee name:")
        esal=int(input("Enter Salary:"))
        rec={'Empno':eno,'Empname':enm,'Salary':esal}
        pickle.dump(rec,myfile)
    myfile.close()


def appendfile():
    myfile=open("employee.txt","ab")
    n=int(input("\nHow many records do you want to append::"))
    for i in range(n):
        eno=int(input("Enter employee no:"))
        enm=input("Enter employee name:")
        esal=int(input("Enter Salary:"))
        rec={'Empno':eno,'Empname':enm,'Salary':esal}
        pickle.dump(rec,myfile)
    myfile.close()

def countrec():
    f=open("employee.txt","rb")
    num=0
    print("\nDetails of employees with salary between 20000 and 40000")
    while True:
        try:
            rec=pickle.load(f)
            if rec['Salary']>=20000 and rec['Salary']<=40000:
                print(rec)
                num=num+1
        except EOFError:
                break
    f.close()
    return num

ans="y"
while ans=="y":
    print("\nMenu")
    print("1. Create a binary file")
    print("2. Read records from binary file")
    print("3. Append records to binary file")
    print("4. Count and display records from binary file")
    ch=int(input("Enter your choice:"))
    if ch==1:
        createfile()
    elif ch==2:
        readfile()
    elif ch==3:
        appendfile()
    elif ch==4:
        countrec()
    elif ch==5:
        break
    else:
        print("Invalid option")
    ans=input("Do you want to continue:")
