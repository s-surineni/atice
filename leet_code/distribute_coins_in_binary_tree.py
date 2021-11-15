def distribute_coins_ib_binary_tree(root):
    if not root:
        return 0, 0

    l_moves, l_coins = distribute_coins_ib_binary_tree(root.left)
    r_moves, r_coins = distribute_coins_ib_binary_tree(root.right)
    moves = l_moves + r_moves
    return moves, (root.val - 1) + (l_coins) + (r_coins)
