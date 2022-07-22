granted=False
def grant():
    global granted
    granted = True
def signup(name,password):
    success=False
    file=open("User_details.txt","r")
    for i in file:
        a,b=i.split(",")
        b=b.strip()
        if(a==name and b==password):
            success=True
            break
    file.close()
    if (success):
        print("Sign in successful")
        grant()
    else:
        ("Wrong username or password")
     
def login(name,password):
    file=open("User_details.txt","a")
    file.write("\n"+name+","+password)
    grant()
def access(choice):
    global name
    if (choice=="signin"):
        name=input("Enter your name:- ")
        password=input("Enter your password:- ")
        signup(name,password)
    else:
        print("Enter your name and password to log in:- ")
        name=input("Enter your name:- ")
        password=input("Enter your password:- ")
        login(name,password)
def start():
    global choice
    choice=input("Signup or Login :- ")
    if choice!="signup" and choice!="login":
        start()
start()
access(choice)
if (granted):
    print("Sign in Successful ")

    