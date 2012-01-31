import glob

def clean_data(files, newfile):
    """ Helper to clean the data """

    names = set()
    for file in files:
        with open(file, 'r') as data:
            print 'cleaning %s' % file
            for line in data:
                data =line.split() #only want names, don't need stats
                names.add(data[0].capitalize())

    with open('data/%s' % newfile, 'w') as clean: #cleaned now write it out for later
        for name in names:
            clean.write("%s\n" % name)

if __name__ == '__main__':

    #Get all the cluttered data for cleaning
    first_names = glob.glob('data/f*.txt')
    last_names = glob.glob('data/l*.txt')

    # Clean it
    clean_data(first_names, 'cleanfirst.txt')
    clean_data(last_names, 'cleanlast.txt')


