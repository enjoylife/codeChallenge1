from itertools import combinations as nCr
import timeit
import glob
import subprocess
import random

def random_combination(iterable, r):
    "Random selection using itertools.combinations(iterable, r)"
    pool = tuple(iterable)
    n = len(pool)
    indices = sorted(random.sample(xrange(n), r))
    return tuple(pool[i] for i in indices)

def combo(pattern):
    files = glob.glob(pattern)
    for file in files:
        print "creating sets of length 2 from file %s" % file
        with open(file, 'r') as data:
            combos = nCr(data,2)
            for c in combos:
                print c
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
    t = timeit.Timer("bufcount('l.txt')", "from __main__ import bufcount")
    print t.timeit(100)


    #print file_len('m.txt')
    #print random_combination(open('m.txt','r'),2)




