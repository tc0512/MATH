import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from matplotlib.patches import Circle


import numpy as np
from sympy import Symbol, symbols, solve, factor, simplify, Rational, sqrt, expand, solveset
x, y = symbols("x y")
ex1 = x/(x+y)
x_new = 2*x
y_new = 2*y
ex2 = x_new/(x_new+y_new)
scale = simplify(ex2/ex1)
scales = [2, 4, 1/2, 1]
choice = ["A", "B", "C", "D"]
for i in range(4):
    if scale==scales[i]:
        print(f"3、{choice[i]}")
        break
k = Symbol("k")
eq = x**2-2*x+2*k-(x+2)*(x+k)
sol = solve(eq, k)
val = sol[0]
values = [3, -3, -2, -4]
for i in range(4):
    if val==values[i]:
        print(f"4、{choice[i]}")
        break
S = 8
res = S/2
area = [2, 4, 5, 6]
for i in range(4):
    if res==area[i]:
        print(f"5、{choice[i]}")
        break
AD = 4
CD = 10
AP = AD
AB = CD
BP = AB-AP
OE = 1/2*BP
l = [1, 2, 3, 4]
for i in range(4):
    if OE==l[i]:
        print(f"6、{choice[i]}")
        break
m = Symbol("m")
ex = (2-x)/(x-1)-m/(1-x)+2
sol_x = solve(ex, x)
val_x = sol_x[0]
sol_m = solve(val_x-1, m)
val_m = sol_m[0]
val = [-1, 0, 1, 2]
for i in range(4):
    if val_m==val[i]:
        print(f"7、{choice[i]}")
        break
print(f"10、{factor(4*x-8*x*y)}")
n = Symbol("n")
sol_n = solve(180*(n-2)-720, n)
val_n = sol_n[0]
print(f"11、{val_n}")
ang1 = ang2 = ang3 = ang4 = 75
ang5 = 360-ang1-ang2-ang3-ang4
AED = 180-ang5
print(f"14、{AED}")

print("16、图片生成中...", end="")
chinese_font = FontProperties(fname='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc')
x = [0, 4, 1, 0]
y = [0, 0, 4, 0]
plt.plot(x, y, 'k-', linewidth=2)
plt.text(0, 0, 'A', fontsize=15)
plt.text(1, 4, 'B', fontsize=15)
plt.text(4, 0, 'C', fontsize=15)
circle1 = Circle((1, 4), np.sqrt(17), fill=False, edgecolor='blue', linestyle="-", linewidth=2)
circle2 = Circle((0, 0), 2, fill=False, edgecolor='blue', linestyle="-", linewidth=2)
circle3 = Circle((2, 0), 2, fill=False, edgecolor='blue', linestyle="-", linewidth=2)
plt.gca().add_patch(circle1)
plt.gca().add_patch(circle2)
plt.gca().add_patch(circle3)
plt.plot([1, 1], [4, -2], 'b-', linewidth=2)
circle4 = Circle((0, 0), 1.5, fill=False, edgecolor='blue', linestyle="-", linewidth=2)
circle5 = Circle((1.5, 0), 3, fill=False, edgecolor='blue', linestyle="-", linewidth=2)
circle6 = Circle((3*np.sqrt(17)/34, 6*np.sqrt(17)/17), 3, fill=False, edgecolor='blue', linestyle="-", linewidth=2)
plt.gca().add_patch(circle4)
plt.gca().add_patch(circle5)
plt.gca().add_patch(circle6)
plt.plot([0, 5], [0, 3.9039], 'b-', linewidth=2)
plt.scatter(1, 0.7808, color='blue', s=50)
plt.text(1, 0.7808, 'P', fontsize=15)
plt.xlim(-1, 5)
plt.ylim(-2, 5)
plt.gca().set_aspect('equal', adjustable='box')
plt.title("第16题", fontproperties=chinese_font)
plt.savefig("T16.png")
plt.close()
print("完成")

print("17、")
a, b, x = symbols("a b x")
print(f"(1){factor(a*b**2-25*a)}")
ine1 = (2*x+3>=-5)
ine2 = (x-2<(x+4)/3)
print(f"(2){solve([ine1, ine2], x)}")
ex = (x-2)/(4-x)-2-x/(x-4)
print(f"(3){solve(ex, x)[0]}")

