from drink import Drink     # 나와 같은 폴더에 있는 drink.py 파일을 가져오기

class Bubbletea(Drink):
    #클래스 변수
    _PEARLS = ('타피오카', '코코', '알로에', '곤약')
    def __init__(self, name, price):
        super().__init__(name,price)    #부모의 생성자 호출하자
        self.pearl = 0
    def __str__(self):
        return super().__str__()+f'\t펄 : {Bubbletea._PEARLS[self.pearl]}펄'
    def set_pearl(self):
        for index, pearl in enumerate(Bubbletea._PEARLS):
            print(f'{index+1}. {pearl}')
        pearl = input('펄 종류를 선택 하세요 : ')
        # if pearl == ' ':
        #     pearl = 1
        # self.pearl = int(pearl)-1
        self.pearl = 0 if pearl == '' else int(pearl) - 1
    def order(self):
        super().order()
        self.set_pearl()

if __name__ == '__main__':       #*****
    버블티1 = Bubbletea('타로버블티', 2700)
    버블티1.order()
    print(버블티1)


