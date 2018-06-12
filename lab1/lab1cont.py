str1=raw_input('introduceti stringul: ')

def find_special (str1):
    if str1.count('t')==0:
        return -2
    elif str1.count('t')==1:

       return -1
    else:
      return str1.find('t',str1.find('t')+1)


print(find_special(str1))

print str1.replace("1", "unu")
print str1.replace("@", "")


def is_palindrom (str1):
   if str1 == 'Radar':
     return True
   else:
     return False

print(is_palindrom(str1))

import math
def my_factorial(x):
 return math.factorial(x)


print(my_factorial(4))

#13
def my_sum(*args):
    s=0
    for i in args:
       s+=i
    return s 

print(my_sum(1,2,3,5,6))
