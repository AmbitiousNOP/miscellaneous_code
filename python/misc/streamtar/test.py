import tarfile

fileName = "test.tgz"

tfile = tarfile.open(fileName, 'r|gz')

#print(tfile.getmembers())

#print(tfile.list(verbose=True))

for t in tfile:
    print(t.isfile(), t.name)
    if t.isfile():
        f = tfile.extractfile(t)
        if f:
            print(len(f.read()))
    


'''
for t in tfile:
    f = tfile.extractfile(t)
    print(len(f.read()))
'''
