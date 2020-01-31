def decrypt_str_from_alpha(strn):
    idx = 0
    resp_str = ''
    while idx < len(strn):
        val = None
        if (idx + 2) < len(strn) and strn[idx + 2] == '#':
            val = strn[idx] + strn[idx + 1]
            idx += 3
        else:
            val = strn[idx]
            idx += 1
        print(val)
        resp_str += chr(ord('a') + int(val) - 1)
    return resp_str

# def freqAlphabets(self, s):
#     return ''.join(chr(int(i[:2]) + 96) for i in re.findall(r'\d\d#|\d', s))
print(decrypt_str_from_alpha("10#11#12"))
