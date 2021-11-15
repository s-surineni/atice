'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
str1 = input()

for c in range(len(str1) - 1):
    # print(str1[c])
    if str1[c].isdigit() and str1[c + 1].isdigit():
        if (int(str1[c]) + int(str1[c + 1])) % 2 == 1:
            print('invalid')
            break
    if not str1[c].isdigit() and  str1[c] in 'AEIOUY':
        print('invalid')
        break
else:
    print('valid')
