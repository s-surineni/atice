class Trie:
    def __init__(self):
        self.root = self._TrieNode()

    def insert_word(self, word):
        curr_node = self.root
        for ch in word:
            if ch not in curr_node.char_dict:
                curr_node.char_dict[ch] = self._TrieNode()
            curr_node = curr_node.char_dict[ch]
        curr_node.char_dict[ch].word_end = True

    class _TrieNode:
        def __init__(self):
            self.char_dict = {}
            self.word_end = False


class StreamChecker:
    def __init__(self, words):
        self.charseq = []
        self._trie = Trie()
        for a_word in words:
            self._trie.insert_word(a_word)

    def query(self, letter):
        self.charseq.append(letter)
        curr_node = self._trie.root
        for idx in range(len(self.charseq) - 1, -1, -1):
            if self.charseq[idx] in curr_node.char_dict:
                curr_node = curr_node.char_dict[self.charseq[idx]]
                if curr_node.word_end:
                    return True
            else:
                return False
        return False
