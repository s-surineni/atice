# pre_fs_sec are kind of global variable, how can we implement otherwise
#
def recover_tree_recur(root, pre_fs_sec):
    if not root:
        return

    recover_tree_recur(root.left, pre_fs_sec)
    # print('root_val', root.val)
    if not pre_fs_sec[1] and pre_fs_sec[0].val > root.val:
        pre_fs_sec[1] = pre_fs_sec[0]

    if pre_fs_sec[1] and pre_fs_sec[0].val > root.val:
        pre_fs_sec[2] = root

    pre_fs_sec[0] = root
    recover_tree_recur(root.right, pre_fs_sec)


def recover_tree(root):
    pre_fs_sec = [None] * 3
    pre_fs_sec[0] = TreeNode(- sys.maxsize)
    recover_tree_recur(root, pre_fs_sec)
    pre_fs_sec[1].val, pre_fs_sec[2].val = pre_fs_sec[2].val, pre_fs_sec[1].val
