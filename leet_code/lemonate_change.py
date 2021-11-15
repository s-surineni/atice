def find_lemonade_change(bills):
    notes = {5: 0, 10: 0, 20: 0}
    for val in bills:
        if val == 5:
            notes[5] += 1
        elif val == 10:
            notes[10] += 1
            if notes.get(5):
                notes[5] -= 1
            else:
                return False
        elif val == 20:
            if not notes.get(5):
                return False
            elif notes.get(10):
                notes[10] -= 1
                notes[5] -= 1
            elif notes[5] < 3:
                return False
            else:
                notes[5] -= 3
    return True


# bills = [5, 5, 5, 10, 20]
bills = [5, 5, 5, 5, 20, 20, 5, 5, 20, 5]
print(find_lemonade_change(bills))
