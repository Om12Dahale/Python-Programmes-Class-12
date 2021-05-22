import mysql.connector as sqltor
mycon=sqltor.connect(host="localhost",user="root",passwd="tiger")
mycur=mycon.cursor()

def displayall():
    mycur.execute("select * from student")
    data=mycur.fetchall()
    count=mycur.rowcount
    print("Total number of rows retrived in resultset:",count)
    for row in data:
        print(row)

def displaymany(n):
    mycur.execute("select * from student")
    data=mycur.fetchmany(n)
    count=mycur.rowcount
    print("Total number of rows retrived in resultset:",count)
    for row in data:
        print(row)

def menu():
    print("\n Menu")
    print("1. Add records using static data")
    print("2. Add records using custom data")
    print("3. Display records")

def insertstatic():
    inquery="INSERT INTO student(rollno,Name,marks,section,project)\
         VALUES('{}','{}','{}','{}','{}')".format(101,'Ruhani',76.80,'A','Pending')
    mycur.execute(inquery)
    mycon.commit()
    print("\n INSERT ROW INTO TABLE")
    print("Record added sucessfully")
    displayall()

def insertcustom():
    print("\n INSERT ROW INTO TABLE")
    ch='y'
    while (ch=='y'):
        rn=int(input("enter rollno::"))
        nm=input("Enter the name of the student::")
        marks=float(input("Enter marks::"))
        section=input("enter the section::")
        project=input("enter the project status::")
        inrow=(rn,nm,marks,section,project)
        inquery="INSERT INTO student(rollno,Name,marks,section,project)\
            VALUES(%s,%s,%s,%s,%s)"
        mycur.execute(inquery,inrow)
        print("record added sucessfully")
        ch=input("Do you want to insert more records::")
        displayall()

mycur.execute("drop database school")
mycur.execute("create database school")
mycur.execute("use school")

query="create table student(rollno int,Name varchar(10),marks float(4,2),\
    section char(1),project varchar(15))"
mycur.execute(query)
print("Table created successfully")
mycur.execute("desc student")
print("Structure of the created table")
for x in mycur:
    print(x)


op="y"
while(op=="y"):
    menu()
    choice=int(input("enter your choice::"))
    if(choice==1):
        insertstatic()
    if(choice==2):
        insertcustom()
    if(choice==3):
        totrow=int(input("how many records you want to read from table student::"))
        displaymany(totrow)
    op=input("Do you want to continue::")

mycur.execute("drop table student")
mycon.close()




  
