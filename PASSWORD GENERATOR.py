import random
import string
password=''                          #To store final password
s=[]                                 #contain characters of password
password_len=random.randrange(8,16)  #genrate the length of password between 8 to 16

#genrates the password
def passwod_genrator():
   global passw
   a=0
   #store character in s which are genrated randomly
   for a in range(0,4):
      strr=(random.choice(string.ascii_lowercase),random.choice(string.ascii_uppercase),random.choice(string.digits),random.choice(string.punctuation))
      passw=random.choice(strr[a])
      s.append(passw)
      a=a+1


#this loop add each character stored in s
for i in range(0,password_len):
    passwod_genrator()
    password=password+str(s[i])
    i=i+1

#print final password
print("Passwod is:",password)