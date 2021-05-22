import mysql.connector as sqltor
mycon=sqltor.connect(host="localhost",user="root",passwd="tiger")
mycur=mycon.cursor()

def displayall():
    mycur.execute("Select * from student")
    data=mycur.fetchall()
    count=mycur.rowcount
    print("Total number of rows retrived in resultant::",count)
    for row in data:
        print(row)

def menu():
    print("\nMENU")
    print("1. Add records using custom data")
    print("2. Display records")

def insertcustom():
    print("\n INSERT ROWS INTO TABLE")
    ch='y'
    while(ch=="y"):
        Rollno=int(input("enter rollno::"))
        Sname=input("Enter name of the student::")
        Marks=int(input("Enter marks::"))
        inrow=(Rollno,Sname,Marks)
        inquery="INSERT INTO student(Rollno,Sname,Marks)\
            VALUES(%s,%s,%s)"
        mycur.execute(inquery,inrow)
        print("Record added sucessfully")
        ch=input("Do you want to insert more records::")
        displayall()

mycur.execute("drop database school")
mycur.execute("create database school")
mycur.execute("use school")

query="create table student(Rollno int(3),Sname varchar(15),Marks int)"
mycur.execute(query)
print("Table created successfully")
mycur.execute("desc student")
print("Structure of the created table")
for x in mycur:
    print(x)

op="y"
while(op=="y"):
    menu()
    choice=int(input("Enter your choice::"))
    if(choice==1):
        insertcustom()
    if(choice==2):
        displayall()
    op=input("Do you want to continue::")

mycur.execute("drop table student")
mycon.close()
    