l=[1,2,3,4,2,1,5,8]
f=[]

for i in l:
   if f.count(i)==0:
      f.append(i)

print(f)


#version 2


f=set(l)
print(f)


#ex3

l1=[1,2,3,4,5,6,7]
l2=['a','b','c','d','e','f']

d=zip(l1,l2)
print(d)

#ex 4


