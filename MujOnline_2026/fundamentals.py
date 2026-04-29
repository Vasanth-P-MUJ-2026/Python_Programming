# Python Variable,
# Identifiers,
# Rules to Follow While Naming Identifiers,
# Convention to be Followed While Naming Identifiers,

#  DECLARING VARIABLE AND ASSIGNING VALUE.

xn = 20
xd = 20.6
xs = "hello world!"
xc = 3+4j
xb = True

# Data Types;

# Numeric :- int , float, complex
a=10
b=20.5
c=3+5j
print(a,b,c)
print(type(a), type(b), type(c))

# Boolean: True or False
p= True
q= False
print(type(p), type(q))

# strings
a='Hello'
b="Java"
c='''Python'''
print(a,b,c)
print(type(a), type(b), type(c))

# String Indexing
s="Java"
print(s[0]) #J
print(s[-1]) #a

# NoneType
r= None
print(r, type(r))

# allocated Memory check using id
p=20
print(id(p))
q=20
print(id(q))
c=20
print(id(c))
p=p+5
print(id(p))

# Sequence of data - List, Tuple, Dictionary, Set.

#tuple - ()
tup=(1,2,3) 
print(tup)
print(tup[0])
print(tup[1])
print(tup[-1])
# why immutable
t = (1, 2, 3)
print(t)
print(id(t))
t = t + (4, 5, 6)
print(id(t))
print(t)

# List - []
l1=[11,22,33,44.5,"Hello"]
print(type(l1))
print(l1[2])
l1[1]=55
print(l1)

# set - ()
s={1,2,3,4,5}
print(s)
print(type(s))

# set is a collection of immutable data type: int , float, string, tuple, frozenset
# mutable: list , set, dictionary

# Dictionary :- collection key and value pairs
# keys must be unique, only immutable datatypes are allowed as a key
d={1:"Java", 2:"Python", 3:"C++"}
print(d
print(type(d))
d[3]="C"
print(d)
print(d.keys())
print(d.values())
print(d.items()) #both key and values

a= ()
print(type(a))
b=[]
print(type(b))
c={}
print(type(c))
s=set()
print(type(s))
