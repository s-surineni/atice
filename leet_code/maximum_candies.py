def max_candies(status, candies, keys, containedBoxes, initialBoxes):
    boxes_we_have = set(initialBoxes)
    boxes_opened = [i for i in boxes_we_have if status[i]]

    for opened_box in boxes_opened:
        for inner_box in containedBoxes[opened_box]:
            if status[inner_box]:
                boxes_opened.append(inner_box)
            boxes_we_have.add(inner_box)
        for a_key in keys[opened_box]:
            if not status[a_key] and a_key in boxes_we_have:
                boxes_opened.append(a_key)
            status[a_key] = 1   # changing it to openend before getting box so that we need not store keys
    return sum([candies[i] for i in boxes_opened])


status = [1,0,0,0]
candies = [1,2,3,4]
keys = [[1,2],[3],[],[]]
containedBoxes = [[2],[3],[1],[]]
initialBoxes = [0]


print(max_candies(status, candies, keys, containedBoxes, initialBoxes))
