def find_max_satisfaction(sats, idx, val, t):
    # print('val idx', val, idx)
    if idx >= len(sats):
        return val
    return max(find_max_satisfaction(sats, idx + 1, (val +  (t) * sats[idx]), t + 1),
              find_max_satisfaction(sats, idx + 1, val, t))

class Solution:
    def maxSatisfaction(self, satisfaction):
        return find_max_satisfaction(sorted(satisfaction), 0, 0, 1)


print(Solution().maxSatisfaction([34,-27,-49,-6,65,70,72,-37,-57,92,-72,36,6
,-91,18,61,77
,-91,5
,64,-16
,5,20
,-60
,-94
,-15,-23,-10
,-61,27,89,38,46,57,33,94,-79,43,-67,-73,-39,72,-52,13,65,-82,26,69,67
]))
