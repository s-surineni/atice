import collections


def main():
    tc = int(input().strip())
    vert, ed = [int(i) for i in input().strip().split()]
    graph = collections.defaultdict(list)
    all_vert = set()
    for _ in range(ed):
        s1, s2, we = [int(i) for i in input().strip().split()]
        graph[s1].append((s2, we))
        graph[s2].append((s1, we))
        all_vert.add(s1)
        all_vert.add(s2)

    all_vert = list(all_vert)
    qu = []
    for idx, val in enumerate(all_vert):
        qu.append([val, 0])
    # qu[0][1] = float('inf')
    # qu.sort(key=lambda val1: val1[1])
    print(qu)
    dist = 0
    while all_vert:
        curr_vert = qu.pop()
        print('*' * 80)
        print('iron man curr_vert', curr_vert)
        dist += curr_vert[1]
        print('*' * 80)
        print('iron man all_vert', all_vert)
        all_vert.remove(curr_vert[0])
        for ver in graph[curr_vert[0]]:
            # print('*' * 80)
            # print('iron man ver', ver)
            if ver[0] in all_vert:
                for idx, val2 in enumerate(qu):
                    if val2[0] == ver[0] and val2[1] < ver[1]:
                        qu[idx] = [ver[0], ver[1]]
        qu.sort(key=lambda val1: val1[1])
    print(dist)
main()
