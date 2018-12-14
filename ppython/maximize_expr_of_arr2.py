def insertion_sort(ip_list):
    for idx in range(1, len(ip_list)):
        i = idx - 1
        a_key = ip_list[idx]
        while i >= 0 and ip_list[i] > a_key:
            ip_list[i + 1] = ip_list[i]
            i -= 1
        ip_list[i + 1] = a_key


test_cases = int(input().strip())

for a_tc in range(test_cases):
    input()
    ip_list = input().strip().split()
    ip_list = [int(i) for i in ip_list]
    ip_list.sort()

    val = 0
    for idx in range(len(ip_list)):
        val += idx * ip_list[idx]
    print(val % ((10 ** 9) + 7))
