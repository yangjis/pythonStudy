#리스트
a = ["양지선","조지원","이미숙","허은주",["동방신기","소녀시대","싹쓰리"]]
b = [1,2,3]
c = [4,5,6]

print(a[4][1])
print(b[0]+b[2])
print(b[:2])
print(b*3)

a[0] = "대성아파트"
b[:2] = []
del c[0]
print(a)
print(b)
print(c)

a.append("강남역")
print(a)

d = ["박주하", "잠수", "문재성"]
d.sort()
print(d)

e = [6,5,1,2,3,4]
e.reverse()
print(e)
print(e.index(6))

e.insert(0, 9)
print(e)
e.remove(9)
print(e)

print(e.pop())
print(e)
print(e.count(1))
e.extend([8,5])
print(e)