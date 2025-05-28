import random
import string
pass_len=16
charvalues=string.ascii_letters+string.ascii_letters+string.punctuation+string.digits
# print(string.ascii_letters)
# print(string.ascii_lowercase)
# print(string.ascii_uppercase)
# print(string.punctuation)
# print(string.digits)


#list comprehensionp[function]

password="".join([ random.choice(charvalues) for i in range(pass_len)])
# print(res)

# password=''
# for i in range(pass_len):
#     # print(random.choice(charvalues))
#     password+=random.choice(charvalues)

print("you random password is ",password)

#American Standard Code for Information Interchange