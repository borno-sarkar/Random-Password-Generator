import random
import string
charValues = string.ascii_letters + string.digits + string.punctuation 
pass_len = int(input("Enter password length: "))
password = "".join([random.choice(charValues) for i in range(pass_len)])

 	
print("your password: ", password)