import weakref


class BigObject:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def __call__(self, *args, **kwargs):
        print(f'I am {self.name} this size of my is {self.size}')


data_loader = BigObject(name='image-set', size=1e9)

loader_ref = data_loader

# from ... import data_loader

del data_loader
# data_loader = tuple() # change to small tuple

loader_ref()


data_loader = BigObject(name='image-set', size=1e9)

loader_ref = weakref.ref(data_loader)

print(loader_ref() is data_loader)

del data_loader

print(loader_ref())

## assignment

data_loader = BigObject(name='image-set', size=1e9)

loader_ref = weakref.ref(data_loader)

print(loader_ref() is data_loader)

data_loader = 1

print(loader_ref())



