input()

ip_list = [int(i) for i in input().split()]
res = 1
for a_num in ip_list:
    res *= a_num
print(res)
