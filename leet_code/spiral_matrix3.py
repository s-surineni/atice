class Solution:
    def spiralMatrixIII(self, R, C, r0, c0):
        steps = 0
        path = [[r0, c0]]
        ridx, cidx = r0, c0
        # moved = True
        while len(path) < R * C:
            # moved = False
            steps += 1
            #         going right
            for _ in range(steps):
                c0 += 1
                if R > r0 >= 0 <= c0 < C:
                    path.append([r0, c0])
                    # moved = True
                # else:
                #     break
                
#             going down
            for _ in range(steps):
                r0 += 1
                if R > r0 >= 0 <= c0 < C:
                    path.append([r0, c0])
                    # moved = True                    
                # else:
                #     break
            steps += 1

            #         going left
            for _ in range(steps):
                c0 -= 1
                if R > r0 >= 0 <= c0 < C:
                    path.append([r0, c0])
                    # moved = True
                # else:
                #     break
            
#             moving up
            for _ in range(steps):
                r0 -= 1
                if R > r0 >= 0 <= c0 < C:
                    path.append([r0, c0])
                    # moved = True                    
                # else:
                #     break
        return (path)

print(Solution().spiralMatrixIII(2, 1, 1, 0))
