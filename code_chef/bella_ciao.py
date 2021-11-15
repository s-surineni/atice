# https://www.codechef.com/JUNE21C/problems/CHFHEIST


def find_profit(dur, inter, initial, rate):
    num_of_intervals_completed = dur // inter
    num_of_times_rate_increased = num_of_intervals_completed - 1    # j

    amount_contributed_by_init_amount = num_of_intervals_completed * initial # 3 * p
    # rate_multiplier = (num_of_times_rate_increased * (num_of_times_rate_increased + 1)) / 2
    rate_multiplier = (num_of_intervals_completed * (num_of_intervals_completed - 1)) / 2
    rate_contri = rate * rate_multiplier
    form_contri = inter * (rate_contri + amount_contributed_by_init_amount)
    rest_days = dur % inter
    # final_rate = (num_of_times_rate_increased + 1) * rate
    final_rate = num_of_intervals_completed * rate
    rest_days_contri = (final_rate + initial) * rest_days
    total_contri = (form_contri + rest_days_contri)
    return int(total_contri)

tc = int(input().strip())
for _ in range(tc):
    inp = [int(i) for i in input().strip().split()]
    print(find_profit(*inp))
