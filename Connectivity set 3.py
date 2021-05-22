import mysql.connector as sqltor
mycon=sqltor.connect(host="localhost",user="root",passwd="tiger",database="school")
mycur=mycon.cursor()

def displayall():
    mycur.execute("Select * from teacher")
    data=mycur.fetchall()
    count=mycur.rowcount
    print("Total number of rows retrived in resultant::",count)
    for row in data:
        print(row)

def searchdept():
    dept=input("Enter the department of the teacher::")
    query="Select * from teacher where department='{department}'".format(department=dept)
    mycur.execute(query)
    data=mycur.fetchall()
    if data!=None:
        print(data)
    else:
        print("\nNo teacher with department",dept)

def menu():
    print("\nMENU")
    print("1. Display all records")
    print("2. Search records")

op="y"
while(op=="y"):
    menu()
    choice=int(input("Enter yor choice::"))
    if(choice==1):
        displayall()
    if(choice==2):
        searchdept()
    op=input("Do you want to continue::")
