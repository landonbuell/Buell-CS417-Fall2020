import os

'''
Test five programs
'''

def write_numbers(numbers, filename):
    f = open(filename, 'w')
    for n in numbers:
        f.write(f"{n}\n")
    f.close()

print('----TESTING is_right-----')
write_numbers([3,4,5], 'test_in.txt')
os.system('python q1-is_right.py < test_in.txt')
write_numbers([3,5,4], 'test_in.txt')
os.system('python q1-is_right.py < test_in.txt')
write_numbers([2,3,4], 'test_in.txt')
os.system('python q1-is_right.py < test_in.txt')

print()

print('----TESTING pi_approx-----')
write_numbers([100], 'test_in.txt')
os.system('python q2-pi_approx.py < test_in.txt')

print()

print('----TESTING reduce-----')
write_numbers([24, 36], 'test_in.txt')
os.system('python q3-reduce.py < test_in.txt')
write_numbers([3, 4], 'test_in.txt')
os.system('python q3-reduce.py < test_in.txt')
write_numbers([-4, 8], 'test_in.txt')
os.system('python q3-reduce.py < test_in.txt')

print()

print('----TESTING diff-----')
write_numbers([12, 28, 32, 40], 'test_1.txt')
os.system('python q4-diff.py test_1.txt test_1.txt')
write_numbers([12, 28, 32, 40], 'test_1.txt')
write_numbers([12, 28, 31, 40], 'test_2.txt')
os.system('python q4-diff.py test_1.txt test_2.txt')
write_numbers([12, 28, 31, 40, 0], 'test_1.txt')
os.system('python q4-diff.py test_1.txt test_2.txt')

print()

print('----TESTING grades-----')
os.system('python q5-grades.py scores.csv')
