# https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/seating-arrangement-1/

test_cases = int(input().strip())

for a_tc in range(test_cases):
    seat_no = int(input().strip())
    # print('seat_no', seat_no)
    seat_no_1 = seat_no % 12 or 12
    # print('seat_no_1', seat_no_1)
    seat_quo = seat_no // 12 if seat_no_1 != 12 else (seat_no // 12) - 1
    opp_seat = 13 - seat_no_1
    # print('opp_seat', opp_seat)
    seat_map = {1: 'WS',
                2: 'MS',
                3: 'AS',
                4: 'AS',
                5: 'MS',
                6: 'WS',
                7: 'WS',
                8: 'MS',
                9: 'AS',
                10: 'AS',
                11: 'MS',
                12: 'WS'}

    seat_type = seat_map[opp_seat]
    # if opp_seat < 7:
        # seat_quo -= 1
    opp_seat = (12 * (seat_quo)) + opp_seat
    print(opp_seat, seat_type)
