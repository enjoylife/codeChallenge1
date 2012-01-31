import time
import glob
import subprocess
import random
from itertools import cycle, islice,  combinations as nCr

def print_timing(func):
    def wrapper(*arg):
        t1 = time.time()
        res = func(*arg)
        t2 = time.time()
        print '%s took %0.3f ms' % (func.func_name, (t2-t1)*1000.0)
        return res
    return wrapper

@print_timing
def party_combo(iterable):
    for name in nCr(iterable,2):
       print name 


def random_combination(iterable, r):
    "Random selection  without using itertools.combinations(iterable, r)"

    pool = tuple(iterable)
    n = len(pool)
    indices = sorted(random.sample(xrange(n), r))
    return tuple(pool[i] for i in indices)

def bufcount(filename):
    """ Count the number of Lines in a file

    Credit: Mykola Kharechko http://stackoverflow.com/a/845151 """
    f = open(filename)
    lines = 0
    buf_size = 1024 * 1024
    read_f = f.read # loop optimization

    buf = read_f(buf_size)
    while buf:
        lines += buf.count('\n')
        buf = read_f(buf_size)

    return lines

if __name__=='__main__':
    
    first = open('shortdata.txt', 'r')
    print 'Now creating List'
    party_combo(first)
    #print random_combination(first,2)
    first.close()


