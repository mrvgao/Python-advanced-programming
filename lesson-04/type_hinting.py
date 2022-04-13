from typing import NewType


vector = list[int]

logId = NewType('LogID', str)
new_id = logId('123456')

print(type(new_id))


def summarize(event: vector, mark: str, _id: logId=logId('')) -> dict:
    return {
        'name': mark,
        'events': event
    }


print(summarize([1, 5], 'loss'))

print(summarize(0.01, -99))

print(summarize([1, 2, 3], 'loss', logId('u998')))

