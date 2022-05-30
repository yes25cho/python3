#튜플
from Tools.scripts.pathfix import new_interpreter

t = ()
xy = (2560, 1440)
color = 129, 247, 216
print(t)
print(xy)
print(color)
print(xy+color)
print(xy*2)

#패킹, 언패킹 : 자동
color = 129, 247, 216  #패킹
rad, green, blue = color #언패킹
print(rad)      #129
x, y = (1920, 1080)
print(y)       #1080
print(color[1])  #인덱싱
print(color[0:3])   #슬라이싱
#color[1] = 255  #TypeError: 'tuple' object does not support item assignment
new_tuple = xy + color  +(1440, 1080)
print(new_tuple)
print(new_tuple.index(1440))    #1
print(new_tuple.index(1440))    #2

임채영, 이예진 = 10, 8
print(임채영)
print(이예진)
이예진, 임채영 = 임채영, 이예진
print(임채영)  #8
print(이예진)  #10

