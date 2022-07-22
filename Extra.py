# Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers. 0 is neither positive nor negative.
# If the input is an empty array or is null, return an empty array.
# , you should return [10, -65].

# a=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]
# pos=0
# neg=0
# b=[]
# for i in a:
#     if i>0:
#         pos+=1
#     if i<0:
#         neg+=i
#     if i not in a:
#         print("[]")
# print([pos,neg])    


# Your boss decided to save money by purchasing some cut-rate optical 
# character recognition software for scanning in the text of old novels to 
# your database. At first it seems to capture words okay, but you quickly 
# notice that it throws in a lot of numbers at random places in the text.
# Examples (input -> output)
# '! !'                 -> '! !'
# '123456789'           -> ''
# 'This looks5 grea8t!' -> 'This looks great!'
# Your harried co-workers are looking to you for a solution to take this garbled 
# text and remove all of the numbers. Your program will take in a string and clean 
# out all numeric characters, and return a string with spacing and special
# characters ~#$%^&!@*():;"'.,? all intact.

# a="Ningmeih123"
# for i in a:
#     if i.isdigit():
#         del i
#     else:
#         print(i,end="")
    
# Convert number to reversed array of digits
# Given a random non-negative number, you have to return the digits of this number within an array in reverse order.
# 348597 => [7,9,5,8,4,3]
# 0 => [0]

# def rev(a):
#     b=[]
#     while a>= 1:
#         b.append(a%10)
#         a//= 10
#     return b
# print(rev(348597))


# Complete the function which converts a binary number (given as a string) 
# to a decimal number.

# n=12
# div=4
# i=1
# sum=0
# while i<=n:
#     c=i%div
#     sum+=c
#     i+=1
# print(sum)
     

# def SumOfNumbers(l,n,k):
#     l.sort()
#     max=l[k-1]
#     min=l[-k]
#     sum=max+min
#     if max==min:
#         return sum*2
#     else:
#         return sum
# result = SumOfNumbers(l,n,k)
# print(result)



# n = int(input("Enter the number:"))
# if n%2!=0:
#     print("Weird")
# if n%2==0 and n<5 and n>2:
#     print("Not Weird")
# if n%2==0 and n<20 and n>6:
#     print("weird")
# if n%2==0 and n>20:
#     print("Not Weird")
    
    
# if n%2!= 0:
#     print ("Weird")
# else:
#     if n >=2 and n<= 5:
#         print ("Not Weird")
#     elif n>= 6 and n<= 20:
#         print ("Weird")
#     elif n> 20:
#         print ((("Not Weird")

# MATRIX
# x= int(input("Enter the first no.:-"))
# y= int(input("Enter the second no.:-"))
# z= int(input("Enter the third no.:-"))
# n= int(input("Enter the final no.:-"))
# c=[]
# for i in range(x+1):
#     for j in range(y+1):
#         for k in range(z+1):
#             if i+j+k!=n:
#                 b=[i,j,k]
#                 c.append(b)
# print(c)               
            


# a=[1,2,3,5,6,7,9]
# i=0
# c=[]
# j=i+1
# while i<len(a) and j<len(a):
#     if a[j]-a[i]!=1:
#         b=a[j]
#         c.append(b)
#     i+=1
#     j+=1
# print(c)
                

# b=[]       
# for i in range(a[0],a[-1]+1):
#         if i not in a:
#             b.append(i)
#             print(b)


# a=[1,2,3,5,6,7,9]
# i=0
# c=[]
# j=i+1
# while i<len(a) and j<len(a):
#     if a[j]-a[i]!=1:
#         b=a[j]
#         c.append(b)
#     i+=1
#     j+=1
# print(c)
# minimum=min(c)



# AREA OF A SQUARE AND PERIMETER OF A RECTANGLE

# a=int(input("Enter the first number:- "))
# b=int(input("Enter the second number:- "))
# if a==b:
#     print(a**2)
# else:
#     print(2*(a+b))



# ADD TWO NUMBERS

# a=int(input("Enter the number:- "))
# for i in range(a):
#     b=int(input("Enter the number:- "))
#     c=int(input("Enter the number:- "))
#     d=b+c
#     print(d)


# def find_volume(a_side, a_volume, b_side):
#     a=a_volume/a_side
#     return (a**3*b_side) 
# print(find_volume(4,8,10))     

    
 





























# words = s.split()
#     flag = False
#     for word in words:
#         if isinstance(word[0], str):
#             flag = True
#         else:
#             flag = False
    
#     if flag:
#         return s.title()
#     else:
#         pass

# s = input()
# print(solve(s))
    




            
        
        

        