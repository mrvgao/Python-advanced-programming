import pickle
import marshal
import shelve


class Dataloader:
    def __init__(self, _id):
        self.id = _id
        self.data = []

    def add(self, elements):
        self.data += elements


dataloader = Dataloader('u88910')
dataloader.add(range(1000))


naive_dataloader = {
    'name': 'uid111312',
    'events': list(range(100)),
    'pairs': (10, 100)
}

with open('dataloader.pkl', 'wb') as f:
    pickle.dump(naive_dataloader, f)


f = shelve.open('some_key_value_data')
f['name'] = 'John'
f['saved'] = -99

f.close()