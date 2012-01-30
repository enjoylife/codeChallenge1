import glob

#Get all the cluttered data for cleaning
files = glob.glob('*.txt')

for file in files:
    names=[]
    with open(file, 'r') as data:
        for line in data:
            data =line.split()
#only want names
            names.append(data[0])

#cleaned now write it out for later
    with open('%s.txt' % file[0], 'w') as clean:
        for name in names:
            clean.write("%s\n" % name)


