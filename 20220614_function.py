#예약어X
#snake_case
# sum = 0
# def sum(x) :내장 함수와 이름이 같으면 에러는 안나지만, 내장 함수를 호출 하지 못한다.
# print(x)
#sum =0
a = sum([10,20,3])
print(a)
print('-'*20)
'''
Java
접근 제어자 반환형 함수 이름(파라미터1, 파라미터2){
}

C
접근 제어자 반환형 함수 이름(파라미터1, 파라미터2){
}

python
def 함수명(파라미터1, 파라미터2):
    return
'''

def my_print(age):
    print('조예서 : '+str(age)+'살 입니다.')
    print('조예서 : ', age, '살 입니다.')
    print(f'조예서 : {age}살 입니다.')
print('-' * 20)
def my_print2(name,age):
    print(name+' : '+str(age)+'살 입니다.')
    print(name,':', age, '살 입니다.')
    print(f'{name} : {age}살 입니다.')

def my_print3(name,age, group):
    print(name+' : '+str(age)+'살 입니다.'+group+'소속입니다.')
    print(name,':', age, '살 입니다.', group, '소속입니다.')
    print(f'{name} : {age}살 입니다.{group}소속입니다.')

print(my_print(18))   #my_print() 실행, my_print()의 리턴 값 출력
print(my_print2('안유진', 20))   #my_print() 실행, my_print()의 리턴 값 출력
my_print3(age=20, name='안유진',group='아이브')
#my_print3(age=20, name='안유진','아이브') #SyntaxError: unterminated string literal
#my_print3('안유진',age = 20,'아이브')#위치 인자 뒤에는 계속 키워드 인자 해야함
#print(my_print2(20, '안유진'))
print(my_print2(age=20, name='안유진'))    #아규먼트 순서와 관계 없이 파라미터의 이름을 쓰면 거기에 들어감
my_print3( '안유진',age=20, group='아이브')
print('-' * 20)


def my_print4(name,age, group='아이브 '): #기본값있는 파라미터
    print(name+' : '+str(age)+'살 입니다.'+group+'소속입니다.')
    print(name,':', age, '살 입니다.', group, '소속입니다.')
    print(f'{name} : {age}살 입니다.{group}소속입니다.')
my_print3( '안유진',age=20, group='아이브')
print('-' * 20)

#가변 임자
def my_print5(*args):
    print('정보 : ')
    print(args)


my_print5('안유진', 20, '아이브' , '러브 다이브')
print('-'*10)

#가변 임자
def my_print6(name,*args):
    print('정보 : ')
    print(args)

my_print5('안유진', 20, '아이브 ', '러브 다이브 ')
# def my_print7(name, age=10, group):
#     print(name + ' : ' + str(age) + '살 입니다.' + group + '소속입니다.')
#     print(name, ':', age, '살 입니다.', group, '소속입니다.')
#     print(f'{name} : {age}살 입니다.{group}소속입니다.')
#
# my_print7('안유진', 20, '아이브 ', '러브 다이브 ')

print('-'*10)

def say(name, msg='안녕하세요', feeling='🍳🍳'):
    print(f'{name}, {msg} {feeling}')
say('가현')
say('가현', feeling="😴")

print('-'*20)
def fn(a, b=[]):
    b.append(a)
    print(b)
fn(3)
fn(5)
fn(10, [1])
print('-'*20)
say('현진', '미안해')

def plus20(age):
    return age+2
a = plus20(20)
print(a) #one:

print('-'*20)
def tel(number):
    index = number.find('-')
    f= number[:index]
    b= number[-4:]
    return f, b #(f, b)인 튜플을 보내는 것이다
# front = '0101'
# back = '5678'
front, back = tel('010-1234-5678')
print(f'앞 : {front}\t뒤 : {back}')
print('-'*20)
#
# def min_max(리스트):
#     minV = 리스트[0]
#     for n in range(1,6):
#         if(minV>리스트[n]):
#             minV = 리스트[n]
#     maxV = 리스트[0]
#     for n in range(1,6):
#         if (maxV < 리스트[n]):
#             maxV = 리스트[n]
#     return minV, maxV

def min_max(*리스트):      #기변인자로 튜플로 들어 온다
    minV = 리스트[0]
    maxV = 리스트[0]
    for n in 리스트[1:]:
        if minV>n:
            minV = n
        elif maxV < n:
            maxV = n
    return minV, maxV
#min_max([3, 31, 1, 6, 5, -6])
# def min_max(리스트):
#     minV =min(리스트)
#     maxV=max(리스트)
#     return minV, maxV
min_value, max_value = min_max(3, 31, 1, 6, 5, -6)
print(f'{min_value}, {max_value}')

#count, sum, min, max 알아야 함