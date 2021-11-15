def count_vowels_permutation(char_len, str_len):
    output_vals = [([1] * str_len)[::] for _ in range(char_len)]

    for i in range(str_len):
        output_vals[0][i + 1] = (output_vals[1][i] + output_vals[2][i] +
                                 output_vals[4][i])
        output_vals[1][i + 1] = (output_vals[0][i] + output_vals[2][i])
        output_vals[2][i + 1] = (output_vals[1][i] + output_vals[3][i])
        output_vals[3][i + 1] = (output_vals[2][i])
        output_vals[4][i + 1] = (output_vals[2][i] + output_vals[3][i])
    return [output_vals[i][str_len - 1] for i in range(char_len)]

print(count_vowels_permutation(2, 3))
