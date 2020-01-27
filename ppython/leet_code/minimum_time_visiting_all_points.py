def find_minimum_time(points):
    min_dist = 0

    for idx, a_point in enumerate(points):
        if idx == (len(points) - 1):
            break
        next_point = points[idx + 1]
        min_dist += max(abs(a_point[0] - next_point[0]), abs(a_point[1] - next_point[1]))
    return min_dist


print(find_minimum_time([[1,1],[3,4],[-1,0]]))


def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        return sum(max(abs(c - p) for c, p in zip(cur, prev)) for cur, prev in zip(points, points[1 :]))  # !! see how current and next element are fetched using zip function
