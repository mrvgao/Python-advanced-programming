""""
c, java, c++:
    add(): -> parameters: int, float, class<Stu>
"""
from collections import namedtuple
import random


def add(a, b): return a + b


class Vector:
    def __init__(self, *args):
        self._list = list(args)

    def __add__(self, other):
        if isinstance(other, (Vector, tuple, list)):
            return [self._list[i] + other[i] for i in range(len(other))]
        else:
            return str(self) + str(other)

    def __getitem__(self, item):
            return self._list[item]

    def __len__(self):
        return len(self._list)

    def __repr__(self):
        return str(self._list)


class SampleBatch(dict):
    """
    "agent": [obs, obs, obs, ... obs]
    """
    AGENT = 'agent'
    PERIOD = 'period'

    def __add__(self, other):
        for key, value in self.items():
            if key in other:
                self[key] += other[key]

        return self


def show_add():
    print(add(Vector(0, 1, 2), Vector(-1, -1, -2)))
    print(add(Vector(0, 1, 2), (-10, -10, -20)))
    print(add(Vector(0, 1, 2), [-10, -10, -20]))
    print(add(Vector(0, 1, 2), 'some other'))

    print(add('I am a ', 'good boy'))

    agent = SampleBatch.AGENT
    period = SampleBatch.PERIOD
    sb = SampleBatch(agent=1, period=3)
    sb2 = SampleBatch(agent=2, period=10)
    print(sb)
    print(sb[SampleBatch.AGENT])
    print(sb[SampleBatch.PERIOD])
    print(add(sb, sb2))
    """<generic>"""

"""
C++, Java
class Poker(){
    public void choose(){}; 
    public void shuffle() {};
}
"""

Card = namedtuple('Card', ['number', 'shape'])


class Poker:
    numbers = '23456789TJQKA'
    shapes = '♥♠♣♦'
    joker = '小王 大王'.split()

    def __init__(self):
        self._cards = [Card(n, s) for n in Poker.numbers for s in Poker.shapes]
        self._cards.append(Card(15, Poker.joker[0]))
        self._cards.append(Card(16, Poker.joker[1]))

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, item):
        return self._cards[item]

    def __setitem__(self, key, value):
        self._cards[key] = value

    def __repr__(self):
        return str(self._cards)


if __name__ == '__main__':
    deck = Poker()
    print(len(deck))
    print(deck[19])
    print(deck[10:19])

    print('*'*8)
    for _ in range(8):
        print(random.choice(deck))

    print(deck)
    random.shuffle(deck)
    print(deck)



