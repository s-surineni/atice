def act_gen(n):
    for val in range(n):
        yield val

def gen2(n):
    return act_gen(n)

def gen1(n):
    return gen2(n)

print('gen1')
for v in gen1(10):
    print(v)

print('gen2')
for k in gen2(10):
    print(k)


print('act_gen')
for k in act_gen(10):
    print(k)
