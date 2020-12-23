# class A:
#     def meth_a(self):
#         pass
#     def meth_c(self):
#         pass

# class B:
#     def meth_b(self):
#         pass
#     def meth_c(self):
#         pass

# class C(A, B):
import math
vals = [9, 1, 2, 8, 3, 7]
vals = [1, 2, 3, 9, 8, 7]

def sort_half(vals):
    vals.sort()
    val_len = len(vals)
    half_val = math.ceil(val_len / 2)
    half = vals[:math.ceil(val_len / 2)]

    vals[:half_val] = half[::-1]
    return vals


print(sort_half(vals))
