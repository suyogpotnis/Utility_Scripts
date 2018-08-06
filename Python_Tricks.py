"""
Date: 08/05/2018
This file contains cool shortcuts / tricks that can be done in python
"""

# 1.]  How to sort a Python dict by value

d = {'a': 4, 'b': 3, 'c': 2, 'd': 1}
# Expected Output: [('d', 1), ('c', 2), ('b', 3), ('a', 4)]

#Solution 1:
sorted(d.items(), key=lambda x: x[1])

# Solution 2:
import operator
sorted(d.items(), key=operator.itemgetter(1))

# ================================================================
# 2.] How to merge two python dictionaries
# Merging Dictionaires with dictinct keys
d1 = {'a':1, 'b':2}
d2 = {'c':3, 'd':4}
# Expected Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}
output = {**d1, **d2}

# Merging Dictionaires with overlapping keys
d1 = {'a':1, 'b':2}
d2 = {'b':3, 'c':4}
# Expected Output: {'a': 1, 'b': 3, 'c': 4}
output = {**d1, **d2}

"""
Explanation: When merging dictionaries with the above syntax the dictionary
on the right will retain its value for all overlapping keys. Which is why
when we merge d1 and d2 where 'b' is the overlapping key, the resultant
dictionary will have the value 3 for the key 'b'
"""
