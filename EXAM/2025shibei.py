import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from matplotlib.patches import Circle

from sympy import*
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

print("第16题图片生成中...", end="")
chinese_font = FontProperties(fname='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc')
x = [0, 4, 1, 0]
y = [0, 0, 4, 0]
plt.plot(x, y, 'k-', linewidth=2)
circle = Circle((1, 4), np.sqrt(17), fill=False, edgecolor='blue', linestyle="-", linewidth=2)
plt.gca.add_patch(circle)
plt.axis('equal')
plt.title("第16题", fontproperties=chinese_font)
plt.savefig("T16.png")
plt.close()
print("完成")
