import random
import string
charValues = string.ascii_letters + string.digits + string.punctuation 
pass_len = int(input("Enter password length: "))
password = ""
for i in range(pass_len):
    password += random.        choice(charValues)
 	
print("your password: ", password)