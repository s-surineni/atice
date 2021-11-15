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

    def _delete_helper(self, p_node, key, level):
        if p_node:
            if level == len(key):
                if p_node.find_if_leaf_node:
                    p_node.is_end_of_word = False
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
        key_length = len(key)
        if key_length > 0:
            self._delete_helper(self.root, key, 0)

    def display_contacts_util(self, trie_node, prefix):
        if trie_node.find_if_leaf_node():
            print(prefix, end=' ')

        for alph in range(0, 26):
            if trie_node.children[alph]:
                # print(chr(ord('a') + alph), end='')
                self.display_contacts_util(trie_node.children[alph], prefix + chr(ord('a') + alph))

                # print()

    def display_contacts(self, search_str):
        trie_node = self.root
        for a_char in range(len(search_str)):
            prefix = search_str[:a_char + 1]
            trie_node = trie_node.children[self._char_to_index(search_str[a_char])]

            if not trie_node:
                # print('No results found at {}'.format(search_str[a_char]))
                print(0)
                break
            # print('results of {}'.format(search_str[:a_char + 1]))
            # print(search_str[:a_char + 1], end='')
            self.display_contacts_util(trie_node, prefix)
            print()
        for a_char in range(a_char + 1, len(search_str)):
            print(0)


test_cases = int(input().strip())

for a_tc in range(test_cases):
    str_count = int(input().strip())
    ip_strs = input().strip().split()
    search_str = input().strip()

    a_trie = Trie()
    for an_ip_str in ip_strs:
        a_trie.insert(an_ip_str)
    a_trie.display_contacts(search_str)
# https://practice.geeksforgeeks.org/problems/phone-directory/0
