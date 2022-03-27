import random
from icecream import ic


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age  = age



## Task -> Person.age += 1


persons = [Person('test', random.randint(2, 20)) for _ in range(10)]

print(persons)

def add_age(p): 
    p.age += 1
    return p


def reverse_name(p):
    p.name = p.name[::-1]
    return p
    
returned = filter(lambda n: n >= 50, 
                map(lambda n : n ** 2,
                    map(lambda p: p.age , persons)
                )
            )


ic(list(returned))

r = map(add_age, persons) #==>  for p in persons: r = add_age(p)
print(next(r))
print(next(r))
print(next(r))

#persons = [p.age + 1 for p in persons]

#print(persons)
