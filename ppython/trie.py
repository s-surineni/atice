# https://www.geeksforgeeks.org/trie-insert-and-search/
class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = self.get_node()

    def get_node(self):
        return TrieNode()

    def _char_to_index(self, ch):
        return ord(ch) - ord('a')

    def insert(self, key):
        p_crawl = self.root

        for a_char in key:
            idx = self._char_to_index(a_char)
            if not p_crawl.children[idx]:
                p_crawl.children[idx] = self.get_node()
            p_crawl = p_crawl.children[idx]
        p_crawl.is_end_of_word = True

    def search(self, key):
        p_crawl = self.root

        for a_char in key:
            idx = self._char_to_index(a_char)
            if not p_crawl.children[idx]:
                return False
            p_crawl = p_crawl.children[idx]
        return p_crawl and p_crawl.is_end_of_word



if __name__ == '__main__':
    trie = Trie()
    trie.insert('the')
    trie.insert('these')
    trie.insert('their')
    trie.insert('thaw')

    print(trie.search('the'))
    print(trie.search('there'))
