import random
import string
password=''
s=[]
password_len=random.randrange(8,16)
def h():
 global passw
 a=0
 while a in range(0,4):
  strr=(random.choice(string.ascii_lowercase),random.choice(string.ascii_uppercase),random.choice(string.digits),random.choice(string.punctuation))
  passw=random.choice(strr[a])
  s.append(passw)
  a=a+1

for i in range(0,password_len):
    h()
    password=password+str(s[i])
    i=i+1
print("Passwod is:",password)