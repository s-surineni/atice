def count_and_say(nth):
    res = "1"
    ith = 1
    while ith < nth:
        res += "$"
        next_res = []
        char = res[0]
        count = 1
        for idx in range(1, len(res)):
            if res[idx] == char:
                count += 1
            else:
                next_res.append(str(count))
                next_res.append(char)
                char = res[idx]
                count = 1
        res = next_res
        ith += 1
    return "".join(res)


nth = 1
nth = 2
nth = 3
nth = 4
print(count_and_say(nth))
