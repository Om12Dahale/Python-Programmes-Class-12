import mysql.connector as sqltor
mycon=sqltor.connect(host="localhost",user="root",passwd="tiger",database="school")
mycur=mycon.cursor()

def displayall():
    mycur.execute("Select * from teacher")
    data=mycur.fetchall()
    count=mycur.rowcount
    print("Total number of rows retrived from resultant::",count)
    for row in data:
        print(row)

def searchtid():
    tid=int(input("\nEnter teacher id to search::"))
    query="select * from teacher Where Tid="+str(tid,)
    mycur.execute(query)
    data=mycur.fetchone()
    if data!=None:
        print(data)
    else:
        print("\nNo teacher with Tid number:",tid)

def menu():
    print("\n MENU")
    print("1. Display all records")
    print("2. Search record")

op="y"
while(op=="y"):
    menu()
    choice=int(input("Enter your choice::"))
    if(choice==1):
        displayall()
    if(choice==2):
        searchtid()
    op=input("Do you want to Continue::")