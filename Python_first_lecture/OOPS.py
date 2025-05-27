# #ps _1(code with harry)
# # class programmer:
# #     company ='microsoft'
# #     def __init__(self,name,salary,pin):
# #         self.name=name
# #         self.salary= salary
# #         self.pin=pin

# # p=programmer("kartik", 120000,201301)
# # print(p.name,p.salary,p.pin,p.company)
# # v=programmer("vishal", 120000,201301)
# # print(v.name,v.salary,v.pin,v.company)

# #ps_2(code with harry)
# # class calculator:
# #     def __init__(self,n):
# #         self.n=n
# #     def square(self):
# #         print(f" the square is {self.n*self.n}")

# #     def cube(self):
# #         print(f" the cube is {self.n*self.n*self.n}")

# #     def squareroot(self):
# #         print(f" the squareroot is {self.n**1/2}")


# # a=calculator(4)
# # a.square()
# # a.cube()
# # a.squareroot()


# #ps_3(code with harry)
# #class demo:
#     a=4

# #o=demo()
# #print(o.a)# print the class attribute becaouse instance attribute is not print
# #o.a=0# print the instance attribute is set
# #print(o.a)# print the instance because instance attribute is presnet 

# #print(demo.a)#print the class attribute
def findSecondLargest(arr):
    if len(arr) < 2:
        return -1  # Return -1 if the array has fewer than 2 elements

    unique_numbers = list(set(arr))  # Remove duplicates
    if len(unique_numbers) < 2:
        return -1  # Return -1 if there is no second largest element

    unique_numbers.sort(reverse=True)  # Sort in descending order
    return unique_numbers[1]  # Return the second largest element

# Test array
arr = [10, 20, 5, 8, 18]

# Print the second largest number
print("Second largest number:", findSecondLargest(arr))