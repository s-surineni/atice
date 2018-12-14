ip_list = input('Enter the numbers').strip().split()

for idx in range(1, len(ip_list)):
    i = idx - 1
    a_key = ip_list[idx]
    while i >= 0 and ip_list[i] > a_key:
        ip_list[i + 1] = ip_list[i]
        i -= 1
    ip_list[i + 1] = a_key

print(ip_list)
