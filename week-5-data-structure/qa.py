from collections import defaultdict
import re
import copy
'''
问题:
为何同样的变量freq定义在不同的位置,
count_word()函数中的freq也是可变类型,它的物理地址为何是变化的,
'''

def get_word(text,freq=defaultdict(int)):
    for word in [i.lower() for i in re.findall(r'\w+',text)]:
        freq[word]+=1
    return freq


def count_word(text):
    freq=defaultdict(int)
    for word in [i.lower() for i in re.findall(r'\w+',text)]:
        freq[word]+1
    return freq


print('run:count',count_word('Go to the world'))
print('run:count',count_word('go and run away the house'))
print('run:get',get_word('Go to the world'))
print('run:get',get_word('go and run away the house'))


def init_arg():
    print('The arg is initialized!!')
    return []


print('--before func def')
def simple_arg_mutable(n, m=0, numbers=init_arg()):
    print(m)
    for i in range(n):
        numbers.append(i)
    print(numbers)
print('--after func def')


print('--before first called')
print(simple_arg_mutable.__defaults__)
print('--after first called')
simple_arg_mutable(3)
print(simple_arg_mutable.__defaults__)
simple_arg_mutable(4)
