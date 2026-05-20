from sympy import*
domain = -1
domains = [-1, 0, 1, 2]
choice = ["A", "B", "C", "D"]
for i in range(4):
    if domain==domains[i]:
        print(f"1、{choice[i]}")
        break
ex = ["1/x", "(m+n)/m", "ab^2/5","(b-c)/(5+a)"]
def has_letter(s: str) -> bool:
    return any(c.isalpha() for c in s)
counter = 0
for i in range(4):
    splited = ex[i].split('/')
    if has_letter(splited[1]):
        counter+=1
count = [2, 3, 4, 5]
for i in range(4):
    if counter==count[i]:
        print(f"2、{choice[i]}")
        break
x = Symbol("x")
ex = [(x**2-1)/x*x/(x**2+1), 1-1/x, (x**2+2*x+1)/(x+1), (x+1)/x/(1/(x-1))]
for i in range(4):
    if simplify(ex[i])==x+1:
        print(f"4、{choice[i]}")
        break
m, n = symbols("m n")
ex = 3*n**2/(m-n)
new_m, new_n = 3*m, 3*n
new_ex = 3*new_n**2/(new_m-new_n)
scale = simplify(new_ex/ex)
scales = [1, 3, 1/3, 9]
for i in range(4):
    if scale==scales[i]:
        print(f"5、{choice[i]}")
        break
y = Symbol("y")
eq = Eq((y-3/(1-x))/(x/(x+1)), (x+1)/(x-1))
sol = solve(eq, y)
ex = [(x-3)/(x-1), (x+3)/(x-1), (x**2-x+1)/(x**2-x), (x**2+5*x+1)/(x**2-x)]
for i in range(4):
    if sol[0]==ex[i]:
        print(f"6、{choice[i]}")
        break
val_m = solve(m**2-3*m+2, m)
res = []
for m in val_m:
    res.append(m/(m**2-m+2))
if res[0]==res[1]:
    value = res[0]
values = [3, 2, Rational(1, 3), Rational(1, 2)]
for i in range(4):
    if value==values[i]:
        print(f"8、{choice[i]}")
        break
a, b = symbols("a b")
print(f"9、{lcm(2*a**2*b, 3*a*b**3)}")
ex = (x**2-16)/(x+4)
print(f"10、{solve(ex, x)[0]}")
print(f"11、{simplify((x**2-4*x)/(x**2-8*x+16))}")
ex = ((a**2-1)/a**2)/(1/a-1)*a
print(f"12、{simplify(ex)}")
v = Symbol("v")
ex = 12/v+12/(Rational(6, 5)*v)-22
print(f"13、{solve(ex, v)[0]}")
print("15、")
ex = ((a-2)/(a**2-1))/(1/(a-1)-1)
print(f"(1){simplify(ex)}")
print(f"(2){solve((2*x-1)/(x-4)+1-(x-1)/(4-x))[0]}")
ex = (1/(1-x))/((x**2+2*x)/(x**2-2*x+1))+1/(x+2)
simplified = simplify(ex)
ine1 = (5-2*x>=1)
ine2 = (x+3>0)
sol1 = solveset(ine1, x, domain=S.Reals)
sol2 = solveset(ine2, x, domain=S.Reals)
sol = sol1 & sol2
min_val = sol.left+1 if sol.left_open else sol.left
max_val = sol.right-1 if sol.right_open else sol.right
available_val = []
for x in range(max_val, min_val-1, -1):
    try:
        val = (1/(1-x))/((x**2+2*x)/(x**2-2*x+1))+1/(x+2)
        available_val.append((x, val))
    except ZeroDivisionError:
        continue
print(f"16、原式={simplified}")
print("求值：")
for i in available_val:
    print(f"x={i[0]}，原式={i[1]}")
x = Symbol("x")
sol_x = solve(x/(x**2-3*x+1)-Rational(1, 5), x)
val_x = sol_x[0]
res = simplify(val_x**2/(val_x**4+val_x**2+1))
print(f"17、{res}")
price = solve(12/x-21/(x+Rational(6, 5)))
num = float(12/price[0])
print(num)
bl = "不对" if int(num)==num else "对"
print("18、")
print(f"(1){bl}")
a, y = symbols("a y")
sol_price = solve(12/y-21/(y+a), y)
num = simplify(12/sol_price[0])
max_denominator = int(str(num)[0])
res = []
for i in range(1, max_denominator+1):
    books = num.subs(a, i)
    val_price = sol_price[0].subs(a, i)
    if float(books)==int(float(books)) and float(val_price)==int(float(val_price)):
        res.append(i)
print(f"(2){res}")
