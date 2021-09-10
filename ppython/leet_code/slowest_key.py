# https://leetcode.com/problems/slowest-key/
def find_slowest_key(rel_time, key_pressed):
    max_time, max_key = rel_time[0], [key_pressed[0]]
    for idx, time in enumerate(rel_time[1:], 1):
        curr_time = time - rel_time[idx - 1]
        if curr_time == max_time:
            max_key.append(key_pressed[idx])
        elif curr_time > max_time:
            max_time = curr_time
            max_key = [key_pressed[idx]]
    return sorted(max_key)[-1]


# releaseTimes = [9, 29, 49, 50]
# keysPressed = "cbcd"

# releaseTimes = [12,23,36,46,62]
# keysPressed = "spuda"

releaseTimes = [28, 65, 97]
keysPressed = "gaf"

print(find_slowest_key(releaseTimes, keysPressed))
