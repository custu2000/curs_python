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
#lambda https://medium.com/@happymishra66/lambda-map-and-filter-in-python-4935f248593
#https://www.linuxtopia.org/online_books/programming_books/python_programming/python_ch20s05.html
#matrici
#dictionar de dictionare
#m3['hau88']={'new8': {'new88':{'new99':{'aici':88}}}}

filter(lambda x : x % 5 == 0 and x % 7 !=0, range(2000,3000))
        
#ex9

def friend(list1,list2):
     set1=set(list1)
     set2=set(list2)
     if len(set1.intersection(set2))>0:
        return True
     else:
        return False
b=[1, 2, 3, 4]
c=[2, 3]
friend(b,c)
    
#ex 9
a=['sdafdsa', 'dfsafdas', 'sdfalkjkl']

def max_size_word(list1):
     return max(map(lambda x: len(x),list))
max_size_word(a)
#ex 10
def filter_size_word(list1,n):
     return  filter(lambda x: len(x)<n,list1)
 
