all_periods = []
for x in period_config:
    # Find the proper range to use
    if x.endswith('-'):
        start, end = x[0:-1], 2050
    elif x.find('-') == -1:
        start, end = x, x
    else:
        start, end = x.split('-')

    # Convert the range to integers
    start, end = int(start), int(end)
    for y in range(start, end + 1):
        all_periods.extend(
            periods_for_year(y, period_config[x], period_type, tzinfo, quarter_adjustments, month_adjustments,
                             starting_quarter))
