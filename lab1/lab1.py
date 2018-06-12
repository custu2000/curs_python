#ex 1

for i in range(100):
    print ("hello world")

# ex 2
s="hello world"*100
print (s)


#ex 3
#fizz  %3, buzz %5, fizz buzz cu 3 si 5
#rest numarul

for i in range(100):
    if i % 3 ==0 and i % 5 ==0:
        print "fizz buzz for: ",i
    if i % 3 ==0 :
        print "fizz for: ",i

    if i % 5 ==0 :
        print "buzz for: ",i
 
#ex 4

n=input('introduceti numarul: ')
n1=(n%100)//10
print "cifra zecilor este :",n1


#ex 5
print "ex 5"
n=input('introduceti numarul de minute: ')
n1=n//60
n2=n-n1*60
print ("Minute : %d Secunde:%d "%(n1,n2))
print ("Minute : {} Secunde: {}".format(n1,n2))

#ex 6
#bisect %4 dar nu si cu 100
#bisect daca este diviz cu 400


an=input('introduceti anul: ')

if an % 400 ==0 or (an % 4==0 or an %100==0):
    print("anul {} este bisect".format(an))
else:
    print("anul nu este bisect"); 



#ex7


