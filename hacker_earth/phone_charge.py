import math


range_rates = ((0, 10, 10),
               (11, 230, 5),
               (231, 559, 8),
               (560, 1009, 2),
               (1010, 5000, 7),
               (5001, 10000, 8),
               (10001, 10 ** 9, 3),
)
def chargingSmartPhone (initCharge, finalCharge):
    time_taken = 0
    curr_time_taken = 0
    while initCharge < finalCharge:
        for idx, val in enumerate(range_rates):
            if val[0] <= initCharge <= val[1]:
                rate = val[2]
                if finalCharge <= val[1]:
                    curr_time_taken = math.ceil((finalCharge - initCharge) / rate)
                    initCharge = finalCharge
                else:
                    curr_time_taken += math.ceil((val[1] - initCharge) / rate) + 1
                    initCharge += (curr_time_taken * rate)
                time_taken += curr_time_taken   

    return time_taken


print(chargingSmartPhone(0, 5))
# print(chargingSmartPhone(10, 50))
