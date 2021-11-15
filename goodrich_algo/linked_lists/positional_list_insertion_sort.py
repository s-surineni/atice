from goodrich_algo.linked_lists.positional_list import PositionalList


def insertion_sort(pos_list):
    marker = pos_list.get_first()
    if len(pos_list) == 0:
        return pos_list
    while marker != pos_list.get_last():
        pivot = pos_list.get_after_node(marker)
        value = pivot.get_element()
        if value > marker.get_element():
            marker = pivot
        else:
            while (marker != pos_list.get_first()
                   and pos_list.get_before_node(marker).get_element() > value):
                marker = pos_list.get_before_node(marker)
            pos_list.add_before(marker, value)
            pos_list.delete(pivot)


pos_list = PositionalList()
pos_list.add_last(15)
pos_list.add_last(22)
pos_list.add_last(25)
pos_list.add_last(29)
pos_list.add_last(36)
pos_list.add_last(23)
pos_list.add_last(53)
pos_list.add_last(11)
pos_list.add_last(42)
for val in pos_list:
    print(val)
# print(pos_list)
insertion_sort(pos_list)
print('after sort')
# print(pos_list)
for val in pos_list:
    print(val)
