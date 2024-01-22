import random
import string
password=''                          #To store final password
s=[]                                 #contain characters of password
password_len=random.randrange(8,16)  #genrate the length of password between 8 to 16

#genrates the password
def passwod_genrator():
 global passw
 a=0
 for a in range(0,4):             #   
  strr=(random.choice(string.ascii_lowercase),random.choice(string.ascii_uppercase),random.choice(string.digits),random.choice(string.punctuation))
  passw=random.choice(strr[a])
  s.append(passw)
  a=a+1

for i in range(0,password_len):
    passwod_genrator()
    password=password+str(s[i])
    i=i+1
print("Passwod is:",password)