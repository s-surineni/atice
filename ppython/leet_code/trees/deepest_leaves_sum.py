# coding: utf-8

# ╭─sampathsurineni@sampaths-MBP ~/ironman/atice/ppython ‹master*› ‹compenv›
# ╰─$ python -m leet_code.trees.deepest_leaves_sum
from goodrich_algo.trees.linked_binary_tree import LinkedBinaryTree


eles = input('Please enter nodes separated by commas').split(',')

tree = LinkedBinaryTree()
curr_level = [tree._add_root(eles[0])] # I'm accessing protected methods not a good thing !!
next_level = []
curr_idx = 1
num_eles = len(eles)
print('num_eles', num_eles)
while curr_idx < num_eles:
    for a_node in curr_level:
        print('adding chilildren to  {}'.format(a_node.get_element()))
        print('adding index {}'.format(eles[curr_idx]))
        if eles[curr_idx] != 'null':
            new_node = tree._add_left(a_node, eles[curr_idx])
            next_level.append(new_node)

        curr_idx += 1

        print('adding index {}'.format(eles[curr_idx]))
        if eles[curr_idx] != 'null':
            new_node = tree._add_right(a_node, eles[curr_idx])
            next_level.append(new_node)
        curr_idx += 1
        print('curr_idx', curr_idx)

    curr_level = next_level
    next_level = []
    print('curr_idx', curr_idx)

for a_node in tree.inorder():
    print(a_node)
