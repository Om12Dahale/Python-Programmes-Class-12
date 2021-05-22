import mysql.connector as sqltor
mycon=sqltor.connect(host="localhost",user="root",passwd="tiger",database="School")
mycur=mycon.cursor()

def displayall():
    mycur.execute("Select * from teacher")
    data=mycur.fetchall()
    count=mycur.rowcount
    print("Total number of rows retrived from resultant::",count)
    for row in data:
        print(row)

def searchsal():
    sal=int(input("Enter the salary of the teacher::"))
    query="select * from teacher where salary>'{Salary}'".format(Salary=sal)
    mycur.execute(query)
    data=mycur.fetchall()
    if data!=None:
        print(data)
    else:
        print("\nNo teacher with Salary",sal)

def menu():
    print("\nMENU")
    print("1. Display records")
    print("2. Search records")

op="y"
while(op=="y"):
    menu()
    choice=int(input("Enter the choice::"))
    if(choice==1):
        displayall()
    if(choice==2):
        searchsal()
    op=input("Do you want to continue::")
