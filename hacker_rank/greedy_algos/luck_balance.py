# https://www.hackerrank.com/challenges/luck-balance/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=greedy-algorithms
# xx this didn't work for some test cases
def luck_balance(req, contests):
    luck = 0
    for _ in range(req):
        # vals = (filter(contests, lambda val: val[1]))
        # print(vals)
        
        maxi = max((filter(lambda val: val[1], contests)), key=lambda val: val[0])
        luck += maxi[0]
        contests.remove(maxi)
        # print('maxi', maxi)
    # print('contests', contests)
    for val in contests:
        if not val[1]:
            luck += val[0]
        else:
            luck -= val[0]
    return luck

if __name__ == '__main__':
    tot, req = list(map(int, input().split()))
    contests = []
    for _ in range(tot):
        contests.append(list(map(int, input().rstrip().split())))
    result = luck_balance(req, contests)
    print(result)
