import re

sentence = 'I am Hacker'

regex = re.compile('(\w+)' '(\w+) (\w+)')
print(re.search(regex, sentence).groups())
