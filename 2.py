import os
start_flder = '/home'
for dirName, subdirList, fileList in os.walk(start_flder):
    print('Found directory: %s' % dirName)
    for fname in fileList:
        print('\t%s' % fname)
