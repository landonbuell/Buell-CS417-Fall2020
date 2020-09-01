'''
Takes two filenames from the command line, and determines
if the files have the same content.
'''

import sys

if len(sys.argv) != 3:
    print('Usage:\n  python diff.py <file1> <file2>')
    sys.exit(1)

file_name1 = sys.argv[1]

# ... write the rest of your code here
