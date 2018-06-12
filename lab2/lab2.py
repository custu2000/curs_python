l=[1,2,3,4,2,1,5,8]
f=[]

for i in l:
   if f.count(i)==0:
      f.append(i)

print(f)


#version 2


f=set(l)
print(f)

#ex2
f1="#".join(l)
print(f)
#ex3

l1=[1,2,3,4,5,6,7]
l2=['a','b','c','d','e','f']

d=zip(l1,l2)
print(d)

#ex 4
a = [1, 3, 20, 1024, 53, 12, 102, 1, 4, 43, 32]
for i in a:
    if i%3==0:
       print("Numarul {} este divizibil cu 3".format(i))

      
      
#ex 5
print(a[::2])

#ex6

cumparaturi={'tastatura':70,'mouse':50,'casti':100}
cumparaturi2={}

for key,value in cumparaturi.items():
     cumparaturi2.update({key:value*1.19}) 

print(cumparaturi2)


#ex7

groups = {}
data=['apple', 'banana', 'pear', 'apple', 'apple', 'banana', 'cherry', 'banana', 'apple']
data = sorted(data)

for k,g in itertools.groupby(data):
   groups.update({k:len(list(g))})

   
dic=dict(collections.Counter(data))

#ex 8

for i in range(2000,3000):
   if i % 5 ==0 and i %7 !=0:
       print i
 
#ex 8. cu filter http://book.pythontips.com/en/latest/map_filter.html

filter(lambda x : x % 5 == 0 and x % 7 !=0, range(2000,3000))
        
      
    

