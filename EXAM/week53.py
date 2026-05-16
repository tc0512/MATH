from sympy import*
x = Symbol("x")
sol = solve(15/x+5-30/(Rational(4, 3)*x), x)
val = sol[0]
res = 4/3*val
price = [1.5, 1.75, 2.0, 2.5]
choice = ["A", "B", "C", "D"]
for i in range(4):
    if res==price[i]:
        print(f"6、{choice[i]}")
        break
sol = solve(2/(x-3)-2, x)
print(f"8、{sol[0]}")
x = 3
a = Symbol("a")
sol = solve(2/(x-a)-3/x, a)
print(f"9、{sol[0]}")
def det2(a, b, c, d):return a*d-b*c
x = Symbol("x")
sol = solve(det2(2, 1, 1/(1-x), 1/(x-1))-1, x)
print(f"11、{sol[0]}")
m = Symbol("m")
sol = solve((2*x+m)/(x-3)-3, x)
domain1 = solve(sol[0]>0)
domain2 = solve(sol[0]-3)
res = str(domain1)[:14]+"!= "+str(domain2[0])+")"
print(f"12、{res}")
print("13、")
print(f"(1)x={solve(1/(x-1)-3/(2*x+1), x)[0]}")
sol = solve(18/(9-x**2)-x/(3-x)-1, x)
print("(2)无解" if sol==[] else f"(2){sol[0]}")
sol = solve(x/(x-4)-3-a/(x-4), x)
domain1 = solve(sol[0]>=2)
domain2 = solve(sol[0]-4)
res = str(domain1)[12:]+" & (a!= "+str(domain2[0])+")"
print(f"14、{res}")
m = solve(1500/(x+100)-1200/x, x)
print(f"15、{m[0]}")
print("16、")
sol = solve(2*6000/x-12800/(x+4), x)
price1, price2 = sol[0], sol[0]+4
print(f"(1)第一批进价{price1}元，第二批进价{price2}元")
total = 6000/price1+12800/price2
y = Symbol("y")
sol = solve((total-50)*y+50*y*Rational(4, 5)-18800-1300>=6000, y)
res = str(sol)[1:3]
print(f"(2){res}")
