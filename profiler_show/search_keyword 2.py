import re
from itertools import chain, repeat


def sub_pat(keyword, string):
    return re.sub(r'({})'.format(keyword), r'#\g<1>#', string)


def search(keyword, dataframe, topn=80000 * 80):
    all_string = ""
    for row in chain(*repeat(dataframe['content'], 40)):
        row = str(row)
        if keyword in row:
            all_string += row + '\n'
        #row = str(row)
        #if keyword in row:
            #yield sub_pat(keyword, row)
    return sub_pat(keyword, all_string).split('\n')
   
