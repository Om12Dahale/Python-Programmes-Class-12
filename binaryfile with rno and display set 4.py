import pickle
def createfile():
    f=open("student.txt","wb")
    studentlist=[]
    ans='y'
    while ans=='y':
        print()
        Rollno=int(input("Enter Rollno:"))
        Sname=input("Enter Name::")
        rec=[Rollno,Sname]
        studentlist.append(rec)
        ans=input("Do you want to add more(y/n)::")
    pickle.dump(studentlist,f)
    f.close()

def readfile():
    print("\nContents of the file:")
    with open("student.txt","rb") as f:
        while True:
            try:
                r=pickle.load(f)
                print(r)
            except EOFError:
                break
    return r
    f.close()

def searchRec():
    fobj=open("student.txt","rb")
    rec=readfile()
    print()
    ans='y'
    while ans=="y":
        flag=False
        print()
        rno=int(input("Enter roll number to search::"))
        for s in rec:
            if s[0]==rno:
                print("Record found!!! \n Rollno:",s[0],"Name::",s[1])
                flag=True
                break
        if flag==False:
            print("Sorry! Roll number",rno,"not found in the file")
        ans=input("Do you want to search other record(y/n)::")
    fobj.close()

createfile()
searchRec()



