import mysql.connector as sqltor
mycon=sqltor.connect(host="localhost",user="root",passwd="tiger",database="School")
mycur=mycon.cursor()

def displayall():
    mycur.execute("Select * from teacher")
    data=mycur.fetchall()
    count=mycur.rowcount
    print("Total number of rows reteived from resultant::",count)
    for row in data:
        print(row)

def deletrec():
    print("\nDELETE FROM TABLE")
    print("\nRecords of teacher table before deletion")
    displayall()
    dept=input("Enter teacher department whose record you want to delete::")
    data1=(dept,)
    delquery="DELETE FROM teacher WHERE department=%s"
    mycur.execute(delquery,data1)
    count=mycur.rowcount
    if count==0:
        print("Sorry! teacher department not found in table")
    else:
        mycon.commit()
        print("Rows affected::",mycur.rowcount)
        print("\nRecords of teacher table after deletion:")
        displayall()

def menu():
    print("\nMenu")
    print("1. Dispaly all records")
    print("2. Delete record")

op="y"
while(op=="y"):
    menu()
    choice=int(input("Enter your choice::"))
    if(choice==1):
        displayall()
    if(choice==2):
        deletrec()
    op=input("Do you want to continue::")