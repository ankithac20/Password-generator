import string
import secrets

#print(string.ascii_lowercase)
#print(string.ascii_uppercase)
#print(string.punctuation)
#print(string.digits)

combination = string.ascii_lowercase + string.ascii_uppercase + string.punctuation + string.digits
#print(combination)
strongpassword = ''
l = int(input("Enter the length of the password : "))
for i in range(l):
    c = secrets.choice(combination)
    strongpassword = strongpassword + c
    print(c)
print(f"Password : {strongpassword}")       
