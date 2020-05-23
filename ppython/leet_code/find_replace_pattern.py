def find_replace_pattern(words, patt):
    matches = []
    for a_word in words:
        patt_set = set()
        word_set = set()
        word_pat = {}
        
        for w, p in zip(a_word, patt):
            if bool({w} - word_set) != bool({p} - patt_set):
                break
            word_set.add(w)
            patt_set.add(p)
            if w in word_pat and word_pat[w] != p:
                break
            else:
                word_pat[w] = p
        else:
            matches.append(a_word)
    return matches


words = ["abc","deq","mee","aqq","dkd","ccc"]
pattern = "abb"
print(find_replace_pattern(words, pattern))
