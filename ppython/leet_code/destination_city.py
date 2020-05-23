def find_destination_city(paths):
    from_set = set()
    to_set = set()

    for a_path in paths:
        from_set.add(a_path[0])
        to_set.add(a_path[1])

    return list(to_set - from_set)[0]


if __name__ == '__main__':
    paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
    print(find_destination_city(paths))
