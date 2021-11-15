# hashTable[i] stores all characters 
# that correspond to digit i in phone 
hashTable = ["", "", "abc", "def", "ghi", "jkl", 
					"mno", "pqrs", "tuv", "wxyz"] 

# A recursive function to print all 
# possible words that can be obtained 
# by input number[] of size n. The 
# output words are one by one stored 
# in output[] 
def printWordsUtil(number, curr, output, n): 
	if(curr == n): 
		print(output) 
		return
		
	# Try all 3 possible characters 
	# for current digir in number[] 
	# and recur for remaining digits 
	for i in range(len(hashTable[number[curr]])): 
		output.append(hashTable[number[curr]][i]) 
		printWordsUtil(number, curr + 1, output, n) 
		output.pop() 
		if(number[curr] == 0 or number[curr] == 1): 
			return; 
			
# A wrapper over printWordsUtil(). 
# It creates an output array and 
# calls printWordsUtil() 
def printWords(number, n): 
	printWordsUtil(number, 0, [], n) 
	
# Driver function 
if __name__ == '__main__': 
	number = [0, 2] 
	n = len(number) 
	printWords(number, n); 
	
# This code is contributed by prajmsidc 


def letterCombinations(digits):
        ans = []
        temp = []
        nums = ['2', '3', '4', '5', '6', '7', '8', '9']
        chars = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        mapping = {i: j for i, j in zip(nums, chars)}
        if len(digits) == 0:
            return ans
        def backtrack(ans, digits, index, temp):
            if len(temp) == len(digits):
                ans.append(''.join(temp))
                return
            for c in mapping[digits[index]]:
                temp.append(c)
                backtrack(ans, digits, index + 1, temp)
                temp.pop()
        backtrack(ans, digits, 0, temp)
        return ans


print(letterCombinations('32'))
