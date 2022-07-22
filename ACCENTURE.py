# MERGE

# list1 = [1,2,4]
# list2 = [1,3,4]
# b=list1+list2
# c=sorted(b)
# print(c)


# DIVISIBILITY

# d=int(input("Enter for len:- "))
# i=0
# c=[]
# while i<d:
#     a=int(input("Enter any number:-"))
#     c.append(a)
#     i+=1
#     # print(c)
# j=0
# b=0
# while j<len(c):
#     b=c[j]%10
#     j+=1
# # print(b)
# if b%10==0:
#     print("Yes")
# else:
#     print("No")

# # PARENTHESIS:

# def valid(a):
#     count=0
#     for i in a:
#         if i=="(":
#             count+=1
#         elif i==")":
#             count-=1
#         if i=="{":
#             count+=1
#         elif i=="}":
#             count-=1
#         if i=="[":
#             count+=1
#         elif i=="]":
#             count-=1
#         if count<0:
#             return False
#         if count==0:
#             return True
# a=input("Enter symbol:- ")
# print(valid(a))


# ROMAN TO INTEGER

# SUBSTRING


# def lengthOfLongestSubstring(s):
#         maxLen=1
#         if s=='':
#             return 0                      
#         for i in range(len(s)):
#             substring=s[i]              
#             for j in range(i+1, len(s)):  
#                 if s[j] not in substring:  
#                     substring=substring + s[j]
#                     maxLen=max(maxLen, len(substring)) 
#                 else:
#                     break
#         return maxLen
# s=input("Enter any string:-")
# print(lengthOfLongestSubstring(s))

# CAPITALIZE

# a="hello world"
# print(a.title()) 

# NESTED LIST

# a=int(input("Enter the total number of students:- "))
# i=0
# d=[]
# while i<a:
#     e=[]
#     b=input("Enter the names of the students:- ")
#     c=float(input("Enter the Marks of the students:- "))
#     e.append(b)
#     e.append(c)
#     d.append(e)
#     i+=1
# print(min(d))


# PLURAL

# def plural(n):
#     if n==1 or n<1:
#         return False
#     else:
#         return True 
# n=int(input("Enter any string") )  
# print(plural(n))
 
# DETECT FLOATING POINT NUMBER

# class Main():
#     def __init__(self):
#         self= int(input())
        
#         for i in range(self):
#           n=input()
          
#           if chr in n:
#             print("False")
#           elif "+" and "-" in n:
#             print("False")
#           elif ("+" or "-" or "." in n) and n.isdigit() and ("." in n ):
#             print("True")
#           else:
#             print("False")
# if __name__ == '__main__':
#     obj = Main()       

# def float(n):
#     for i in range(0,n):
#         a=int(input("Enter the num:- "))
#         if a==float:
#             return True
#         else:
#             return False
# n=input("Enter the string:- ")
# print(float(n))  


# WHO IS TALLER?

# x=int(input("ENter the number:-"))
# y=int(input('Enter the number2:- '))
# if x>y:
#     print("x is taller")
# elif y>x:
#     print("y is taller")
# else:
#     pass


# COMPANY LOGO

# s="aabbbccde"
# a=list(s)
# print(a)
# b={}
# for i in a:
#     if i in b:                
#         b[i]+=1
#     else:
#         b[i]=1
# x=[]
# for k,v in b.items():
#     x.append(k)
#     x.append(v)
    
# print(b)




# c=sorted(b.items(), key=lambda x: x[1], reverse=True)
# # c=sorted(b.items(), key=lambda x: x[0], reverse=True)
# for i in c:
#     if i[1]!=1:
#        print(i[0],i[1])
#        break

# print(b)
# c=sorted(b.values())
# d=sorted(b.keys())
# print(d,c)




# sorted_values = sorted(b.values()) # Sort the values
# sorted_dict = {}
# for i in sorted_values:
#     for k in b.keys():
#         if b[k]==i:
#             sorted_dict[k]=b[k]
#             break
# print(sorted_dict)


