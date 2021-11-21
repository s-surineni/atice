def find_str(haystack, needle):
    if not needle:
        return 0
    hlen = len(haystack)
    nlen = len(needle)
    # for hid in range(hlen):
    #     if hlen - hid < nlen:
    #         return -1
    for hid in range(hlen - nlen + 1):
        # (Better) (Notice)by running loop till nlen we avoided if this is the last character if contition
        for nid in range(nlen + 1):
            if nid == nlen:
                return hid
            if haystack[hid + nid] != needle[nid]:
                break
    return -1


haystack = "hello"
needle = "ll"
haystack = ""
needle = "a"
haystack = "mississippi"
needle = "mississippi"
print(find_str(haystack, needle))
