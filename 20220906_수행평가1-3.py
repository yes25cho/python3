"""
share: 몫, reminder : 나머지
무한 반복
    number를 2로 나누자
    number이 0이면, 끝내고 결과 리턴
    아니면, number를 2 로 나눈 나머지를 앞으로 보관 하자 s = '1'
        number는 number를 2로 나눈 몫으로 설정하자
"""

def dec_to_bin(n):
    s = ''
    while n>0:
        s = str(n%2) + s
        n = n//2
    return s

print(dec_to_bin(10))
print(dec_to_bin(2))
print(dec_to_bin(77))
print(dec_to_bin(1024))

def dec_to_bin4(n):
    s = ''
    while True:
       #share = n // 2
        if n == 0:
            return s
        else:
            reminder = n%2
            s = str(reminder)+s
            n = n // 2

print(dec_to_bin4(10))

def dec_to_bin2(n):
    b = bin(n)
    return b.replace('0b',"")

def dec_to_bin3(n):
    return bin(n)[2:]


#print(dec_to_bin2(10))