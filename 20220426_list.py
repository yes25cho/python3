empty_list = []
player = ['Faker', 10, True]        #문자, 숫자. 불리안
print(len(empty_list))  #0
print(len(player))  #3
print(type(empty_list), type(player))
empty_list2 = list()        #[]
print(len(empty_list2))     #0
message = list('miracle')
print(message)      #['m', 'i', 'r', 'a', 'c', 'l', 'e']
# numbers = list(56)  #TypeError: 'int' object is not iterable
# print(numbers)

#리스트 추가
player = player+[10, 11]        #리스트 풀려서 하나씩 추가
print(player)

player.append([0, 21])          #리스트 통째로 추가 (훨씬 많음)
print(player)
player.append(56)
print(player)

#수정
player.insert(2, 'SKT T1')      #index, 값
print(player)
player.extend([30, 31])         #+=랑 같음, 즉 플려서 하나씩추가
print(player)
#append : 리스트 통 째로 추가
#insert
#++, extend()

print(player)
player.append(40)
print(player)
#player.insert(11,50)
# player.insert(-1,50)   #실패, 마지막꺼 밀어내고 그자리 차지
player.insert(len(player), 50)       #선호
print(player)

#수정
print(player[0:4])
print(player[0])
player[0] = '스티치'
print(player[0])
print(player)
print(player[6])
player[6][0] = [2, 3]
print(player)
player[6] = 16
print(player)

#삭제
del player[2]   #인덱싱으로 지우기
print(player)
player.remove(30)  #값으로 지우기
print(player)
player.pop(2)   #인덱스로 지우기
print(player)
# player.clear()  #리스트 지우기(초기화)
#remove() : 값으로 지우기
#pop(index), del 리스트명[index]: 인덱스 지우기
#pop() : 맨뒤에서 지우기

print(100 in player)    #False
print(10 in player)     #True
print('아이유' in player)  #False
print(player)
player[0] = 1
player.sort()   #정렬
print(player)
player.reverse()    #뒤집기(내림차순 정렬 아님)
print(player)

#******** range()
a = range(14)
print(a)
a2 = list(a)
print(a2)
print(list(range(14)))
b = range(1, 14+1)
print(list(b))
c = range(1, 14 +1, 2)
print(list(c))
#range(stop) : range(0, stop): 0, 1, 2, ..., stop-1
#range(start, stop) : start, start+1, start+2, ..., stop-1
#range(start, stop, step) : start, start+step, start+step+step, ..., stop-1

반1 = list(range(1, 14+1))
반2 = list(range(1, 14+1))
반3 = list(range(1, 14+1))
반3.remove(6)
반3.remove(10)
print(반3)
#두자리 숫자 중 홀수인 숫자 리스트를 출력하자
print(list(range(11, 99+1, 2)))
#한자리 숫자중 짝수인 숫자 리스트를 출력 하자
print(list(range(8, 0, -2)))

