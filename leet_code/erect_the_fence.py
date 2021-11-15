# HTTP://leetcode.com/problems/erect-the-fence
def orientation(p1, p2, p3):
    return (p2[1] - p1[1]) * (p3[0] - p2[0]) - (p2[0] - p1[0]) * (p3[1] - p2[1])


def in_between(p1, p2, p3):
    a = p2[0] >= p1[0] and p2[0] <= p3[0] or p2[0] <= p1[0] and p2[0] >= p3[0]
    b = p2[1] >= p1[1] and p2[1] <= p3[1] or p2[1] <= p1[1] and p2[1] >= p3[1]
    return a and b


def erect_the_fence(trees):
    if len(trees) < 4:
        return trees

    left_most = 0
    for trk in range(1, len(trees)):
        if trees[trk][0] < trees[left_most][0]:
            left_most = trk

    p1 = left_most

    hull = set()
    while True:
        p2 = (p1 + 1) % len(trees)

        for trk in range(len(trees)):
            if orientation(trees[p1], trees[trk], trees[p2]) < 0:
                p2 = trk

        for trk in range(len(trees)):
            if (
                trk != p1
                and trk != p2
                and orientation(trees[p1], trees[trk], trees[p2]) == 0
                and in_between(trees[p1], trees[trk], trees[p2])
            ):
                hull.add(tuple(trees[trk]))
        hull.add(tuple(trees[p2]))
        p1 = p2
        if p1 == left_most:
            break
    return hull


points = [[1, 1], [2, 2], [2, 0], [2, 4], [3, 3], [4, 2]]
print(erect_the_fence(points))
