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
