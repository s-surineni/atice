# https://practice.geeksforgeeks.org/problems/return-two-prime-numbers/0

def sieve_of_erastosthene(num):
    primes_vals = [True] * num

    curr_num = 2

    while curr_num <= num:
        
test_cases = int(input().strip())

for a_tc in range(test_cases):
    eve = int(input().strip())

    primes_vals = sieve_of_erastosthene(eve)
