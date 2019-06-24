from sympy import *
from sympy.vector import Vector

a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, v = symbols("a b c d e f g h i j k l m n o p v")
symlist = [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, v]

Ck_prev = Matrix(
    [[a, b, c, d, e],
     [b, f, g, h, i],
     [c, g, j, k, l],
     [d, h, k, m, n],
     [e, i, l, n, o]]
)

H = Matrix([[1], [p], [0], [0], [0]])

A = Ck_prev * H * H.T * Ck_prev
div = v + (H.T * Ck_prev * H)[0,0]
Ck = Ck_prev - A/div

# print(det(Ck_prev))
print(det(Ck))
