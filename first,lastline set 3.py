def readfirstlastline():
    f=open("Corona.txt","r")
    contents=f.readlines()
    print("\nNumber of lines in the file are:",len(contents))
    print("First line:",contents[0],end='')
    print("Last line:",contents[len(contents)-1])
    f.close()

def startwith():
    f=open("Corona.txt","r")
    contents=f.readlines()
    count=0
    print("\nLines start with 'O' or 'o' in file")
    for line in contents:
        if line[0]=='O' or line[0]=='o':
            count=count+1
            print(line,end='')
    print("\nNo. of lines start with('O' or 'o') are::",count)

def endwith():
    f=open("Corona.txt","r")
    contents=f.readlines()
    count=0
    print("\nLines end with 'a' in file")
    for line in contents:
        if line[-2]=='a':
            count=count+1
            print(line,end='')
    print("No. of lines end with 'a' are::",count)
    f.close()

readfirstlastline()
startwith()
endwith()
