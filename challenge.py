from itertools import combinations as nCr
import glob
import subprocess
import random

def file_len(fname):
    p = subprocess.Popen(['wc', '-l', fname], stdout=subprocess.PIPE, 
                                              stderr=subprocess.PIPE)
    result, err = p.communicate()
    if p.returncode != 0:
        raise IOError(err)
    return int(result.strip().split()[0])

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


if __name__=='__main__':
    print random_combination(open('m.txt','r'),2)




