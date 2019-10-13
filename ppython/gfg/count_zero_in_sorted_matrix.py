tc = int(input().strip())
dim = int(input().strip())
elements = input().strip().split()
zero_count = 0

for row in range(dim):
    for col in range(dim):
        # print(elements[(row * dim) + col])
        if elements[(row * dim) + col] == '1':
            break
        zero_count += 1

print(zero_count)
