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


a, b = map(int,input().split())
print (a - b)


a, b = map(int,input().split())
print (a * b)


a, b = map(int,input().split())
print (a / b)


A = int(input())
B = int(input())
print(A + B)
print(A - B)
print(A * B)
print(A // B)
print(A % B)


a, b, c = map(int,input().split)
print((a + b) % c)
print((a % c + b % c) % c)
print((a * b) % c)
print((a % c * b % c) % c)


a = int(input())
b = int(input())
print(a*(b%10))
print(a*((b//10)%10))
print(a*(b//100))
print(a*b)


a, b = map(int,input().split())
if(a > b):
    print(">")
elif(a < b):
    print("<")
else:
    print("==")


a = int(input("시험점수 입력 : "))
if (a >= 90 and a <= 100):
    print("A")
elif (a >= 80 and a < 90):
    print("B")
elif (a >= 70 and a < 80):
    print("C")
elif (a >= 60 and a < 70):
    print("D")
else:
    print("F")


a = int(input())
if a % 400 == 0:
    print(1)
elif a % 4 == 0 and a % 100 != 0:
    print(1)
else:
    print(0)


H,M = int(input().split())
if M >= 45 and M <= 60:
    print(H,M-45)
elif M < 45 and H != 0:
    print(H-1,M + 15)
elif M < 45 and H == 0:
    print(23, M + 15)
else:
    print("시간확인")


H,M= map(int, input().split())
if M>= 45:
    M=M-45
else:
    if H>0:
        H=H-1
    else:
        H=H+23
    M=M+15
print(H,M)      # 위와 동일한 다른 입력방법


a, b, c = map(int,input().split())
if a > b and a > c :
    if b > c :
        print(b)
    else:
        print(c)
elif a < b and a < c :
    if b > c :
        print(c)
    else:
        print(b)
else:
    print(a)


N = int(input())
for a in range(1,10):
    print(N,"*",a,"=",N*a)


T = int(input())
for x in range(T):
    A, B = map(int, input().split())
    print(A+B)


n = int(input())
sum = 0
for i in range(1,n+1):
    sum = sum+i
print(sum)


# 파이썬에서 입력을 받을 수 있는 함수로 input함수를 많이 사용하는데,많은 수의 입력을 받을 때는 input함수 대신 sys.stdin.readline()을 사용하면 입출력 시간을 줄일 수 있다.
import sys
for t in range(int(sys.stdin.readline())):
    a, b = map(int, sys.stdin.readline().split())
    print(a + b)

import sys
for N in range(int(sys.stdin.readline())):
	N = N + 1
	print(N)

# 위와 동일한 결과값
n = int(input())
for a in range(1,n+1):
	print(a)
a = a + 1


T = int(input())
for i in range(T):
	a, b = map(int,input().split())
	print('Case #%d: %d' %(i+1, a + b))
# 변수를 문자열과 함께 출력할 때는 연결 방식을 사용. 이때 %를 사용. %f  실수(float), %d  정수(interger), %s  문자열(string)
# 예시  name = "Amy"  \n   print "Hello %s" %(name) => 결과  Hello Amy
# 예시2 S_1 ="drink"  \n  s_2 ="bar"  \n  print "Let's go %s. Tell me when you find a %s" %(S_1, S_2)  => 결과  Let's go drink. Tell me when you find a bar


T = int(input())
for x in range(T):
	a, b = map(int, input().split())
	print("Case #%d: %d + %d = %d" %(x+1,a,b,a+b))
# 들여쓰기는 위의 명령어와 연장되어 실행됨. 들여쓰기를 잘 확인해야 함


N = int(input())
for i in range(N+1):
	print("*"*i)

N = int(input())
for i in range(N):
	print("*"*(i+1))
# 위와 아래는 결과값이 동일하다.


N = int(input())
for i in range(N):
	print(" "*(N-i-1)+"*"*(i+1))
# 출력물을 연결할때는 +를 사용하면 된다.

N, X = map(int,input().split())
A = list(map(int,input().split()))
for i in range(N):
	 if A[i] < X:
		 print(A[i],"", end="")
# 출력물에 공백 넣을때는 "" 또는 '' 또는 "필요 공백칸" 한줄에 출력물 표기할때는 end =''


while True:   # while True 와 while(1)은 동일
	a, b = map(int, input(). split())
	if(a==0 and b==0):
		break
	else:
		print(a+b)
# while문의 경우 반드시 조건이 들어가야 함. 무한반복을 위해서는 항상 참이되는 1을 넣음


import sys

while True:
	try:
		a,b=map(int,sys.stdin.readline().split())
	except:
		break
	print(a+b)



#0보다 크거나 같고, 99보다 작거나 같은 정수가 주어질 때 다음과 같은 연산을 할 수 있다. 먼저 주어진 수가 10보다 작다면 앞에 0을 붙여 두 자리 수로 만들고, 각 자리의 숫자를 더한다. 그 다음, 주어진 수의 가장 오른쪽 자리 수와 앞에서 구한 합의 가장 오른쪽 자리 수를 이어 붙이면 새로운 수를 만들 수 있다.
# 다음 예를 보자. 26부터 시작한다. 2+6 = 8이다. 새로운 수는 68이다. 6+8 = 14이다. 새로운 수는 84이다. 8+4 = 12이다. 새로운 수는 42이다. 4+2 = 6이다. 새로운 수는 26이다.
# 위의 예는 4번만에 원래 수로 돌아올 수 있다. 따라서 26의 사이클의 길이는 4이다. N이 주어졌을 때, N의 사이클의 길이를 구하는 프로그램을 작성하시오.

N = A = int(input())
count = 0
while True:
	ten = N // 10
	one = N % 10
	total = ten + one
	count = count + 1
	N = int(str(N % 10)+str(total % 10))
	if(A == N):
		break
print(count)

N = X = int(input())
count = 0
while True:
    N = int(str(N % 10) + str((N // 10 + N % 10) % 10))
    count += 1
    if N == X:
        break
print(count)
# 위, 아래 동일


a = int(input())
b = list(map(int,input().split()))
print('{} {}'.format(min(b),max(b)))   # print(min(b),max(b))도 문제 없음.
# '{} {}'.format() : {} 대괄호 안에 아무 숫자도 입력하지 않으면, format 안에 들어있는 값들이 처음부터 차례대로 출력.
# {}안에 숫자를 넣으면 format 안에 입력된 순서에 따라 입력값을 불러온다. print('{1}'.format(min(b),max(b))) => max(b)값. 마찬가지로 0부터 순서
# 리스트형 [], 튜플형 () : 리스트는 변경이 가능(가변적) 하고, 튜플은 변경이 불가능(불변적). 문자열도 튜플처럼 변경이 불가능한 자료형
# 튜플 사용 이유: 데이터 할당할 공간의 내용과 크기가 변화없어 생성이 간단. 데이터가 오염되지 않을 것이라는 보장. 효율적인 데이터 공간. 위도 경도 좌표 RGB색상 등 작고 고정된 값 나타내기 편리. 딕셔너리 자료형의 키값에 사용 가능


a = []
for i in range(9):
    a.append(int(input()))
print(max(a))
print(a.index(max(a))+1)
# 리스트명.append(넣고싶은 값) 을 해주면 리스트의 맨 뒤에 괄호안에 썼던 값이 추가
# 리스트명.insert(인덱스(순서), 넣고싶은 값)을 해주면 리스트에서 입력한 index에 넣고 싶은 값이 추가
# index를 사용하면 원하는 요소가 리스트의 몇번째에 위치하고 있는지 알 수 있음. 단, 시작이 0부터 임을 유의
# a리스트에서 n번째 요소 출력하기 : print(a[n-1])    print(a[1],a[2]) : 요소출력별로 구분


# 리스트 슬라이싱
number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(number[1:3])  # 이상~미만
print(number[3:])  # 이상
print(number[:3])  # 미만
print(number[1:3:2])  # 1이상 3미만 2개씩
print(number[0:9:2])  # 0이상 9미만 2개씩
print(number[::-1])  # 거꾸로
print(number[]::2]) # 처음부터 끝까지 두 칸 간격으로
print(number[]::-2]) # 처음부터 끝까지 역순 두 칸 간격으로


a = int(input())
b = int(input())
c = int(input())
d = a*b*c
e = list(str(d)) #값을 문자화하여 리스트
for i in range(0,10): #10미만. 이외의 표현으로 길이지정. range(10)
    print(e.count(str(i))) #리스트가 문자이기 때문에, i 값을 넣은 것도 문자로 변환시켜야 매칭이 가능.

a= []   # a = list()
for i in range(10):
    b = int(input())
    a.append(b % 42)
a = set(a)
print(len(a))
# set은 집합자료형으로 1)순서를 가지지 않으며, 2)중복을 허용하지 않는다. 3)인덱싱이 되지 않는다.


N = int(input())
score = list(map(int,input().split()))
M = max(score)
Sum = 0
for i in range(N):
    Sum = Sum + (score[i]/M)*100
print(Sum/N) # 소수점 2째자리까지 표시할때는 print("%.2f" %(Sum/N))


N = int(input())
for i in range(N):
    a= input()
    ts = 0
    os = 0
    for j in range(len(a)):
        if a[j] == 'O':
            os += 1
            ts += os
        elif a[j] == 'X':
            os = 0
            ts += 0
    print(ts)
# 백준 8958번


C = int(input())
for i in range(C):
    l = list(map(int,input().split()))
    avg = float(sum(l[1:])/float(l[0]))
    count = 0
    for j in l[1:]:
        if j > avg:
            count += 1
    print('%.3f%%' % round(float((count/l[0])*100),3))
# 나눗셈 연산자를 사용한 결과값을 정수가 아닌 소수점까지 적용하기 위해서는 A/B가 아니라 float(A)/float(B)

def solve(a):  #배열 a를 함수를 통해서 전달받고
    return sum(a)  #모든 배열의 원소를 함수 sum을 통해서 더하면된다.


def self(n):  #self라는 함수 생성
    total = n
    for i in range(0, len(str(n))): #0에서 n이라는 문자열의 길이까지 - 예 12면 2, 415면 3
        total += int(n/10**i)%10 #n을 10의 i승으로 나눈 값의 1의 자리만 얻어서 total에 합산
    return total
A = []
for i in range(10000):
    A.append(self(i))
for i in range(10000):
    if i not in A:
        print(i)
# 셀프 넘버는 1949년 인도 수학자 D.R. Kaprekar가 이름 붙였다. 양의 정수 n에 대해서 d(n)을 n과 n의 각 자리수를 더하는 함수라고 정의하자. 예를 들어, d(75) = 75+7+5 = 87이다.
# 양의 정수 n이 주어졌을 때, 이 수를 시작해서 n, d(n), d(d(n)), d(d(d(n))), ...과 같은 무한 수열을 만들 수 있다.
# 예를 들어, 33으로 시작한다면 다음 수는 33 + 3 + 3 = 39이고, 그 다음 수는 39 + 3 + 9 = 51, 다음 수는 51 + 5 + 1 = 57이다. 이런식으로 다음과 같은 수열을 만들 수 있다.
# 33, 39, 51, 57, 69, 84, 96, 111, 114, 120, 123, 129, 141, ...
# n을 d(n)의 생성자라고 한다. 위의 수열에서 33은 39의 생성자이고, 39는 51의 생성자, 51은 57의 생성자이다. 생성자가 한 개보다 많은 경우도 있다. 예를 들어, 101은 생성자가 2개(91과 100) 있다.
# 생성자가 없는 숫자를 셀프 넘버라고 한다. 100보다 작은 셀프 넘버는 총 13개가 있다. 1, 3, 5, 7, 9, 20, 31, 42, 53, 64, 75, 86, 97
# 10000보다 작거나 같은 셀프 넘버를 한 줄에 하나씩 출력하는 프로그램을 작성하시오.


def A(x):
    N2 = x // 100  # 100의 자리의 수 결정
    N1 = (x % 100) // 10  # 10의 자리의 수 결정
    N0 = x % 10 # 1의 자리의 수 결정
    if N2 - N1 == N1 - N0: # 등차여부 확인
        return 1
    else:
        return 0
x = int(input())
count = 0
if x > 99: # 100보다 크면, 세자리 수이기 때문에 함수 A(x) 적용
    for i in range(100,x+1):
        if A(i) == 1:
            count += 1
    print(count + 99) # 100보다 작은 수는 등차이기때문에 합산
else:
    print(x)


n = ord(input())
print(n)
#ord(c)는 파라미터c의 유니코드 int 값을 return해 줍니다. 반대로 int값을 character로 변환할 때는 chr(i)함수를 씁니다. chr(i)는 아스키코드 i와 대응하는 문자열(len=1)을 return해 줍니다.


n = int(input())
a = input()
sum = 0
for i in range(n):
    sum += int(a[i])
print(sum)

n = int(input())
a = input()
sum = 0
for i in a:
    sum += int(i)
print(sum)
# 상위식 개선1

def acc(x, y):
    return int(x) + int(y)
from functools import reduce
n = int(input())
num = input()
sum = reduce(acc, num)
print(sum)
# 상위식 개선2

from functools import reduce
n = int(input())
num = input()
sum = reduce(lambda x, y: int(x) + int(y), num)
print(sum)
# 상위식 개선3

# string 모듈
# import string
# string.ascii_lowercase # 소문자 abcdefghijklmnopqrstuvwxyz
# string.ascii_uppercase # 대문자 ABCDEFGHIJKLMNOPQRSTUVWXYZ
# string.ascii_letters #대소문자 모두 abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
# string.digits # 숫자 0123456789

import string
n = input()
a = list(string.ascii_lowercase)
for i in a:
    print(n.find(i), end=" ")

# 상위식 개선
import string
n = input()
a = list(string.ascii_lowercase)
b = list(map(lambda x: print(n.find(x), end=" "), a))
# 게으른 실행의 개념을 알아야 이해할 수 있음


T = int(input())
for j in range(T):
    a, b = input().split()
    a = int(a)
    for i in b:
        print(i*a, end ="")
    print()
# 테스트 갯수가 있고, 한줄로 출력이 될 경우에는 공백을 입력하기 위해 print()를 입력


import string
w = input()
W = w.upper()
l = list(string.ascii_uppercase)
b = list(map(lambda x: W.count(x), l))
c = b.index(max(b))
if b.count(c) == 1:
    d = l[c]
    print(d)
else:
    print("?")
# 위 문제를 dic으로 풀려면 어떻게 해야 하는가??


X = input().upper() #대문자로 통일해서 받음
l = [i for i in range(0,26)] #길이가 26인 리스트 생성
for i in range(0,26):
    l[i] = X.count(chr(i+65)) #X의 A-Z가 몇개인지 센다.
M = max(l) #C리스트의 가장 큰 숫자
if l.count(M) >= 2: #가장 큰 숫자가 2개 이상이면
    print('?') #? 출력
else: #가장 큰 숫자가 1개라면 C리스트에 있는 큰 수의 인덱스를 찾아 65를 더하고 대문자로 만듦
    print(chr(l.index(M)+65))
# 배열의 초기화 - 배열을 0으로 100개 초기화: l = [0]*100  / 임의의 아이템 e를 n번 나타내려면 l = [e] * n / 0~99까지 넣어 초기화 l = [i for i in range(0,100)]


a=input().split()
print(len(a))

a = list(map(str,input().split()))
print(len(a))
# 위 아래 동일


a = input()[::-1].split() # [::-1] 입력을 역순으로 저장
print(max(a))


a = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'  #1
b = '2223334445556667778889999'
sum = 0
for i in input():
    sum += int(b[a.index(i)])+1
print(sum)

W = input().lower()  #2
l = ['abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
sum = 0
for i in range(len(W)):
    for j in l:
        if W[i] in j:
            sum += l.index(j) + 3
print(sum)

print(sum(min(ord(c)-64,25)*28//89+3 for c in input()))  #3
# 1,2,3은 동일...


x = input()
a = ['c=','c-','dz=','d-','lj','nj','s=','z=']
for i in a:
    x = x.replace(i,'a')
print(len(x))


a = int(input())
l = []
for i in range(a):
    w = list(str(input()))

    for k in range(len(w)):
        if k != len(w) - 1 and w[k] == w[k + 1]:
            pass
        elif w[k + 1:].count(w[k]) != 0:
            break
        elif k == len(w) - 1:
            l.append(i)
print(len(l))


# 파보나치 수열 역순일때 재귀함수를 쓴다.
def fibo(n):
    if n==1 or n==2:
        return 1
    return fibo(n-1)+fibo(n-2)



# 숙제


# T개의 원소를 가진 리스트와 특정값 N이 1항에 입력
# 리스트의 원소를 입력
# 리스트 원소 중 N으로 나누어 떨어지지 않는 수를 출력하라

T, N = map(int,input().split())
A = list(map(int,input().split()))
for i in A:
    if i % N == 0:
        pass
    else:
        print(i,"",end="")


# 리스트 원소 개수 입력
# 리스트 입력
# 가장 많이 등장하는 수 출력

from collections import Counter
X = int(input())
l = list(map(int,input().split()))
c = Counter(l)
print(c.most_common(1))
# 답에서 빈도수 빼고 최빈값만 노출하는 방법?

import numpy as np
X = int(input())
l = list(map(int,input().split()))
a = np.bincount(l)
print(a)


# 숫자 개수 입력
# 숫자 개수만큼의 원소 입력
# 최대값, 최소값, 최소값이 나중에 오면 True, 최대값이 나중에 오면 false 출력

x = int(input())
l = list(map(int,input().split()))
M = int(l.index(max(l))) - int(l.index(min(l)))
if M < 0:
    print('true')
else:
    print('false')


# 숫자 개수 입력
# 숫자 개수만큼의 원소 입력
# 붙어있는 숫자의 차이를 출력(절대값)

x = int(input())
l = list(map(int,input().split()))
A = []
for i in range(x-1): # 원소개수의 차이기 때문에 원소의 갯수가 1개 줄어든다!
    A.append(abs(l[i+1]-l[i]))
print(A)

# 함수를 정의
# n을 입력 시 [0~n-1) 출력

n = int(input())
def my_range(n):
    l = []
    while n > 0:
        l.append(n-1)
        n -= 1
    return l[::-1]  #l.reverse()와 동일
print(my_range(n))

n = int(input())
def my_range(n):
    l = []
    while n > 0:
        l.append(n-1)
        n -= 1
    l.reverse()
    return l
print(my_range(n))
# 위 아래 동일. l.reverse()가 while안에 들어가면 다른 결과. 확인해볼 것

week_dict = dict()
week_dict['Mon'] = '맑음'
week_dict['Tue'] = '구름'
week_dict['Wed'] = '비'
print(week_dict)
weather = week_dict['Wed']
print(weather)
# dict 기초

