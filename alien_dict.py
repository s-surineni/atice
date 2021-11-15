# https://practice.geeksforgeeks.org/problems/alien-dictionary/1
from collections import defaultdict


class Graph:
    def __init__(self, num_of_vertices):
        self.graph = defaultdict(list)
        self.num_of_vertices = num_of_vertices

    def add_edge(self, start, end):
        self.graph[start].append(end)

    def topological_sort_util(self, i, visited, stack):
        visited[i] = True

        for adj_v in self.graph[i]:
            if not visited[adj_v]:
                self.topological_sort_util(adj_v, visited, stack)
        stack.insert(0, i)

    def topological_sort(self):
        visited = [False] * self.num_of_vertices
        stack = []

        for i in range(self.num_of_vertices):
            if not visited[i]:
                self.topological_sort_util(i, visited, stack)
        # print('stack', stack)
        for a_char in stack:
            print(chr(a_char + ord('a')), end=' ')
        print()
def print_order(words, distinct_char):
    gr = Graph(distinct_char)

    for trk in range(len(words) - 1):
        w1 = words[trk]
        w2 = words[trk + 1]

        for trk2 in range(min(len(w1), len(w2))):
            if w1[trk2] != w2[trk2]:
                gr.add_edge(ord(w1[trk2]) - ord('a'), ord(w2[trk2]) - ord('a'))
                break
    gr.topological_sort()
    # print(gr.graph)

test_cases = int(input().strip())

for a_tc in range(test_cases):
    word_char = input().strip().split()
    num_of_words = int(word_char[0])
    distinct_char = int(word_char[1])

    words = input().strip().split()
    print_order(words, distinct_char)
