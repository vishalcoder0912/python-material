# #using walrus operator 
# if(n:=len([1,2,3,4,5]))>3:
#     print(f"life is to long ({n}) element expected <=3")#output :list 
#     #is too long (5 elements , expected <=3)


#type 
# from typing import list,unnion 
# n :int =5

# name:str='harry'

# def sum(a:int ,b:int)->int:
#     return a+b

# sum()

## match cases

# def https_status(status):
#         match status:
#             case 200:
#                 return 'ok'
#             case 400:
#                 return 'not found'
#             case 500:
#                 return 'inter server error'
#             case _:
#                 return 'unknown status '
                
# print(https_status(200))
# print(https_status(400))
# print(https_status(600))

#dictonary merged programmed 

# dict1={'a':1,'b':2}
# dict2={'c':3,'d':4}
# merged=dict1|dict2
# print(merged)


#exception file handling in pyt/hon
# try:
#     a=int(input("hey , Enter a number :"))
#     print(a)

# except Exception as e:## give error intentionally 
#     print(e)


# print("thanku you ")


# a=int(input('Enter a number: '))
# b=int(input('Enter second number :'))
# if(b==0):
#     raise ZeroDivisionError("hey buddy our program is not meant to divide numbers by zero")
# else:
#     print(f'the division is a/b is {a/b}')

# def main():
#     try:
#         a=int(input('hey, Enter a numbers '))
#         print(a)
#         return
#     except Exception as e:
#         print(e)
#         return
    
#     finally:
#         print('hey i am inside the progrm')
# main()


## problem set 12( codee with harry)
# try:
#     with open('1.txt','r') as f:
#         print(f.read())
# except Exception as e:
#     print(e)

# try:
#     with open('2.txt','r') as f:
#         print(f.read())
# except Exception as e:
#     print(e)


# try:
#     with open('3.txt','r') as f:
#         print(f.read())
# except Exception as e:
#     print(e)


# print('thanku you !')

# question 2

# l=[1,2,3,4,5,6,7,8]
# for i, item in  enumerate(l):
#     if i==2 or i==4 or i==6:
#         print(item)

# print table 

# n=int(input("ENter a number : "))

# table=[i*n for i in range (1,11)]
# print(table)


# try:
#     a =int(input('enter a: '))
#     b=int(input('enter b: '))
#     print(a/b)
# except ZeroDivisionError as v:
#     print('infinite')


