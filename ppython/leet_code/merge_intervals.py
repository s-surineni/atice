def merge(intervals):
    intervals = sorted(intervals, key = lambda val: val[0])
    # print('sorted', intervals)
    # new_list = []
    idx = 0
    start_len = len(intervals)
    # idx += 1
    res = []
    while idx < (len(intervals)):
        temp = intervals[idx]

        # print(temp[0])
        # print(intervals[idx][0])
        while (idx + 1) < len(intervals) and temp[0] <= intervals[idx + 1][0] <= temp[1]:
            # intervals[idx:idx + 2] = [intervals[idx][0], intervals[idx + 1][1]]
            if temp[1] > intervals[idx + 1][1]:
                # temp = intervals[idx + 1]
                # temp = intervals[idx]
                pass

                # new_list.append(intervals[idx])
            else:
                # new_list.append([intervals[idx][0], intervals[idx + 1][1]])
                temp = [temp[0], intervals[idx + 1][1]]

            idx += 1
        # else:
        #     new_list.append(intervals[idx])
        #     idx += 1
        else:
            idx += 1
        res.append(temp)
        # temp = intervals[idx]
        # print(res)
    # if idx < len(intervals):
    #     new_list.append(intervals[idx])
    # return new_list
    return res


# print(merge([[1,4],[0,2],[3,5]]))
# print(merge([[1,3],[2,6],[8,10],[15,18]]))
# print(merge([[1,4],[2,3]]))
print(merge([[2,3],[4,5],[6,7],[8,9],[1,10]]))