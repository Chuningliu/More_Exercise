# STRONG PASSWORD

# password=int(input("Enter the password:"))
# if len(password)<=6:
#     if "$" in password or "@" in password or "#"  in password:
#         if "0"or "9" in password:
#             if "A"or"Z" in password:
#                 print("Strong password")
#             else:
#                 print("Weak password")
#         else:
#             print("Wrong password")
#     else:
#         print("Wrong")
# else: 
#     print("yuyiuyliyi")
l, u, p, d = 0, 0, 0, 0
s = "R@m@_f0rtu9e$"
if (len(s) >= 8):
    for i in s:
  
        # counting lowercase alphabets 
        if (i.islower()):
            l+=1            
  
        # counting uppercase alphabets
        if (i.isupper()):
            u+=1            
  
        # counting digits
        if (i.isdigit()):
            d+=1            
  
        # counting the mentioned special characters
        if(i=='@'or i=='$' or i=='_'):
            p+=1           
if (l>=1 and u>=1 and p>=1 and d>=1 and l+p+u+d==len(s)):
    print("Valid Password")
else:
    print("Invalid Password")

# num=int(input("Enter the number:"))
# n=str(num)
# i=-1
# s=""
# while i>=-len(n):
#     a=n[i]
#     s+=a
#     i-=1
# print(int(s))