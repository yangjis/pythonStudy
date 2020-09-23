#괄호 안에 데이터를 넣으면 튜플
t1 = (1,2,'a','b')
print(t1[0:2])
print(t1)

t2 = (3,4)
print(t1+t2)
print(t1*3)

a = (1,2)
a = a *3
print(a)

#딕셔너리 자료형: 연관배열 또는 해시, 키를통해 밸류를 얻는다.
dic = {'name': 'Eric', 'age': 15}
print (dic['name'])

print("익명"*2000)

a = {1: 'a'}
a['name'] = "익명"
print(a[1])

del a[1]
print(a)

b ={1: '파랑구름', 2: '이현준', 3: '민MIN준JUN'}
# print(b.keys())
# print(b.values())
# print(b.items())
for k, v in b.items():
    print("키는: " + str(k))
    print("벨류는: " + v)

#b.clear()
print(b.get(4,'없음'))
print(4 in b)



