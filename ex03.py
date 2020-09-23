#합집합,차집합,교집합, bool, 변수




#set으로 데이터 저장(집합과 같음.)
s1 = set([1,2,3])
s2 = {1,2,3}
print(type(s1))
print(type(s2))

#list로 데이터 저장
l = [1,2,2,3,4]
print(l)
#list의 값에 중복을 제거하고자 set으로 감쌈.
newList = list(set(l))
print(newList)

s3 = set("Hello")
print(s3)

#공통된 부분만 출력하기.
s4 = set([1,2,3,4,5,6])
s5 = set([4,5,6,7,8,9])
print(s4 & s5)
print(s4.intersection(s5))

#합집합: 집합은 순서가 없다
s6 = set([1,2,3,4,5,6])
s7 = set([4,5,6,7,8,9])
print(s6 | s7)
print(s6.union(s7))
#차집합:집합은 순서가 없다
print(s6-s7)
print(s6.difference(s7))

#집합에 데이터 추가
s7.add(1)
print(s7)

#집합에 여러 데이터를 추가
s6.update([7,8,9])
print(s6)

#집합에 원소 삭제하기
s6.remove(9)
print(s6)

#자료형 bool
a = True
if a:
    print(type(a))


b = [1,2,3,4]
while b:
    b.pop()
    print(b)


