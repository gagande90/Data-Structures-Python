number_set = {1, 2, 3, 4}                       # sets use curly braces for creation          
letter_set = {'a', 'b', 'c', 'd'}
mixed_set = {1, 'a', 2, (1, 2, 3)}              # types must be "hashable", i.e. immutable
empty_set = set()                               # have to use the set() function, cannot use = {}




print(number_set)
print(letter_set)
print(mixed_set)
print(empty_set)                                # returns: set(). {} would be a dict, not a set

print(type(number_set))                         # <class 'set'>
###
number_set_unique = {1, 2, 3, 4, 2, 3, 4}       # sets only store unique values  
print()
print(number_set_unique)                        # {1, 2, 3, 4}, ignores dupes
###
number_set.add(5)                               # add an item to the set
print()
print(number_set)
###
print()
print()
number_set.add(4)                               # try to add existing item to the set
number_set.add(5)                               # try to add existing item to the set
print(number_set)                               # no duplicates, nothing got added
###
print()
print()
number_set.remove(1)                            # remove an item from the set
print(number_set)
###

print()
print()
try:                                            # if the item is not in the set
    number_set.remove(3)                       # KeyError: 98 
    print("Test worked fine! Cool!! Move Ahead!!!")
except Exception as e:
    print('** caught Exception:', e) 
###
###                                                # use the 'in' keyword

print()
print()

if (98 in number_set):
	print("Yes, its there!")
else:
	print("Nope, its not there!")









