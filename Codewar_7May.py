# Remove string space:

# def no_space(x):
#     a=x.replace(" ","")
#     return a
# x=input("Enter any string:- ")
# print(no_space(x))

# LENGTH,WIDTH,BREADTH

# def a(l,w,h):
#     return l*w*h

# print(a(2,2,2))

# COUNT POSITIVE AND SUM NEGATIVE

# def count_positives_sum_negatives(arr):
#     if not arr: 
#         return []
#     pos=0
#     neg=0
#     for i in arr:
#         if i>0:
#             pos+=1
#         elif i<0:
#             neg+=i
#     return [pos,neg]
# arr=[3,4,5,6,7,8,9,2]
# print(count_positives_sum_negatives(arr))
  
  
# REMOVE EVERY SECOND ELEMENT

# def remove_every_other(my_list):
#     r = []
#     for i in range(len(my_list)):
#         if i % 2 == 0:
#             r.append(my_list[i])
#     return r
# print(remove_every_other(["Keep", "Remove", "Keep", "Remove", "Keep", ...]))

# Lario and Muigi Pipe Problem

# def pipe_fix(nums):
#     length = len(nums) - 1
#     y = []
#     x = nums[0]
#     while x <= nums[length]:
#         y.append(x)
#         x += 1
#     return y
#     return []
# nums=1,3,5,6,7,8 
# print(pipe_fix(nums))

# Implement a function which multiplies two numbers.

# def multiply(a,b):
#     return a*b
# print(multiply(2,3))

# MERGE TWO LIST

# def merge_arrays(arr1, arr2):
#     c=arr1+arr2
#     return c
# arr1=[1,2,3]
# arr2=[3,4,5]
# print(merge_arrays(arr1, arr2))

# SENTENCE SMASH
# def smash(words):
#     i=0
#     l=len(words)
#     str1=""
#     while i<l:
#         if i<l-1:
#             str1+=words[i] + " "
#         else: 
#             str1+=words[i]
#         i+=1
        
#     return str1
#     return ""
# words=["Hello","world","this","is","great"]
# print(smash(words))

# LOVE FUNCTION

# def lovefunc(flower1,flower2):
#     if (flower1+flower2)%2==0:
#         return False
#     else:
#         return True
# flower1=int(input("Enter the num"))
# flower2=int(input("Enter the num"))
# print(lovefunc(flower1,flower2))

# WHAT IS BETWEEN
# Complete the function that takes two integers (a, b, where a < b)
# and return an array of all integers between the input parameters, 
# including them.

# def between(a,b):
#     i=a
#     c=[]
#     while i<=b:
#         c.append(i)
#         i+=1
#     return c
# print(between(1,4))



# test_case=int(input())
# for i in range(test_case):
#     N,K,X,Y = map(int,input().split())
#     a=[]
#     while True:
#         if (X+K)%N not in a:
#             a.append((X+K)%N )
#             X=(X+K)%N
#             if X==Y:
#                 print("YES")
#                 break
#         else:
#             print("NO")
#             break


# a=10
# print(a>>5)

# def anagram(a,b):
#     if sorted(a)==sorted(b):
#         return True
#     else:
#         return False
# print(anagram("build","dubil"))
# print(anagram("grace","raceg"))


# def differenceofSum(n, m):
#     n_d=0
#     d=0
#     for i in range(m):
#         if i%n==0:
#             d+=1
#         else:
#             n_d+=i
#         c=d-n
#     return c
# n=int(input())
# m=int(input())
# print(differenceofSum(n, m))

# d={"a":2,"b":3,"c":4}
# for i in d:
#     d[i]=[]
# print(d)

# LONGEST WORD

# a=['simple', 'is', 'better', 'than', 'complex',"Chuningliu",""]
# max1 = len(a[0])
# temp = a[0]
# for i in a:
#     if(len(i) > max1):
#         max1 = len(i)
#         temp = i
# print(len(temp))    


# def longest(words):
#         return max(len(i) for i in words)
# words=['simple', 'is', 'better', 'than', 'complex',"Chuningliu",""]
# print(longest(words))
    
# REMOVE EXCLAIMATORY MARK FROM THE END OF THE STRING

# def remove(s):
#     if s and s[-1]=='!':
#         return s[:-1]
#     else:
#         return s
# s=("Hi!!")
# print(remove(s))
 
           
    