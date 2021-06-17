class Trie:
    def __init__(self):
        self.last = False
        self.nxt = [None] * 26
        self.idx = -1
        self.pals = []


def get_pos(ch):
    return ord(ch) - ord('a')

def is_palindrome(word, st, ed):
    while st < ed:
        if word[st] != word[ed]:
            return False
        st += 1
        ed -= 1
    return True


def add_word(root, word, idx):
    for trk in range(len(word) - 1, -1, -1):
        ch = word[trk]
        pos = get_pos(ch)
        if not root.nxt[get_pos(ch)]:
            root.nxt[pos] = Trie()
        if is_palindrome(word, 0, trk):
            root.pals.append((idx))
        root = root.nxt[pos]
    root.last = True
    root.idx = idx
    root.pals.append(idx)

def find_pairs(idx, word, root):
    pals_idx = []
    for idx2, ch in enumerate(word):
        chi = get_pos(ch)
        if root.idx >=0 and root.idx != idx and is_palindrome(word, idx2, len(word) - 1):
            pals_idx.append((idx, root.idx))

        root = root.nxt[chi]
        if not root:
            return pals_idx
    
    # if root.last and root.idx != idx:
    #     pals_idx.append(root.idx)
    for x in root.pals:
        if x == idx:
            continue
        pals_idx.append((idx, x))
    return pals_idx

def find_palindrome_pairs(words):
    root = Trie()
    for trk, a_w in enumerate(words):
        add_word(root, a_w, trk)

    all_pairs = []
    for trk, a_w in enumerate(words):
        pals = find_pairs(trk, a_w, root)
        # if not pals:
        #     continue
        # for vi in pals:
        #     all_pairs.append((trk, vi))
        all_pairs.extend(pals)
    return all_pairs

words = ["abcd", "dcba", "lls", "s", "sssll"]
# words = ["a",""]
print(find_palindrome_pairs(words))
