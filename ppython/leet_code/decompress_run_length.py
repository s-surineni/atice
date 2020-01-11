nums = [int(i) for i in input('please enter numbers separated by commas: ').split(',')]
print(nums)
num_len = len(nums)
idx = 0
op_list = []
while idx < num_len:
    freq = nums[idx]
    val = nums[idx + 1]
    for idx2 in range(freq):
        op_list.append(val)
    idx += 2
print(op_list)
