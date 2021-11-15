def find_incr_teams(ratings, team, start_idx, size):
    team_len = len(team)
    if team_len == size:
        return team
    if start_idx == len(ratings):
        return
    res_list = []
    for idx, val in enumerate(ratings[start_idx:]):
        if val > team[-1]:
            res = find_incr_teams(ratings, team + [val], start_idx + idx + 1, size)
            if res and team_len < 2:
                res_list.extend(res)
            if res and team_len == 2:
                res_list.append(res)
    return res_list

def find_decr_teams(ratings, team, start_idx, size):
    team_len = len(team)
    if team_len == size:
        return team
    if start_idx == len(ratings):
        return
    res_list = []
    for idx, val in enumerate(ratings[start_idx:]):
        if val < team[-1]:
            res = find_decr_teams(ratings, team + [val], start_idx + idx + 1, size)
            if res and team_len < 2:
                res_list.extend(res)
            if res and team_len == 2:
                res_list.append(res)
    return res_list
      
class Solution:
    def numTeams(self, rating):
#         Increasing
        res_list = []
        for idx, val in enumerate(rating):
            team = [val]
            res = find_incr_teams(rating, team, idx + 1, 3)
            if res:
                res_list.extend(res)


# decreasing

        for idx, val in enumerate(rating):
            team = [val]
            res = find_decr_teams(rating, team, idx + 1, 3)
            if res:
                res_list.extend(res)
        return (res_list)

print(Solution().numTeams([3,6,7,5,1]))
