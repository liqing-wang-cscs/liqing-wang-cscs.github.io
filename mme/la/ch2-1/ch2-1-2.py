import sympy as sp

sp.var('k',positive=True, integer=True)
a = sp.Matrix([[0, 1], [1, 1]])
val = a.eigenvals()
vec = a.eigenvects()
P, D = a.diagonalize()
ak = P @ (D ** k) @ (P.inv())
F = ak @ sp.Matrix([1, 1])
s = sp.simplify(F[0])
print(s) 
sm = []
for i in range(20):
    sm.append(int(s.subs(k, i)))
print(sm)