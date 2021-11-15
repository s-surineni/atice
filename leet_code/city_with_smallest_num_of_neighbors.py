def find_cities_with_threshold_distance(weighted_graph, city, distanceThreshold, reachable, travelled):
    for dest in weighted_graph[city]:
        if travelled + dest[1] <= distanceThreshold:
            if dest[0] in reachable:
                return
            else:
                reachable.append(dest[0])
            find_cities_with_threshold_distance(weighted_graph, dest[0], distanceThreshold, reachable, travelled + dest[1])

def find_the_city(n, edges, distanceThreshold):
    weighted_graph = {}
    for an_edge in edges:
        if weighted_graph.get(an_edge[0]):
            weighted_graph[an_edge[0]].append(an_edge[1:])
        else:
            weighted_graph[an_edge[0]] = [an_edge[1:]]

        if weighted_graph.get(an_edge[1]):
            weighted_graph[an_edge[1]].append([an_edge[0], an_edge[-1]])
        else:
            weighted_graph[an_edge[1]] = [[an_edge[0], an_edge[-1]]]
    for ed in range(n):
        if ed not in weighted_graph:
            weighted_graph[ed] = []
    min_reachable = n
    min_reachable_city = 'something'
    for city in weighted_graph:
        reachable = []
        find_cities_with_threshold_distance(weighted_graph, city, distanceThreshold, reachable, 0)
        if city in reachable:
            reachable.remove(city)
        if min_reachable > len(reachable):
            min_reachable_city = city
            min_reachable = len(reachable)
        if min_reachable == len(reachable):
            min_reachable_city = min_reachable_city if min_reachable_city > city else city
        print(city, reachable)
        print(min_reachable_city, 'min_reachable_city')
    return min_reachable_city

# n = 4
# edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]]
# distanceThreshold = 4

# n = 5
# edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]]
# distanceThreshold = 2

# n = 6
# edges = [[0,3,7],[2,4,1],[0,1,5],[2,3,10],[1,3,6],[1,2,1]]
# distanceThreshold = 417

n = 6
edges = [[2,3,7],[2,5,8],[0,2,8],[4,5,5],[1,5,10],[3,4,3],[0,5,9],[1,2,1]]
distanceThreshold = 3269
print(find_the_city(n, edges, distanceThreshold))


