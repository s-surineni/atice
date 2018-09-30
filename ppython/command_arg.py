import sys

print(sys.argv[0])

with open('hello.py', 'a') as hell:
    with open('bye.py', 'a') as bey:
        hell.write('Hello')
        bey.write('Bye')
print('Done')
