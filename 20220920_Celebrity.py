#연예인, 가수, 배우
class Celebrity:
    def __init__(self, name):
        self.name = name
        self.debut_date = None
        self.company = None

    def set_debut_date(self, debut_date):
        self.debut_date = debut_date

    def set_company(self, company):
        self.company = company
    def __str__(self):
        return f'{self.name}\t{self.debut_date}\t{self.company}'

아이유 = Celebrity('이지은')
아이유.set_debut_date('2008-09-18')
아이유.set_company('이담엔터테이먼트')
print(아이유)

class Singer(Celebrity):
    def set_song(self, song):
        self.song = song
    def __str__(self):
        return f'{super().__str__()}\t대표곡 : {self.song}'

태민 = Singer('이태민')
태민.set_company('SM 엔터테인먼트')
태민.set_song('MOVE')
print(태민)
print(태민.song)

class Actor(Celebrity):
    def __init__(self, name):
        super().__init__(name)
        self.drama = None
    def set_drama(self, drama):
        self.drama = drama
    def __str__(self):
        return f'{super().__str__()}\t 대표작 : {self.drama}'

정경호 = Actor('정경호')
정경호.set_debut_date('2003-00-00')
정경호.set_company('매니지먼트 오름')
정경호.set_drama("슬기로운 의사생활")
print(정경호)
print()

내아가들 = [태민, 정경호]
for 내아가 in 내아가들:
    print(내아가)