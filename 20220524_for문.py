#문자열
for ch in "SORI":
    print(ch,end=' ')

#리스트
for item in ['힙합', '발라드']:
    print(item)

#튜플
for item in (2929, 39393):
    print(item)

#셋
for item in{"wsm", "java", "Python"}:
    print(item)
#딕션너리
pl = {'c':1972, 'java':1995, 'Python':1991}
for item in pl:
    print(item)
for key in pl.keys():
    print(key)
for val in pl.values():
    print(val)
for ite in pl.items():
    print(ite)

#문제1
num_list = [-5, 127, -13, 9, -21, 100]
for num in num_list:
    if num>0:
        print(num,end=' ')

#문제2
num_list = [13, 8, 7, 55, 10, 2, 12, 10, 17]
for num in num_list:
    if num % 2 ==0:
        print('{}은 짝수이다.'.format(num))
    else:
        print('{}은 홀수이다.'.format(num))

print('------------------------------------------')
holzzak = ['홀수', '짝수']
for num in num_list:
    print(holzzak[num%2])

#자리수
for num in num_list:
    print('{}은 {}자리수이다.'.format(num,len(str(num))))


sev = {'정한':100, '준':50, '호시':85, '우지':75, '디노':25, '가현':60}
for mem, sco in sev.items():
    if sco>=60:
        print(f'{mem}(는/은) 합격이다.')
    else:
        print(f'{mem}(는/은) 불합격이다.')

#range함수
print(list(range(0, 10, 1)))
print(list(range(10, 0, -1)))
#print(reversed(list(range(0, 10))))
print(list(range(0, 10, 5)))
print(list(range(0, 10)))
print(list(range(10)))

#for i in range(1, 11, 1):

# 리스트
nctdream = ['런쥔', '제노', '해찬', '마크', '재민', '지성', '천러']
for member in nctdream:
    print(member)
print('--------------------------------')
for i in range(0, len(nctdream)):
    print(i+1, nctdream[i])
print('--------------------------------')
for i,member in enumerate(nctdream):
    print(i+1, member)

# 문제
sumV = 0
for i in range(1, 201):
    if i % 3 == 0:
        sumV += i
print(sumV)


sumV = 0
for i in range(0, 201, 3):
    sumV += i
print(sumV)

sumV = 0
for i in range(500, 1001):
    if i % 5 == 0:
        sumV += i
print(sumV)

sumV = 0
for i in range(500, 1001, 5):
    if i % 5 == 0:
        sumV += i
print(sumV)

# sum()함수,max,min,avg(sum(l)/len(l))
l = [1, 2, 3, 4, 5]
print(sum(l))
print(max(l))
print(min(l))
print(sum(l)/len(l))
#변수이름 조심 해야함 

for i in range(1, 10):
    print(f'2 * {i} = {2*i}')

#문제
for i in range(1, 10):
    print(f'{i}단------------------------------------')
    for j in range(1 , 10):
        print(f'{i} * {j} = {j * i}')
