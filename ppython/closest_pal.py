t = int(input())
while t:
    n = input()
    print('n', n)
    if n == n[::-1]:
        print(n)
        t-=1
        continue
    if len(n)%2==0:
        s = n[:len(n)//2]
    else:
        s = n[:(len(n)//2)+1]
    print('s', s)
    p = str(int(s)+1)
    q = str(int(s)-1)
    print('p, q', p, q)
    if(len(n)%2!=0):
        r = s+s[::-1][1:]
        p = p+p[::-1][1:]
        q = q+q[::-1][1:]
    else:
        r = s+s[::-1]
        p = p+p[::-1]
        q = q+q[::-1]
    print('r, p, q', r, p, q)
    d1 = abs(int(n)-int(p))
    d2 = abs(int(n)-int(q))
    d3 = abs(int(n)-int(r))
    if(d1<d2):
        if(d1<d3):
            print(p)
        elif(d1==d3):
            print(p if p<r else r)
        else:
            print(r)
    else:
        if(d2<d3):
            print(q)
        elif(d2 == d3):
            print(q if q<r else q)
        else:
            print(r)
    t-=1