print("18、图片生成中...", end="")
plt.plot([0, 0], [-4, 4], 'k-', linewidth=2)
plt.plot([-4, 4], [0, 0], 'k-', linewidth=2)
plt.text(0, 0, "O(B'')(B')", fontsize=15)
plt.plot([-1, -3, -2, 0, -1], [-1, 0, 2, 1, -1], 'k-', linewidth=2)
plt.text(-1, -1, 'A', fontsize=15)
plt.text(-3, 0, 'B', fontsize=15)
plt.text(-2, 2, 'C', fontsize=15)
plt.text(0, 1, 'D', fontsize=15)
plt.plot([2, 0, 1, 3, 2], [-1, 0, 2, 1, -1], 'gray', linewidth=2)
plt.text(2, -1, "A''(C')", fontsize=15)
plt.text(1, 2, "C''", fontsize=15)
plt.text(3, 1, "D''", fontsize=15)
plt.plot([-1, 0, 2, 1, -1], [-2, 0, -1, -3, -2], 'b-', linewidth=2)
plt.text(-1, -2, "A'(-1, -2)", fontsize=15)
plt.text(1, -3, "D'", fontsize=15)
plt.xlim(-4, 4)
plt.ylim(-4, 4)
plt.grid(True, linestyle="--", alpha=0.7)
plt.gca().set_aspect('equal', adjustable='box')
plt.title("第18题", fontproperties=chinese_font)
plt.savefig("T18.png")
plt.close()
print("完成")

a = sqrt(5)-1
ex = (2+(1-a)/a)/((a**2+2*a+1)/a)
print(f"19、{simplify(ex)}")
print("21、")
k1, b1, k2, b2 = symbols("k1 b1 k2 b2")
x = [1, 2]
f1 = [6000, 10500]
f2 = [4800, 9600]
ex1 = solve([f1[0]-k1*x[0]-b1, f1[1]-k1*x[1]-b1], [k1, b1])
ex2 = solve([f2[0]-k2*x[0]-b2, f2[1]-k2*x[1]-b2], [k2, b2])
x = Symbol("x")
y1 = ex1[k1]*x+ex1[b1]
y2 = ex2[k2]*x+ex2[b2]
print(f"(1)y1={y1}\ny2={y2}")
print(f"(2){str(solve(y1<y2))[:7]}")
print("22、")
a, b = symbols("a b")
print(f"(1)(a+b)**2={expand((a+b)**2)}")
simplify_res = str(expand((a+2*b)*(a+b)))
No2 = simplify_res[-6]
No3 = simplify_res[7]
print(f"(2){No2};{No3}")
print(f"(3){factor(a**2+4*a*b+3*b**2)}")

print("(4)图片生成中...", end="")
plt.plot([0, 5, 5, 0, 0], [0, 0, -4, -4, 0], 'k-', linewidth=2)
plt.plot([2, 2], [0, -4], 'k-', linewidth=2)
plt.plot([3, 3], [0, -4], 'k-', linewidth=2)
plt.plot([4, 4], [0, -4], 'k-', linewidth=2)
plt.plot([0, 5], [-2, -2], 'k-', linewidth=2)
plt.plot([0, 5], [-3, -3], 'k-', linewidth=2)
plt.text(1, -4, "a", fontsize=15)
plt.text(2.5, -4, "b", fontsize=15)
plt.text(3.5, -4, "b", fontsize=15)
plt.text(4.5, -4, "b", fontsize=15)
plt.text(5, -1, "a", fontsize=15)
plt.text(5, -2.5, "b", fontsize=15)
plt.text(5, -3.5, "b", fontsize=15)
plt.text(1, 0.5, "a^2+5ab+6b^2=(a+2b)(a+3b)")
plt.xlim(-1, 6)
plt.ylim(-5, 1)
plt.gca().set_aspect('equal', adjustable='box')
plt.title("第22题第(4)问", fontproperties=chinese_font)
plt.savefig("T22-4.png")
plt.close()
print("完成")

print("24、")
x = Symbol("x")
sol = solve(1800/x-3000/(x+400), x)
A = sol[0]
B = A+400
print(f"(1){A};{B}")
print("25、")
AD = 4*sqrt(3)
AB = 1/2*AD
BD = AB*sqrt(3)
DG = 1/2*BD
BF = AB
S2 = BF*DG/2
AF = BF
AE = AF
AH = AE*1/2
EH = AH*sqrt(3)
BH = EH
BE = BH+EH
S1 = BE*AH/2
print(f"(2){S1};{S2}")
