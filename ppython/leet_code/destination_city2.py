def find_destination_city(paths):
    from_to = {}

    for a_path in paths:
        from_to[a_path[0]] = a_path[1]

    start = a_path[1]

    while from_to.get(start):
        start = from_to[start]

    return start


if __name__ == '__main__':
    paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
    print(find_destination_city(paths))
