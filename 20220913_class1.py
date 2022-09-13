#클래스 연습 1
# 1. 요리 2. 연예인 3. 자동차 4. 게임
"""
속성
title : 제목
genre :
bm : 비즈니스 모델
platform : 플랫폼

행동
실행하다()
로그인하다()
저장하다()

객체
wow, 마인트래프트, 배틀그라운드

java
class Game{
    String title;
    String genre;
    int platform;       //0:윈도우 1:맥, 2: 아이, 3: 안드 4: 닌텐도
    public void run(title){
        this.title = title;
        this.genre = "MMORPG"
        this.platform = 0;
    }
    public boolean login(){
    }
    public int save(){
    }
    public toString(){
        retur title + genre;
    }
}

예서게임 = new Game("World of Warcraft);
채영게임 = new Game("배틀 그라운드");
채영게임.genre = "FPS"
"""
class Game:
    def __init__(self, title): #특수 메소드 : 생성자(던더 함수)
        self.title = title
        self.genre = "MMORPG"
        self.platform = 0

    def run(self):
        print("실행")

    def login(self, id, password):
        print(f'{id}님 환영합니다.')

    def save(self):
        print('저장 완료')

    def __str__(self):  #특수 메소드 : 믄자열 표현
        return f'{self.title} {self.genre}'

예서게임 = Game('World of Warcraft')
채영게임 = Game('마인크래프트')
채영게임.genre = '샌드박스'
print(예서게임)
print(채영게임)
