def counting_sort(num_list, place):
    count_list = [0] * 10

    for a_num in num_list:
        a_num //= place
        a_num %= 10
        count_list[a_num % 10] += 1  # -1 because values are from 0 through 9

    num_list_len = len(num_list)
    for idx in range(1, 10):
        count_list[idx] += count_list[idx - 1]

    new_list = [0] * num_list_len
    for idx in range(num_list_len - 1, -1, -1):
        a_num = num_list[idx]
        a_num //= place
        a_num %= 10
        new_list[count_list[a_num % 10] - 1] = num_list[idx]
        count_list[a_num % 10] -= 1
    return new_list


def radix_sort(num_list):
    max_num = max(num_list)

    place = 1

    while max_num // place:
        num_list = counting_sort(num_list, place)
        place *= 10
    return num_list


print(radix_sort([382, 363, 985, 776, 543]))
