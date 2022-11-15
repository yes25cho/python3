from copy import copy

from bubbletea import Bubbletea
from coffee import Coffee

class Order:
    def __init__(self):
        #메뉴판
        self.menu = []
        self.init_menu()
        #주문한 음료수 리스트
        self.order_menu = []
    def __str__(self):
        pass
    def init_menu(self):#메뉴판 초기화
        new_menu = Bubbletea("하농녹차오레오", 4500)
        self.menu.append(new_menu)
        new_menu = Coffee("카페 모카", 3000)
        self.menu.append(new_menu)
        new_menu = Bubbletea("라즈베리소다", 2900)
        self.menu.append(new_menu)
    def __str__(self):
        #self.order_menu에서 drink 하나씩 꺼내서 이름과 가격을 출력
        return '\n'.join(map(str, self.order_menu))
    def order(self):
        #반복
        while True:
            self.show_menu()   #메뉴판을 보여주자
            choice = input("원하는 음료수를 고르세요(엔터치면 끝) : ")
            if choice == '':
                break
            new_drink = copy(self.menu[int(choice) - 1])
            new_drink.order()
            self.order_menu.append(new_drink)
    def show_menu(self):
        for index, drink, in enumerate(self.menu):
            print(f'{index+1}. {drink.name}\t{drink.price}원')

if __name__ == '__main__':
    order = Order()
    order.order()