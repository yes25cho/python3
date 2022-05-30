"""
조건식 : true 또는 False로 결전되는 문장
파이썬에서 if문 작성시 유의 해야 할 사항 - 콜론, 들어쓰기
"""

# if True:
# print("실행")     #IndentationError: expected an indented block after 'if' statement on line 6
if True:
    print("실행")

# 교통수단 결정 문제
money = 15000
if money >= 10000:
    print("택시를 타라")
else:
    print("버스를 타라")

# input
x = input()
print(x, type(x))
num = int(input())
print(num, type(num))

# 교통수단 결정 문제+input 함수..
money = int(input('잔고를 입력 하세요 : '))
if money >= 10000:
    print("택시를 타라")
else:
    print("버스를 타라")

# 문제 1
num = int(input('정수 입력 : '))
if num % 2 == 0:
    print("짝수")
else:
    print("홀수")

# 문제 2
password = input('암호 입력 : ')
if password == '미림과학고':
    print('암호이다')
else:
    print('암호가 아니다')

