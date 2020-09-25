#함수에 대해 배워보자
def sum(a, b):
    return a+b 

a = sum(3,4)
print(a)


#return값만 있고 파라미터는 없다.
def say():
    return 'HI'

print(say())


#return값은 없고 파라미터는 있다.
def sum2(a,b):
    print("%d, %d의 합은 %d입니다."%(a,b,a+b))

sum2(1, 2)


#return값도 없고 파라미터도 없다.
def say2():
    print('HI2')

say2()


#함수가 몇개의 인자를 받을지 모를경우 *args를 사용
def sum_many(*args):
    sum = 0
    for i in args:
        sum = sum + i
    return sum

print(sum_many(1,2,3,4))

#키워드 파라미터, 딕셔너리 타입을 넣는 함수. 예제가 이상한듯
def print_kwargs(**kwargs):
    for k in kwargs.keys():
        if(k == "name"):
            print("당신의 이름은 :" + k)
            
print_kwargs(name="양지선", b="2")

#함수의 결과값은 언제나 하나이다.
def sum_and_mul(a,b):
    return a+b, a*b

print(sum_and_mul(1, 2))

#매개 변수에 초깃값 미리 설정하기
def say_myself(name, old, man=True):
    print("나의 이름은  %s입니다."%name)
    print("나이는 %d살입니다."%old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")
        
say_myself("강동원", 40)
say_myself("양지선 ", 31,False)
say_myself(old=3, name="조지원", man=False)

#지역변수1
a = 1
def vartest(a):
    a = a + 1
    
vartest(a)
print(a)

#지역변수2
a = 1
def vartest2(a):
    a = a + 1
    return a
a = vartest2(a)
print(a)

#전역변수
a = 1
def vartest3():
    global a    #전역변수 a를 뜻함.
    a = a + 1

vartest3()
print(a)

#함수 Lambda: 익명함수
add = lambda a, b: a+b
print(add(3,4))

def add(a, b):
    return a + b

#list에 람다식 사용
myList = [lambda a, b: a+b, lambda a, b: a*b]
print("람다 myList[0] = %d" %myList[0](1,2))

#내장함수인 input함수를 사용해보
number = input("숫자를 입력하세요: ")
print(number)

#print함수에 대해 공부해보자
print("life""is""too short")
print("life","is","too short") #콤마를 사용하면 뛰어쓰기 되어 출력

for i in range(10):
    print(i, end='hi')
    #print(i, end=' ')
    
#파일 읽고 쓰기, 자바의 스트림
f = open("새파일.text",'w')#w=쓰기모드, r=읽기모드, a=추가모드
f.close()

f = open("c:/PythonCoding/새파일.txt",'w')#절대주소
for i in range(1, 11):
    data = "%d번째 줄입니다.\n"%i
    f.write(data)
f.close()