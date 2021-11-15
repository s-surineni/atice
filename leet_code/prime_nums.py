import time

def get_prime_nums(count, begin = 0):
    start_time = time.perf_counter()
    curr_num = 0 + begin
    curr_count = 0
    prime_list = []

    idx = 1
    while curr_count <= count:
        curr_factor = 1
        tot_factors = 0
        start_time2 = time.perf_counter()

        while curr_factor <= curr_num:
            if curr_num % curr_factor == 0:
                tot_factors += 1
            curr_factor += 1

        if tot_factors == 2:
            prime_list.append(curr_num)
            end_time = time.perf_counter()
            print('took {} seconds to calculate {}th prime {}'.format(
                end_time - start_time2,
                idx, curr_num
            ))
            idx += 1
            curr_count += 1
        curr_num += 1
    end_time = time.perf_counter()
    print('Took {} seconds to calculate {} primes'.format(
        end_time - start_time, len(prime_list)
    ))
    return prime_list


print(get_prime_nums(30000, 10000))
