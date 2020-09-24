#배열에 저장된 단어를 연결해서 출력하라
a = ['Life', 'is', 'too','short'] #배열
result = " ".join(a)
print(result)
#리스트는 [], 배열은 ()

#오늘은 조건제어문을 배워보자
#돈이 있으면 택시를 타고, 돈이 없으면 걸어 간다.
money = True
if money:
    print("택시를 타고 가라")
    print("aaa")#if문은 들여쓰기를 꼭 해야되고 안하면 오류메세지 뜸.
else:
    print("걸어 가라")
    
#비교연산자
a = 1
b = 2
if a < b:
    print("b가 더 크다")
else:
    print("a가 더 크다")
    
#만약 3000원 이상의 돈을 가지고 있으면 택시를 타고 그렇지 않으면 걸어 가라
money = 2000
if money >=3000:
    print("3000원 이상 있다. 택시를 타고 가라")
else:
    print("3000원 없다. 걸어가라")
    
#돈이 3000원 이상 있거나 카드가 있다면 택시를 타고 그렇지 않으면 걸어 가라
money = 2000
card = 1
if money >= 3000 or card:
    print("돈이 삼천원 이상있거나 카드가 한장 있다. 택시를 타고 가라")
else:
    print("돈이 삼천원도 없고 카드도 없다. 걸어가라")


#in은 집합안에 원하는 데이터가 있는지 없는지 검사.
if 1 not in [1,2,3]:
    print("1이 들어있다")
else:
    print("1이 안들어있다")
    
#조건문에서 아무 일도 하지 않게 설정하고 싶다면(in, pass)
pocket = ['paper', 'money','cellphone']
if 'money' in pocket:
    pass
else:
    print("카드를 꺼내라")

#다중조건 판단 elif
pocket = ['paper','cellphone']
card=True
if 'money' in pocket:
    print("다중조건 판단1: 돈이 있다. 택시를 타고가라")
elif card:
    print("다중조건 판단2: 돈은 없지만 카드가 있으면 택시를 타고가라")
else:
    print("돈도 없고 카드도 없다. 걸어가라")
    
    
score = 70
if score >= 60:
    message = "success"
else:
    message = "failure"
print(message)
#위와 아래는 같은 표현. 3항연산자의 파이썬 표현방식
#(조건문이 참인 경우) if (조건문) else (조건문이 거짓인 경우)
message = "success2" if score >= 60 else "failure2"
print(message)


#반복문
#열 번 찍어 안 넘어 가는 나무 없다.
treeHit = 0
while treeHit <= 10:
    treeHit +=1
    print("나무를 %d번 찍었습니다."%treeHit)
    if treeHit == 10:
        print("나무가 넘어갑니다.")
        
#break문
print("----------------------------break문-------------------------")
coffee = 10
money = 300
while money:
    print("돈을 받았으니 커피를 줍니다.")
    coffee = coffee -1
    print("남은 커피의 양은 %d개입니다."%coffee)
    if not coffee:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break#반복문을 빠져나간다.

#continue문
print("-----------------------continue문--------------------------")
a = 0
while a < 10:
    a = a+1
    if a % 2 == 0:
        continue#위로 올라가라 와일문에 맨 처음으로 돌아가라(와일문 조건문까지 돌어간다.)
    print(a)

#무한루푸
#while True:
#    print("안녕하세요")
    
#반복문(for문)
test_list = ['one','two','three']
for i in test_list:
    print(i)
    
print("-------------for문2--------------")
a = [(1,2),(3,4),(5,6)]
for (first, last) in a:
    print(first + last)
    
print("--------------종합판 문제1-----------------")    
#60점이 넘으면 합격이고 그렇지 않으면 불합격
marks = [90, 25, 67, 45, 80]

number =0
for mark in marks:
    number = number+1
    if mark >= 60:
        print("%d번 학생은 합격입니다." %number)    
    else:
        print("%d번 학생은 불합격입니다."%number)

print("--------------종합판 문제2-----------------")
#60점이 넘으면 합격이고 그렇지 않으면 불합격
marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
    number  = number +1
    if mark < 60: continue
    print("%d번 학생 축하합니다. 합격입니다."%number)    
    
    
print("---------------for와 함께 자주 사용하는 range함수------------------")
sum = 0
for i in range(1,11):#1이상이고 11미만
    sum = sum + i
print(sum)

print("---------------이중for문----------------")
for i in range(2,10):
    for j in range(1,10): 
        print(i*j, end=" ")
    print("")

print("-----------for문 리스트 내포1-------------")
a = [1,2,3,4]
result = [num * 3 for num in a]
print(result)

#위의 코드와 같은 뜻 쉬운 표현
#result = []
#for num in a:
#    result.append(num*3)

print("-----------for문 리스트 내포2 짝수일 경우 3을 곱해서 result에 담아주고 출력해라-------------")
result = [num * 3 for num in a if num % 2 == 0]
print(result)



