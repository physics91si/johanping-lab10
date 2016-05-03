#testing code 

#import sets.py

a = NewSet([1,3,4,5])
a.does_contain(10)
a.adder(9)
a.remover(9)
a.remover(10)
a.size()
print(a.__union__([1,3,5,8]))
print(a.__intersection__([1,3,5,8]))
print(a.__sub__([1,3,5,8]))