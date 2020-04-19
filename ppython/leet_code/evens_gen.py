def get_nums_gen(limit):
    begin = 0
#     even_list = []
    while begin <= limit:
        if begin %2 == 0:
#             even_list.append(begin)
            yield begin
        begin += 1


for val in get_nums_gen(9):
    print(val)
