#1.()
#tu=(10)
tu=(10,)  #use comma for single value
tu=(10,20,30,'a',3.14,10)

#2.Heterogeneous

#3.ordered

#4.Immutable
#tu[0]=50  raise error

#5.Duplicate elements allowed

#Tuple is faster then list

import sys
li=[]
tu=()
print(type(tu))
print(tu)
print(sys.getsizeof(li))
print(sys.getsizeof(tu))