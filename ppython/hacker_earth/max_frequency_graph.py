'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''
from collections import defaultdict, deque, Counter

def construct_graph(nodes):
    graph = defaultdict(list)
    for _ in range(nodes - 1):
        u, v = [int(i) for i in input().split()]
        graph[u].append(v)
        graph[v].append(u)
    print(graph)
    return graph
    
def do_queries(graph, paths, curr_node, end, power_freqs, visited):
    visited.add(curr_node)
    if curr_node == end:
        power_freqs.append(freqs[end - 1])
        power_freqs = Counter(power_freqs)
        max_val = 0
        max_q = None
        for vert in power_freqs:
            if power_freqs[vert] > max_val:
                max_val = power_freqs[vert]
                max_q = vert
        print(max_q)
        return True
    else:
        for vert in graph[curr_node]:
            if vert not in visited:
                visited.add(vert)
                res = do_queries(graph, paths, vert, end, power_freqs + [freqs[curr_node - 1]], visited)
                if res:
                    return res
                    break
    # root = 2
    # qu = deque()
    # qu.append(root)
    # power_freqs = []
    # while qu:
    #     curr_node = qu.pop()
    #     for reachable in graph[curr_node]:
    #         if reachable == end:
                
    

nodes = int(input())
freqs = input().split()
graph = construct_graph(nodes)
queries = int(input())
paths = defaultdict()
for q in range(queries):
    start, end = [int(i) for i in input().split()]
    do_queries(graph, paths, start, end, [], set())
