# https://www.hackerrank.com/challenges/luck-balance/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=greedy-algorithms
def luck_balance(req, contests):
    luck = 0
    imp = 0
    for val in contests:
        luck += val[0]
        if val[1]:
            imp += 1
    # print('luck', luck)
    for _ in range(imp - req):
        mini =  min((filter(lambda val: val[1], contests)), key=lambda val: val[0])
        # print('mini', mini)
        luck -= (2 * mini[0])
        contests.remove(mini)
    return luck

if __name__ == '__main__':
    tot, req = list(map(int, input().split()))
    contests = []
    for _ in range(tot):
        contests.append(list(map(int, input().rstrip().split())))
    result = luck_balance(req, contests)
    print(result)
