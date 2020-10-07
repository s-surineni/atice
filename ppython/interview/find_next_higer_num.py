num = input('Enter the number: ').strip()
num_list = [int(i) for i in num]
num_len = len(num_list)

for idx in range(num_len - 1, 0, -1):
    if num_list[idx - 1] < num_list[idx]:
        break
val = num_list[idx - 1]
valg = num_list[idx]

idx3 = idx
idx -= 1

for idx2, valgg in enumerate(num_list[(idx + 1):]):
    if valg > valgg > val:
        idx3 = idx2 + idx
        valg = valgg
num_list[idx], num_list[idx3] = num_list[idx3], num_list[idx]
num_list[idx + 1:] = sorted(num_list[idx + 1:])
print(num_list)
