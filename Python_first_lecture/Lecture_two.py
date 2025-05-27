# str1="this is a string ,\n we are ceating in it "
# str2='i am vishal'
# print(str1+str2)

#string count 

# str1="kartik"
# len1=len(str1)
# print(len1)

# str2='kumar'
# len2=len(str2)
# print(len2)

# final_length=str1+ " "+str2
# print(final_length)
# print(len(final_length))

#indexing 

# str="apna collage"
# ch=str[4]
# print(ch)


##slicing
# str="apna collage"
# print(str[5:len(str)])

# str="apna collage"
# print(str[5:12])

# str="apna collage"
# print(str[5:])

# str="apna collage"
# print(str[:4])

##negative(backword counting )
# str='apple'
# print(str[-5:-2])

# str='i am studying python formm apna college'
# print(str.endswith('ge'))

# str='i am vishal'
# str=str.capitalize()
# print(str)

# str='my n@me is k@rtik . i study in bc@ @nd i want to be @ h@cker '
# print(str.replace("@","a"))

# str='vishal  is a great person '
# print(str.find("a"))
# print(str.count("a"))


#let's practice some question
## write a program to input user's first name & print its length.
# Name=input("Enter you name")
# print(len(Name))
## write to find the occurrence of $ in a string
# str='my name is vishal $$$$$$$'
# print(str.count('$'))

# age=7

# if(age>=18):
#     print("you can vote")
# else:
#     print("you cannot be vote")

# Marks=int(input("Enter you grade :"))
# if(Marks>=90):
#     print("your grade is A :")
# elif(Marks>=80):
#     print("your grade is B")
# elif(Marks>=70):
#     print("you grade is c")
# else:
#     print("you grade is d ")

age=90
if(age>=18):
    if(age>=80):
         print('cannot drive ')
    else:
         print('can drive ')
else:
     print("cannot drive")