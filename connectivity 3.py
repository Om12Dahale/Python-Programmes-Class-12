import mysql.connector as sqltor
mycon=sqltor.connect(host="localhost",user="root",passwd="tiger",database="sl")
mycur=mycon.cursor()

def displayall():
    mycur.execute("select * from teacher")
    data=mycur.fetchall()
    count=mycur.rowcount
    print("Total numbers of rows retrived in resultset::",count)
    for row in data:
        print(row)

def displayone(tid):
    mycur.execute("select * from teacher where T_ID=%s" %(tid,))
    data=mycur.fetchone()
    print(data)

def menu():
    print("\nMenu")
    print("1. display record")
    print("2. Delete record")
    print("3. Update record")

def deleterec():
    print("\nDelete Row From Table")
    print("\nRecords of teacher table before deletion:")
    displayall()
    tid=int(input("\nEnter teacher id whose record you want to delete::"))
    data1=(tid,)
    delquery="DELETE FROM teacher WHERE T_ID=%s"
    mycur.execute(delquery,data1)
    count=mycur.rowcount
    if count==0:
        print("Sorry! teacher id not found")
    else:
        mycon.commit()
        print("Rows affected::",mycur.rowcount)
        print("\nRecords of tacher table after deletion:")
        displayall()

def updaterec():
    print("\nUPDATE ROW FOR TABLE")
    print("\nRecords of teacher table before updation:")
    tid=int(input("Enter teacher id whose record you want to UPDATE::"))
    query="select * from teacher where T_ID=%s"%(tid)
    mycur.execute(query)
    result=mycur.fetchall()
    if mycur.rowcount==0:
        print("Sorry! Teacher with",tid,"not found")    
    else:
        for row in result:
            print(row)
        print("You can change only department and salary")
        dept=input("Enter new department,leave blank if not want to change::")
        if dept==' ':
            dept=str(row[3])
            print(dept)
        try:
            sal=int(input("Enter new salary,leave blank if not want to change::"))
        except:
            sal=row[5]
        updatequery="UPDATE teacher SET department='%s',salary=%s WHERE T_ID=%s"%(dept,sal,tid)
        mycur.execute(updatequery)
        mycon.commit()
        print("Rows affected::",mycur.rowcount)
        print("\nContents of updated record:")
        displayone(tid)

op='y'
while (op=='y'):
    menu()
    choice=int(input("\nEnter your choice::"))
    if(choice==1):
        displayall()
    if(choice==2):
        deleterec()
    if(choice==3):
        updaterec()
    op=input("Do you wabt to continue::")

mycon.close()

