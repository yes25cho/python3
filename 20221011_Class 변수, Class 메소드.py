#클래스 변수: 객체로 생성 하지 않아도 클래스에 하나 존재하는 변수
#클래스 메소드: 객체로 생성 하지 않아도 클래스에 하나 존재하는 메소드

# 학생
# 속성 : 학번, 이름
class Student:
    def __init__(self, student_number, name):
        self.student_number = student_number
        self.name = name

    def __str__(self):
        return f'학번 : {self.student_number}\t이름 : {self.name}'
    def __getitem__(self, key):
        if key == '학번':
            return self.student_number
        elif key == '학년':
            return self.student_number[0]

# 동아리
# 속성 : 동아리명, 장소, 멤버들
# 메소드 : 장소 설정하자(), 멤버 추가하자(), 활동하자()
class Club:
    count = 0       #클래스 변수

    @classmethod        #클래스 함수
    def get_count_club(cls):
        return f'동아리 개수 : {Club.count}'

    def __init__(self, name):
        self.name = name        #동아리이름
        self.location = None    #장소
        self.members = []       #멤버들
        Club.count += 1

    def __str__(self):
        s = ''
        for member in self.members:
            s += str(member) + "\t"
        return f'동아리명 : {self.name}\t장소 : {self.location}\t멤버들 : {s}'

    def set_location(self, location):
        self.location = location

    def add_member(self, student):
        self.members.append(student);

    def set_action(self, action):
        self.action = action

    def act(self):
        print(self.action)

    def __len__(self):  #동아리 멤버수 리턴
        return len(self.members)
    def __del__(self):      #del 객체 했을때, 메모리에서 삭제
        print(f'{self.name}는 간다')




학생1 = Student('2213', '임채영')
print(학생1)
학생2 = Student('2106', '양다연')
print(학생2)

동아리1 = Club("사진반")
동아리1.set_location('실습1')
동아리1.set_action("사진 찍기")
동아리1.add_member(학생2)
동아리1.add_member(학생1)
print(동아리1)
동아리1.act()
print(len(동아리1.members))

동아리2 = Club("보드게임반")
동아리2.set_action("보드 게임 하기")
동아리2.add_member(학생1)
print(동아리2)
동아리2.act()

print(Club.count)
print(Club.get_count_club())

#특수메소드
#__init__(self,...)     #생성자, 멤버 변수 초기화

#__str__(self)      #클래스의 객체를 문자열화      str(객체) --> 무엇을 리턴 하는냐
# (주로 객체의 속성을 알아볼 수 있도록 정보 표시)

#__len__(self)     #len(객체) 재정의
print("__len__()")
print(len(동아리1))        #동아리1의 멤버수를 출력 하다.

#__getitem__(self, key)     #객체[key] 재정의
print('__getitem__()')
print(학생1)
print(학생1['학번'])
print(학생1['학년'])

#__del__(self)      #객체를 명시적으로 지울 때 호출되는 메소드
print('__del__()')
number = 10
print(number)
# del number
# print(number)
print('동아리1')
del 동아리1
print(동아리1)