import sympy as sp
import math
ABC = 140/2
BAD = 180-ABC
ang = [140, 110, 80, 70]
choice = ["A", "B", "C", "D"]
for i in range(4):
    if BAD==ang[i]:
        print(f"2、{choice[i]}")
        break
C = 13
AC = 4
half = C-AC
res = half*2
l = [26, 24, 20, 18]
for i in range(4):
    if res==l[i]:
        print(f"4、{choice[i]}")
        break
BD = 6
AD = 4
DO = 1/2*BD
AO = math.sqrt(AD**2+DO**2)
AC = 2*AO
l = [8, 9, 10, 12]
for i in range(4):
    if AC==l[i]:
        print(f"5、{choice[i]}")
        break
S = 72
S1 = S/4
S3 = S/4
AD = 12
BC = AD
h1 = 2*S1/AD
h3 = 2*S3/BC
d = AD+h1+h3
l = [18, 20, 24, 28]
for i in range(4):
    if d==l[i]:
        print(f"6、{choice[i]}")
        break
BAC = 40
ACB = 80
ACD = BAC
BCD = ACD+ACB
print(f"7、{BCD}")
AD = 3
BC = AD
print(f"9、{BC}")
C = 8
BC = 5
AB = C-BC
CD = AB
print(f"10、{CD}")
A = (-1, 3)
O = (0, 0)
AO = sp.sqrt((O[0]-A[0])**2+(O[1]-A[1])**2)
AF = AO
F = (A[0]+AF, A[1])
print(f"11、{F}")
a = 2
b = 4
h = a/2+b/2
S = (a+b)*h/2
print(f"12、{S}")
print("16、")
x = sp.Symbol("x")
AC = x
BD = 3*x
AO = CO = sp.Rational(1, 2)*x
BO = DO = sp.Rational(3, 2)*x
AB = 2*sp.sqrt(2)
ex = AB**2+AO**2-BO**2
AC = sp.solve(ex, x)[1]
BC = sp.sqrt(AB**2+AC**2)
print(f"(2){BC}")
