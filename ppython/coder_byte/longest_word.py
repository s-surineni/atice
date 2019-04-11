import re
def LongestWord(sen): 
    words = re.split("[^a-zA-Z]", sen)
    print(words)
    len_dict = {}
    longest = 0
    for word in words:
        if longest < len(word):
            longest = len(word)
            if longest in len_dict:
                len_dict[longest].append(word)
            else:
                len_dict[longest] = [word]
    # print(len_dict)
    # code goes here 
    return len_dict[longest][0]
    
# keep this function call here  
print( LongestWord(input()))
