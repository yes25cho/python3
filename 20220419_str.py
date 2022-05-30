greeting = 'hello'
to = 'world!'
say_hello = greeting +', '+to
print(say_hello)
print(greeting * 5)
print(greeting + '\n' + to)
print("'"+greeting+"'")
print('"'+greeting+'"')
print("\""+greeting+"\"")
print('\''+greeting+'\'')
names = """양다연
인소리
이예진
"""
print(names)

#*** indexing, slicing
names = """양다연인소리이예진"""
print(names[2]) #'연'
print(names[4]) #'소'
print(names[8]) #'진'
print(names[-1]) #'진'
print(names[-2]) #'예'
print(names[-9]) #'양'
#indexing은
# 0  1  2  3  4  5  6  7  8
#-1 -2 -3 -4 -5 -6 -7 -8 -9
student_number = '2112'
print(student_number[0]+'학년')
print(f"{student_number[0]}학년")
print(f"{student_number[1]}반")

#"""양다연인소리이예진"""
print(names[2:5])       #[2]~[4]

#'연인'
print(names[2:4])
print(names[-7:-5])
#'소리이'
print(names[4:7])
#'예진'
print(names[7:9])


print(f'{student_number[2:4]}번')
print(f'{student_number[-2:]}번')    #start:end-1    [start:]_끝까지
print(f'{student_number[0:2]}학년반')
print(f'{student_number[0:-2]}학년반')
print(f'{student_number[:-2]}학년반')  #start:end-1    [:end] 앞까지
print(f'{student_number[:]}학년반')  #start:end-1    [:] 앞~끝까지 #문자열을 넣음


#문자열 함수
print(f'길이 : {len(student_number)}') #4
print(f'2개수 : {student_number.count("2")}') #2
print(f'{"NCT dream buffering".upper()}')
print(f'{"NCT dream buffering".lower()}')
s = "   NCT dream buffering     "
print(f'{s.strip()}')
print(f'{s.lstrip()}')
print(f'{s.rstrip()}')
print(f'{s.find("e")}') #[7]
print(f'{s.find("z")}') #없으면 -1
print(f'{s.rfind("e")}') #[7]
print(f'{s.index("e")}')    #2
print(f'{s.find("z")}') #없으면 -1
print(f'{s.index("b")}') #7
#print(f'{s.index("z")}')    #없으면 오류난다 ValueError: substring not found
print(f'{s.replace("buffering","hello future")}')       #replace하면 바뀐 문자열을 리턴하지만 원본은 바뀌지 않음
print(s)

print('e' in s) #True
print('z' in s) #False

#split, join
ip = '10.253.123.119'
ip_List = ip.split('.')
print(ip_List)
names = '양다연, 최자윤, 임채영, 이예진, 인소리'
name_List = names.split(',')
print(name_List)
print(name_List[2])
print(name_List[2:4])
ip_list_str = '::'.join(ip_List)
print(ip_list_str)
name_List_str = ' | '.join(name_List)
print(name_List_str)
print(",".join(name_List))


#format
s = 'name: {}, number: {}, soccer: {}'
print(s.format('손흥민', 7, True))
s = 'name: {1}, number: {2}, soccer: {0}'
print(s.format('손흥민', 7, True))
s = '-'
print(s.format(name='손흥민', s=True, n=7))

phone_number = '010-9793-8993'
print(f'전화 번호 : {phone_number[9:13]}')
print(f'전화 번호 : {phone_number[9:]}')    #끝까지 출력
print(f'전화 번호 : {phone_number[-4:]}')   #좋을 수 있음
#p46연습
s = "name: {}, number: {}, soccer: {}"
print(s.format("Ronaldo", 7, True))
print("name: {name}, number: {num}".format(name = "Jordan", num = 23))

print("{:d}".format(515))
print("{:5d}".format(515))
print("{:=+5d}".format(515))
print("{:05d}".format(515))
print("{:+05d}".format(515))

print("{:f}".format(11.17))
print("{:12f}".format(11.17))
print("{:12.1f}".format(11.17))

print("{:=+.1f}".format(11.17))

