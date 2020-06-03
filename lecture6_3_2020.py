import math

# memoization, top-down dynamic programming

cache = {}

def fib(n):
    if n <= 1:
        return n
    
    if n not in cache: # looks for n to be a key in the cache
        cache[n] = fib(n-1) + fib(n-2)
    
    return cache[n]

for i in range(95):
    print(f'{i:3} {fib(i)}')



# cache pattern to reduce time to compute - useful to reduce actual runtime of recurisve functions
def expensive_function(x,y):

    key = (x,y)

    if key not in cache:
        cache[key] = 'whatever_expensive_thing_here'
    
    return cache[key]
################################################################################################################################

# Inverse square root

# inv_sqrt(x) = 1 / sqrt(x)

inv_sqrt = {}

def build_lookup_table():
    for i in range(1, 1000):
        inv_sqrt[i] = 1 / math.sqrt(i)

build_lookup_table()

print(inv_sqrt[3])
print(inv_sqrt[12])

#######################################################################################################################################

# Sort a dictionary/hash table

d = {
    'foo':12,
    'bar':17,
    'qux':2
}

items = list(d.items())

# sort ascending by key
items.sort()

print(items)

# sort decending by key
items.sort(reverse=True)

print(items)

print(dict(items))

# sort ascending by value

"""
def get_key(e): # e si goig to be the tuple
    # return the thing we want to sort by
    return e[1]
items.sort(key=get_key)
"""

items.sort(key=lambda e: e[1])

print(items)

