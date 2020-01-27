def parse_input():
    palindrome = input('Please enter a palindrome: ')
    return palindrome


def sort_matrix_diagonally(mat):
    diagonal_idx = [(i, i) for i in range(len(mat))]
    diagonal_values = [mat[i][j] for i, j in diagonal_idx]
    print(diagonal_values)
# palindrome = parse_input()
mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
print(sort_matrix_diagonally(mat))
