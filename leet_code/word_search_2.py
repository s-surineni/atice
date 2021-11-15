class TrieNode:
    def __init__(self):
        self._next = [None] * 26
        self._word = None


def build_trie(word_list):
    root = TrieNode()
    for a_word in word_list:
        node = root
        for ch in a_word:
            ch_idx = ord(ch) - ord("a")
            if not node._next[ch_idx]:
                node._next[ch_idx] = TrieNode()
            node = node._next[ch_idx]
        node._word = a_word  # [Note] special treatment
    return root


def dfs(row, col, cross_word, root, res):
    ch_idx = ord(cross_word[row][col]) - ord("a")
    if cross_word[row][col] == "#" or not root._next[ch_idx]:
        return
    root = root._next[ch_idx]

    if root._word:
        res.append(root._word)
        root._word = None

    cross_word[row][col] = "#"
    for ri, ci in ((row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)):
        if 0 <= ri < len(cross_word) and 0 <= ci < len(cross_word[0]):
            dfs(ri, ci, cross_word, root, res)
    cross_word[row][col] = chr(ch_idx + ord("a"))


def search_words(cross_word, word_list):
    root = build_trie(word_list)
    res = []
    for row in range(len(cross_word)):
        for col in range(len(cross_word[0])):
            dfs(row, col, cross_word, root, res)
    return res


board = [
    ["o", "a", "a", "n"],
    ["e", "t", "a", "e"],
    ["i", "h", "k", "r"],
    ["i", "f", "l", "v"],
]
words = ["oath", "pea", "eat", "rain"]

board = [["a"]]
words = ["a"]
print(search_words(board, words))
