def maximize_array(vals, key):
    val_map = set()
    pos = 0
    while key > 2 ** pos:
        if key | (2 ** pos) == key:
            val_map.add(pos)
        pos += 1

    while val_map:
        temp_set = set()
        for vl in vals:
            for key in val_map:
                if (2 ** key) | vl > vl:
                    temp_set.add(key)
        val_map -= temp_set
    # final left over keys value
    left = 0
    for key in val_map:
        left += (2 ** key)
    return sum(vals) + key - left



vals = [8, 7, 1, 8, 2]
key = 5
print(maximize_array(vals, key))
