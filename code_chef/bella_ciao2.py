# https://www.codechef.com/JUNE21C/problems/CHFHEIST


def find_profit(D, d, P, Q):
    n=(D//d)-1;
    ans=d * (P * n + (n * (n+1)/2) * Q  ) + P * d;
    ans+=(D%d) * (P+(n+1)*Q);
    return int(ans)


tc = int(input().strip())
for _ in range(tc):
    inp = [int(i) for i in input().strip().split()]
    print(find_profit(*inp))
