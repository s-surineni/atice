# https://www.geeksforgeeks.org/trie-insert-and-search/
class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_end_of_word = False

    def find_if_leaf_node(self):
        return self.is_end_of_word

    def find_if_free_node(self):
        for child in self.children:
            if child:
                return False
        return True


class Trie:
    def __init__(self):
        self.root = self.get_node()
        # number of keys stored in the trie
        self.count = 0

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

    # different possibilities
    # part of ip_str is sub_string of string in trie
    # whole ip_str is sub_string of string in trie but is not part of trie
    # whole ip_str is sub_string of string in trie and also is part of trie
    # whole ip_str is part of trie and is only one string in that branch
    # whole ip_str is part of trie and also holds other sub_strings which are part of trie
    def _delete_helper(self, p_node, key, level):
        # needs to be checked as the input string may not be
        # contained in trie and also not a sub string of
        # strings exits in trie
        if p_node:
            # this condition is because the input string may be part of
            # a sting in trie but might not be stored in trie
            if level == len(key):
                # this condition is not necessary as it does not add any
                # change even if it is removed
                if p_node.find_if_leaf_node():
                    p_node.is_end_of_word = False
                # last node will be deleted only when
                # last char of input is last node of a branch
                return p_node.find_if_free_node()
            else:
                index = self._char_to_index(key[level])
                if self._delete_helper(p_node.children[index],
                                       key, level + 1):
                    p_node.children[index] = None
                    return (not p_node.find_if_leaf_node() and
                            p_node.find_if_free_node())
        return False

    def delete_key(self, key):
        # input may be the only string for that branch
        # it may be part of another string
        # it may hold another string in it
        # the input may be substring of a string in trie but is not stored itself
        key_length = len(key)
        if key_length > 0:
            self._delete_helper(self.root, key, 0)


if __name__ == '__main__':
    trie = Trie()
    trie.insert('the')
    trie.insert('these')
    trie.insert('their')
    trie.insert('thaw')

    print(trie.search('the'))
    # print(trie.search('there'))
    print(trie.delete_key('the'))
    print(trie.delete_key('the'))
    print(trie.search('the'))

