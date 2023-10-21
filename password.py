import string
import random

if __name__ == "__main__":
    s1= string.ascii_lowercase
   # print (s1)
    s2 = string.ascii_uppercase
    #print (s2)
    s3 = string.digits
    #print (s3)
    s4 = string.punctuation
    s5=string.octdigits
    #print(s4)
    #creat a list
    passwordlenght = int(input("enter the lenght of password\n"))
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    s.extend(list(s5))
    random.shuffle(s)
    print ("".join(s[0:passwordlenght]))