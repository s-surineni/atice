from collections import deque


def find_neighbors(word, word_set):
    neighbors = []

    for idx, ch in enumerate(word):
        ch_list = list(word)
        for ali in range(26):
            ch_list[idx] = chr(ord("a") + ali)
            cw = "".join(ch_list)
            if cw != word and cw in word_set:
                neighbors.append(cw)
    return neighbors


def breadth_first_search(begin, graph, word_list):
    que = deque()
    que.append(begin)
    if begin in word_list:
        word_list.remove(begin)
    accounted = set()  # represents words that have been included already

    while que:
        # qs? why don't we remove elemens for word_list as soon as we see in the neighbor
        visited = set()  # to store values in current layer

        for trk in range(len(que)):
            curr_word = que.popleft()
            neighbors = find_neighbors(curr_word, word_list)

            # qs? is this check even necessary
            if curr_word not in graph:
                graph[curr_word] = []
            for nei in neighbors:
                visited.add(nei)
                graph[curr_word].append(nei)
                if nei not in accounted:
                    accounted.add(nei)
                    que.append(nei)

        word_list -= visited


def backtrack(begin, endw, curr_path, shortest_paths, graph):
    if begin == endw:
        shortest_paths.append(curr_path)
        return  # qs? we should return right java doesn't have it

    if begin not in graph:
        return

    for wor in graph[begin]:
        backtrack(wor, endw, curr_path + [wor], shortest_paths, graph)


def find_word_ladder(begin, endw, word_list):
    word_set = set(word_list)
    graph = {}
    breadth_first_search(begin, graph, word_set)
    shortest_paths = []
    curr_path = [begin]
    backtrack(begin, endw, curr_path, shortest_paths, graph)
    return shortest_paths


# beginWord = "a"
# endWord = "c"
# wordList = ["a", "b", "c"]
# print(find_word_ladder(beginWord, endWord, wordList))




beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
print(find_word_ladder(beginWord, endWord, wordList))
