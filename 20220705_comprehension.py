#1~10까지의 수
array  = []
for n in range(1, 20, 3 ):
    array[n]= n
    array  = []
    for n in range(1, 10, 2):
        if n ** 2 > 30:
            array.append()