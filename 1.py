import os
start_folder = '/home'
for dirName, subdirList, fileList in os.walk(start_folder):
    print('Found directory: %s' % dirName)
    for fname in fileList:
        print('\t%s' % fname)
