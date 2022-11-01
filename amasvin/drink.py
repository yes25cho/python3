# Drink
    # name
    # price
    # cup_size
    # suger
    # ice
# Drink <- Coffee
# Drink <- Bubbletea
    # pearl
# 옵션들
# 컵사이즈 : 기본, 점보
# 펄 : 타피오카, 알로에, 곤약, 코코넛
# 당도 : 30%, 50%, 70%, 100%
# 얼음량 : 없음, 적게, 기본, 많게

class Drink:
    #클래스 변수
    _CUP_SIZES = ('레귤러', '점보')
    _SUGARS = ('30%', '50%', '70%', '100%')
    _ICES = ('없음', '적게', '기본', '많게')
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.cup_size = 0   #0: 레귤러, 1: 점보
        self.suger = 1  #0: 30%, 1: 50%, 2: 70%, 3: 100%
        self.ice = 2  #0: 없음, 1: 적게, 2: 기본, 3: 많게
    def __str__(self):
        return f'이름 : {self.name}\t가격 : {self.price}원\t컵사이즈 : {Drink._CUP_SIZES[self.cup_size]}\t당도 : {Drink._SUGARS[self.suger]}\t얼음량 : {Drink._ICES[self.ice]}'

    def set_cup_size(self):
        #사용자에게 숫자를 묻자 1: 레귤러, 2: 점보
        for index, cup_size_label in enumerate(Drink._CUP_SIZES):
            print(f'{index+1}. {cup_size_label}')
        cup_size = input('컵사이즈를 선택하세요 : ')
        if cup_size == '':
            cup_size = 0;
        self.cup_size = int(cup_size)-1
        #self.cup_size가 점보(1)일 때, 가격 +500원
        if self.cup_size == 1:
            self.price += 500
    def set_sugars(self):
        for index, sugar_label in enumerate(Drink._SUGARS):
            print(f'{index+1}. {sugar_label}')
        sugar = input('당도를 선택하세요 : ')
        if sugar == '':
            sugar = 2
        self.suger = int(sugar)-1
    def set_ice(self):
        for index, ice_label in enumerate(Drink._ICES):
            print(f'{index+1}. {ice_label}')
        ice = input('얼음량을 선택하세요 : ')
        if ice == '':
            ice = 3
        self.ice = int(ice)-1
    def order(self):
        self.set_cup_size()
        self.set_sugars()
        self.set_ice()
음료1 = Drink('아메리카노', 1800)
음료1.order()
print(음료1)