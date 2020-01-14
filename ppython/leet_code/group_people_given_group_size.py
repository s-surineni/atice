import collections


groupSizes = [3,3,3,3,3,1,3]
def group_the_people(groups):
    people_groups = {}
    pid = 0
    for a_grp in groups:
        if a_grp in people_groups:
            people_groups[a_grp].append(pid)
            pid += 1
        else:
            people_groups[a_grp] = [pid]
            pid += 1
    res = []
    for grp in people_groups:
        a_slice = 0
        # while a_slice < len(people_groups[grp]):
        for a_slice in range(0, len(people_groups[grp]), grp):
            res.append(people_groups[grp][a_slice: a_slice + grp])
            a_slice += grp
    return res


print(group_the_people(groupSizes))
