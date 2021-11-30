# https://leetcode.com/problems/maximal-rectangle/
def find_max_area(histogram):
    stack = []
    area = 0
    max_area = 0
    for idx, val in enumerate(histogram):
        if stack and val < histogram[stack[-1]]:
            while stack and histogram[stack[-1]] > val:
                higher_idx = stack.pop()
                if stack:
                    # (Notice) notice how we are using stack[-1] instead of higher_idx
                    # check the sample 3 1 3 2 2 to see why
                    area = histogram[higher_idx] * (idx - stack[-1] - 1)
                else:
                    area = histogram[higher_idx] * idx
                max_area = max(max_area, area)
        stack.append(idx)
    idx += 1
    while stack:
        top = stack.pop()
        if stack:
            area = histogram[top] * (idx - stack[-1] - 1)
        else:
            area = histogram[top] * len(histogram)
        max_area = max(max_area, area)
    return max_area


# print(find_max_area([1, 1]))
# print(find_max_area([1, 2]))
# print(find_max_area([2, 1]))
# print(find_max_area([2, 1, 2]))
# print(find_max_area([4, 3, 2, 1]))


def find_maximum_rectangle(matrix):

    # matrix = [int(val) for row in matrix for val in row]
    matrix = [[int(val) for val in row] for row in matrix]
    # print("*" * 80)
    # print("ironman matrix", matrix)
    row_sum = matrix[0]
    max_area = find_max_area(row_sum)
    idx = 1
    while idx < len(matrix):
        for cid in range(len(matrix[0])):
            row_sum[cid] += matrix[idx][cid]
            if not matrix[idx][cid]:
                row_sum[cid] = 0
        max_area = max(max_area, find_max_area(row_sum))
        idx += 1
    return max_area


matrix = [
    ["1", "0", "1", "0", "0"],
    ["1", "0", "1", "1", "1"],
    ["1", "1", "1", "1", "1"],
    ["1", "0", "0", "1", "0"],
]
# matrix = [["0", "1"]]
# matrix = [["0", "1"], ["1", "0"]]
print(find_maximum_rectangle(matrix))
