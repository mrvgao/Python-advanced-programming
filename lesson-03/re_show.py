import re
import pandas as pd

file = open('sqlResult_1558435.csv', encoding='gb18030')

length = int(1e5)

"""
Task-01: 
    Characters -> 字符 
"""


def token(string):
    return re.findall(r'\w+', string)


def clean(string):
    return re.sub(r'[a-z\d\W]+', ' ', string)


"""
Input: 单词 多个单词
Output: 包含该单词的所有句子，并且用特殊的##进行高亮 
"""
def read_and_write(file):
    short_sample = open('short_sample', 'w')
    for i, line in enumerate(file):
        if i >= length: break

        tokens = token(clean(line.lower()))
        print(tokens)
        short_sample.write(' '.join(tokens) + '\n')

    short_sample.close()


if __name__ == '__main__':
    content = open('short_sample').read()
    PAT = r'(山东|河南)\w+'

    searched = re.sub(PAT, r'\n## \g<1>: \n \g<0>', content)

    with open('result.md', 'w') as f:
        f.write(searched)




