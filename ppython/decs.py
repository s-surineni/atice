import time


def calculate_time(fun):
    begin = time.time_ns()

    def nested(*args, **kwargs):
        res = fun(*args, **kwargs)
        print("*" * 80)
        print("ironman time_taken", time.time_ns() - begin)
        return res

    return nested
