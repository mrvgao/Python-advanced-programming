import time
from collections import defaultdict
import datetime


def count_words(filename):
    counts = defaultdict(int)
    
    time.sleep(1)

    return counts

def get_all_results(files):

    return (count_words(f) for f in files)
    #return [count_words(f) for f in files]

    """
    results = []

    for f in files:
        yield count_words(f)

    """
    

    

def update_remote_db(k, v):
    pass

def collect_results(files):
    results = defaultdict(int)

    for c in get_all_results(files):
        print('get one {}'.format(datetime.datetime.now()))
        for k, v in c:
            update_remote_db(k, v)
            results[k] += v


if __name__  == '__main__':
    files = ['some_file'] * 5
    # 9999 Error
    print('programming running at {}'.format(datetime.datetime.now()))
    collect_results(files)



    



