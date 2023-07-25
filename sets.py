# a set is an unordered sequence of elements that can't have repeated elemnents

basket = {'apple', 'orange', 'pear'}

x = 'orange' in basket
print(x)

a = set('abracadabra')
b = set('alacazam')

print(a - b) # letters in a, but not in b
print(a | b) # letters in a or b or both
print(a & b) # letters in both a and b
print(a ^ b) # letters in a or b but not both

# set comprehension
c = {x for x in 'abracadabra' if x not in 'abc'}
print(c)