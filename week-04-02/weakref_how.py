import weakref
import gc


class BigObject:
    def __call__(self, *args, **kwargs):
        print('a huge obj is called')


class MyObject:
    def __call__(self, *args, **kwargs):
        print('a huge obj is called')


bg = BigObject()

another = bg

gc.collect()

print(another is bg)

bg = 'new'

gc.collect()
print(another())


obj = MyObject()
r = weakref.ref(obj)

gc.collect()
assert r() is obj #r() allows you to access the object referenced: it's there.

obj = 1 #Let's change what obj references to
gc.collect()
assert r() is None #There is no object left: it was gc'ed.
