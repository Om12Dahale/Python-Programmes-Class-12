import mysql.connector as ms 
mycon=ms.connect(host="localhost",user="root",passwd="tiger",database="sl")
if mycon.is_connected()==False:
    print("Error connecting to mysql database")
mycursor=mycon.cursor()

def displayall():
    mycursor.execute("select * from teacher")
    data=mycursor.fetchall()
    count=mycursor.rowcount
    print("Total number of rows retrived in resultset:",count)
    print("Records of teacher table are:")
    for row in data:
        print(row)

    
def searchtid():
    tid=int(input("\n Enter tearcher id of the teacher::"))
    query="select * from teacher where T_ID="+str(tid,)
    mycursor.execute(query)
    data=mycursor.fetchone()
    if data!=None:
        print(data)
    else:
        print("\n No teacher with T_ID number:",tid)

def searchdeptage():
    tdept=input("\n Enter the department to search::")
    tage=int(input("\n Enter the age criteria to search::"))
    query="select * from teacher where department=%s and age=%s"%(tdept,tage)
    mycursor.execute(query)
    data=mycursor.fetchall()
    count=mycursor.rowcount
    print("Total records of department",tdept,"and age=",tage,"are=",count)
    print("Retrived records:")
    if data!=None:
        for row in data:
            print(row)
    else:
        print("\n No matching records found")

def searchdeptsal():
    dept=input("\n Enter the department to search::")
    tsalary=int(input("\n Enter salary of the teacher to search::"))
    query="select * from teacher where department='{department}'\
        and salary>={salary}".format(salary=tsalary,department=dept)
    mycursor.execute(query)
    data=mycursor.fetchall()
    count=mycursor.rowcount
    print("Total records of",dept,"with salary greater than",tsalary,"are=",count)
    print("Retrived records:")
    if data!=None:
        for row in data:
            print(row)
    else:
        print("\n No matching records found")

def menu():
    print("\n Menu")
    print("1. Display all records")
    print("2. Search record using + operator")
    print("3. Search record using %s")
    print("4. Search record using format{}")

op="y"
while(op=="y"):
    menu()
    choice=int(input("Enter your Choice::"))
    if(choice==1):
        displayall()
    if(choice==2):
        searchtid()
    if(choice==3):
        searchdeptage()
    if(choice==4):
        searchdeptsal()
    op=input("Do ypu want to continue::")

