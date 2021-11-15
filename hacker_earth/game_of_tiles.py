'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

tc = int(input())

def find_max_score_dp(all_tiles, tile_no, res, memw):
    if tile_no >= len(all_tiles):
        return res
    # if tile_no in memw:
    #     print('in memw')
    #     return memw[tile_no]
    for idx in range(3): # 3 is length of tiles
        # res1 = res + all_tiles[tile_no][idx] + find_max_score_dp(all_tiles, tile_no + idx + 1, res + all_tiles[tile_no][idx], memw)
        res1 = find_max_score_dp(all_tiles, tile_no + idx + 1, res + all_tiles[tile_no][idx], memw)
        res2 = find_max_score_dp(all_tiles, tile_no + idx + 2, res + all_tiles[tile_no][idx + 1], memw)
        res3 = find_max_score_dp(all_tiles, tile_no + idx + 3, res + all_tiles[tile_no][idx + 2], memw)
        # memw[tile_no] = max(res1, res2, res3)
        return max(res1, res2, res3)
        
        
def find_max_score():
    num_tiles = int(input())
    all_tiles = []
    for j in range(num_tiles):
        all_tiles.append([int(i) for i in input().split()])
    
    return find_max_score_dp(all_tiles, 0, 0, {})

for _ in range(tc):
    print(find_max_score())
