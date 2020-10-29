def reconstructQueue(people):
    people.sort(key=lambda h: (-h[0], h[1]))
    queue = []
    for p in people:
        queue.insert(p[1], p)
    return queue


people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
print(reconstructQueue(people))
