def maxCandies(status, candies, keys, containedBoxes, initialBoxes):
    boxes = set(initialBoxes)
    bfs = [i for i in boxes if status[i]]
    for i in bfs:
        for j in containedBoxes[i]:
            boxes.add(j)
            if status[j]:
                bfs.append(j)
        for j in keys[i]:
            if status[j] == 0 and j in boxes:
                bfs.append(j)
            status[j] = 1
    return sum(candies[i] for i in bfs)


status = [1,0,1,0]
candies = [7,5,4,100]
keys = [[],[],[1],[]]
containedBoxes = [[1,2],[3],[],[]]
initialBoxes = [0]
print(maxCandies(status, candies, keys, containedBoxes, initialBoxes))
