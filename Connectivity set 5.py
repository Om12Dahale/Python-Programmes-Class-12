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

def updaterec():
    sal=int(input("Enter new salary::"))
    updatequery="UPDATE teacher SET salary=salary+%s"%(sal)
    mycur.execute(updatequery)
    data=mycur.fetchall()
    mycon.commit()
    print("rows affected::",mycur.rowcount)
    print("Records after updation::")
    displayall()

    
def menu():
    print("\nMenu")
    print("1. Dispaly record before updation")
    print("2. Update Record")
    
op="y"
while(op=="y"):
    menu()
    choice=int(input("Enter your choice::"))
    if(choice==1):
        displayall()
    if(choice==2):
        updaterec()
    op=input("Do you want to continue::")

   