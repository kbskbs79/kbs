company = {}
company["삼성전자"] = (100, 10, 5)
company["SK하이닉스"] = (50, 5, 3)
company["셀트리온"] = (30, 7, 10)
company["LG화학"] = (15, 8, 3)
company["포스코"] = (60, 3, 5)

print(company["삼성전자"])

print(company.keys())

print(company.items())

# keys = company.keys()
# for key in keys:
#    print(key)
#    print(company[key])

# for k, v in company.items():
#    print(k)
#    print(v)

b = company.copy()

for D, E in b.items():
    print(D)
    print(E)

n = 10
while n > 0:
    print(n)
    n -= 1   # n = n-1

    # while, for, if, comtinue, break 함수 학습

True and True
True and False
False and True
False and False
True or True
True or False
False or True
False or False

a=1
b=3

print(a==1 and b==2)
print(a==2 and b==2)
print(a==1 and b==3)
print(a==1 or b==2)
print(a==2 or b==2)
print(a==1 or b==3)