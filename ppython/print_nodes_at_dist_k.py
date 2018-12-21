class Node:
    def __init__(self, data):
        self.data = data
        self.lc = None
        self.rc = None


def printKDistanceNodeDown(root, dist):
    if not root:
        return

    if dist == 0:
        print(root.data)
        return

    printKDistanceNodeDown(root.lc, dist - 1)
    printKDistanceNodeDown(root.rc, dist - 1)


def printKDistanceNode(root, target, k):
    if not root:
        return -1

    if root == target:
        printKDistanceNodeDown(target, k)
        return 0                # couldn't we return 1 here??

    dl = printKDistanceNode(root.lc, target, k)

    if dl != -1:
        if dl + 1 == k:
            print(root.data)

        else:
            printKDistanceNodeDown(k - dl - 2)

        return dl + 1

    dr = printKDistanceNode(root.rc, target, k)

    if dr != -1:
        if dr + 1 == k:
            print(root.data)

        else:
            printKDistanceNodeDown(k - dr - 2)

        return dr + 1
    return -1
