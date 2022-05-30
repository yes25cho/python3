#
games = {"LOL", "Overwatch", "Tetris", 1942, 2048}
print(games)        #{2048, 'Overwatch', 'Tetris', 'LOL', 1942}
                    #{2048, 'Overwatch', 1942, 'LOL', 'Tetris'}
                    #인덱스로 불러 올수 없다

empty_set = {}      #빈 딕셔너리
empty_set = set()   #빈 셋
print(set({'google':'google.com', 18: 'unesco.crg'}))
#가져오지 못하니까 수정도 못함
#요소 추가
games.add('테일즈러너')
print(games)
games.update(("카트라이더", "지렁이"))
print(games)
#요소 제거
games.remove("LOL")
print(games)

#셋연산
games.add("Fifa")
print(games)
#{2048, 'Tetris', 1942, '테일즈러너', '지렁이', 'Overwatch', '카트라이더', 'Fifa'}

#교집합
s3 = {3, 6, 9, 12}
s4 = {4, 8, 12, 16}
s3 & s4
print(s3.intersection(s4))

#합집합
s3 | s4
print(s3.union(s4))

#자집합
s3-s4
print(s3.difference(s4))

#대칭 차집합
s3^s4
print(s3.symmetric_difference(s4))
#p56, 57실습 하자


#p57 표 *********
a = set()
a.add('밥')
a.add('국')
print(a)
a.add('밥')
print(a)
idol = ['세븐틴', '스트레이키즈', '악뮤', '방탄소년단', '방탄소년단']
print(idol)
print(list(set(idol)))  #중복제거:set() -> list()