# if(0):
#     print(True)
# print(False)

# CATS AND DOGS

# t = int(input("Enter the number:- "))
# for i in range(t):
#     cats=int(input("Enter the number:- "))
#     dogs=int(input("Enter the number:- "))
#     legs=int(input("Enter the number:- "))
#     total=(cats+dogs)*4
#     mini=max(0,cats-dogs*2)
#     if total>=legs and legs%4==0 and (dogs+mini)*4<=legs:
#         print("YES")
#     else:
#         print("NO")

# SWATI CODE

# t=int(input())
# i=0
# while i<t:
#     c=int(input())
#     d=int(input())
#     l=int(input())
#     total_leg=(c+d)*4
#     min_cat=(c-d*2)
#     if  total_leg==l or (d+min_cat)*4==l:
#         print("yes")
#     else:
        # print("no")


# MONORI CODE

# T=int(input())
# for i in range(T):
#     C,D,L=map(int,input().split())
#     total = (C+D)*4
#     min_no=C-D*2
#     if(total>=L and L%4==0 and (D+min_no)*4<=L):
#         print("yes")
#     else:
#         print("no")


# ANSHIKA CODE

# t=int(input())
# for i in range(t):
#      c,d,l=map(int,input().split())
#      total=(c+d)*4
#      if(c>(d*2)):
#         min_legs=(c-(d*2)+d)*4
#      else:
#         min_legs=(d*4)
#      if l%4==0 and l>=min_legs and l<=total:
#          print("yes")
#      else:
#           print("no")



# TRIANGLE QUEST:

# for i in range(1,int(input())): 
#     print(int(i * 10**i / 9))


# n=int(input("Enter the number:- "))
# i=1
# while i<n:
#     b=i*10**i
#     c=b/9
#     print(int(c))
#     i+=1


# WORDS SCORE:

# def is_vowel(letter):
#     return letter in ['a', 'e', 'i', 'o', 'u', 'y']

# def score_words(words):
#     score = 0
#     for word in words:
#         num_vowels = 0
#         for letter in word:
#             if is_vowel(letter):
#                 num_vowels += 1
#         if num_vowels % 2 == 0:
#             score += 2
#         else:
#             score+=1
#     return score

# THE CAPTAINS ROOM

# a=int(input("Enter the number of groups:- "))
# i=0
# c=[]
# while i<a:
#     b=int(input("Enter the number of rooms:- "))
#     c.append(b)
#     d=str(c)
#     e=d.split()
#     i+=1
# print(e)

# SATISH CODE

# t = int(input())
# while(t>0):
#     cats, dogs, legs = map(int, input().split())
#     max_legs = (dogs + cats) * 4
 
#     if((2 * dogs) >= cats):
#         min_legs = 4 * dogs

#     else:
#         min_legs = (cats - (2*dogs)) * 4 + dogs * 4

#     if(legs < min_legs or legs > max_legs):
#         print("no")

#     else:
#         if(legs % 4 == 0):
#             print("yes")
#         else:
#             print("no")
#     t -= 1

# f={}
# for j in e:
#     if j not in f:
#         f[j]=1
#     else:
#         f[j]+=1
#     for i,k in b.items():
#         if k!=a:
#             print(j)
        
    
    

# num_rooms=(int(x) for x in input().split())
# b={}
# for i in num_rooms:
#     if not i in b:
#         b[i]=1
#     else:
#         b[i]+=1
# for i,j in b.items():
#     if j!=a:
#         print(i)
    
# COUNT ODD:


# def odd_count(n):
#     if n%2==0:
#         return n/2
#     else:
#         return(n-1)/2
#     pass
# n=int(input("Enter the number:- "))
# print(odd_count(n))

dict=[{"name":"liki"},{"dosth":"preethi"},{"mentor":"savitha"}]
n=input("Enter any string:- ")
for i in dict:
        if n==i:
                print(dict[i])
























    
