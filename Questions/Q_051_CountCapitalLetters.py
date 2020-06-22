"""""""""
Using Python, write code that will read a file and return the number of capital letters. 
Once you have your initial piece of code, see if you can condense into a one-liner. 
"""

file_to_read = '../Utils/Q51_TextFile.txt'
fo = open(file_to_read, 'r')

"""
count = 0
for c in fo.read():
    if ord('A') <= ord(c) <= ord('Z'):
        count += 1

print('Count =', count)     # 28
"""

count_fn = lambda file_name: len([c for c in open(file_name).read() if ord('A') <= ord(c) <= ord('Z')])

print(count_fn(file_to_read))


