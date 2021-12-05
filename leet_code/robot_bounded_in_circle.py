def find_if_robot_in_circle(instr):
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    cd = 0
    x, y = 0, 0
    for ad in instr:
        if ad == "G":
            x += dirs[cd][0]
            y += dirs[cd][1]
        elif ad == "R":
            cd = (cd + 1) % 4
        elif ad == "L":
            cd = (cd + 3) % 4
    # print(x, y, cd)
    return (x, y) == (0, 0) or cd != 0


dirs = "GG"
print(find_if_robot_in_circle(dirs))
