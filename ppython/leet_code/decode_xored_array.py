def decode(enc_list, first):
    res = [first]
    for en in enc_list:
        res.append(en ^ res[-1])
    return res
