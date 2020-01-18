a = 'Hello World!'
print (a)

b = "강한친구 대한육군"
print(b)
print(b)

c = "\\    /\\\n )  ( ')\n(  /  )\n \\(__)|"
print(c)

print("a\tb")  #tap만큼 띄기
print("a\nb")  #1칸 건너띄기
print("a\\b")  #백슬래시 입력방법

d="|\\_/|\n|q p|   /}\n( 0 )\"\"\"\\\n|\"^\"`    |\n||_/=\\\\__|"
print(d)

e = "abc def efg hig"
print(e.split())

f = "abc.def.efg.hig"
print(f.split("."))

g,h = map(int,input().split()) #입력값을 정수로 변환시켜 출력
print(g + h)

g,h = map(float,input().split()) #입력값을 실수로 변환시켜 출력
print(g + h)

i, j = input().split()  #문자로만 연결시켜 출력
print(i + j)
