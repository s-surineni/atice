def find_orderly_queue(srn, k):
    if k > 1:
        return ''.join(sorted(srn))
    else:
        return min([srn[k:] + srn[:k] for k in range(len(srn))])


srn = "cba"
k = 1
print(find_orderly_queue(srn, k))
srn = "baaca"
k = 3
print(find_orderly_queue(srn, k))
