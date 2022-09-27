'''
Python
변수, 함수 : snake_case
클래스 : CamelCase

set 함수 : 웬만하면 자세하게
클래스, 변수 이름 명확하게

변수이름 대소문자 통일

일관성있게
'''

class Food:
    def __init__(self, name):
        self.name = name
        self.style = None
        self.money = 0
    def set_style(self, style):
        self.style = style
    def set_money(self, money):
        self.money = money  #money 가 음수 0, 양수면 그대로

    def __str__(self):
        return f'{self.name}\t비용 : {self.money}\t style : {self.style}'



class DeliveryFood(Food):
    def __init__(self, name):
        super().__init__(name)
        self.de_m = 0
    def set_delivery_money(self, delivery_money):
        self.delivery_money = delivery_money
    def __str__(self):
        return f'{super().__str__()}\t배달료 : {self.de_m}'


치킨 = DeliveryFood('처갓집')
치킨.set_style('튀김')
치킨.set_money(36000)
치킨.set_delivery_money(2500)
print(치킨)

class StreetFood(Food):
    def __init__(self, name):
        super().__init__(name)
        self.shape = None
        self.season = None

    def set_shape(self, shape):
        self.shape = shape

    def set_season(self,season):
        self.season = season

    def __str__(self):
        return f'{super().__str__()}\t매장 형태 : {self.shape}\t 계절 : {self.season}'

붕어빵 = StreetFood('황금 붕어빵')
붕어빵.set_style('빵')
붕어빵.set_money(5000)
붕어빵.set_shape('수레')
붕어빵.set_season('겨울')
print(붕어빵)



#옆친구와 클래스 구조 만들고
#객체화 하고
#상속하고
#출력

'''
사람 - 이름, 나이, 성별
선생님 - 과목, 담임반
'''
'''
클래스는 웬만하면 단수. 여러가 담음면 복수
수치가 들어오는 값이면, 가능하면 숫자로 세팅하자
    나이, 생년 등은 숫자, 핸드폰번호는 문자로 처리 하자
    01012345678은 10억 1234만 5678이 아님 => '01012345678'
'''

class Person:
    def __init__(self, name):
        self.name = name
        self.age = None
        self.gender = None

    def set_age(self, age): #매개변수와 함수이름을 같게하지말 것
        self.age = age

    def set_gender(self, gender):
        genders = ['여자','남자']
        if gender in genders:
            self.gender = gender

    def __str__(self):
        return f'{self.name}\t{self.age}\t{self.gender}'

# people에 값넣기
고나근샘 = Person('고낙은')
고나근샘.set_age(34)
고나근샘.set_gender('남자')
print(고나근샘)

class Teacher(Person):
    def set_subject(self, subject):
        self.sub = subject
    def set_homeroom_teacker(self, homeroom_teacker):
        self.homeroom_teacker = homeroom_teacker
    def __str__(self):
        return f'{super().__str__()}\t담당과목: {self.sub}\t담임반: {self.hrt}'


#Teacher에 값넣기
고낙은샘 = Teacher('고낙은')

고낙은샘.set_subject('체육')
고낙은샘.set_homeroom_teacker('2-2')
print(고낙은샘)
