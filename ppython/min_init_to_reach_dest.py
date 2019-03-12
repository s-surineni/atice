# Python3 program to find minimum initial 
# points to reach destination 
import math as mt 
R = 3
C = 3
  
def minInitialPoints(points): 
    ''' 
    dp[i][j] represents the minimum initial 
    points player should have so that when  
    starts with cell(i, j) successfully 
    reaches the destination cell(m-1, n-1) 
    '''
    dp = [[0 for x in range(C + 1)]  
             for y in range(R + 1)] 
    m, n = R, C 
      
    if points[m - 1][n - 1] > 0: 
        dp[m - 1][n - 1] = 1
    else: 
        dp[m - 1][n - 1] = abs(points[m - 1][n - 1]) + 1
    ''' 
    Fill last row and last column as base 
    to fill entire table 
    '''
    for i in range (m - 2, -1, -1): 
        dp[i][n - 1] = max(dp[i + 1][n - 1] -
                           points[i][n - 1], 1) 
    for i in range (2, -1, -1): 
        dp[m - 1][i] = max(dp[m - 1][i + 1] -
                           points[m - 1][i], 1) 
    ''' 
    fill the table in bottom-up fashion 
    '''
    for i in range(m - 2, -1, -1): 
        for j in range(n - 2, -1, -1): 
            min_points_on_exit = min(dp[i + 1][j], 
                                     dp[i][j + 1]) 
            dp[i][j] = max(min_points_on_exit -
                               points[i][j], 1) 
              
    return dp[0][0]  
      
# Driver code 
points = [[-2, -3, 3], 
          [-5, -10, 1], 
          [10, 30, -5]] 
  
print("Minimum Initial Points Required:",  
                minInitialPoints(points)) 
  
  
# This code is contributed by  
# Mohit kumar 29 (IIIT gwalior) 
