def func_cache(func):
    res_store = {}
    def enclosed(ip):
        if res_store.get(ip):
            return res_store[ip]
        res = func(ip)
        res_store[ip] = res
        return res
    return enclosed


def arg_count(arg_count):
    def func_cache(func):
        res_store = {}
        def enclosed(*args):
            key = tuple(args)
            # for ar in args:
            #     key += (ar, )
            if res_store.get(key):
                return res_store[key]
            res = func(*args)
            res_store[key] = res
            return res
        return enclosed
    return func_cache
