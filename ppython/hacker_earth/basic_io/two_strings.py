'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here

tc = int(input())
for at in range(tc):
    alphas = [0] * 26

    s1, s2 = input().split()
    # print(s1, s2)
    for c in s1:
        alphas[ord('a') - ord(c)] += 1
    for c in s2:
        alphas[ord('a') - ord(c)] -= 1
    
    for val in alphas:
        if val != 0:
            print('NO')
            break
    else:
        print('YES')
