"""
Convert a file with \r's into a file with \n's.
"""

import sys
def main():
    if len(sys.argv) != 3:
        print("""
        Usage:
            python tonl.py <in_file> <out_file>
        """)
        sys.exit(1)
    fin = open(sys.argv[1], 'r')
    fout = open(sys.argv[2], 'w', newline='\n')
    for line in fin.readlines():
        fout.write(line.rstrip('\r\n') + '\n')
    fin.close()
    fout.close()

if __name__ == '__main__':
    main()

