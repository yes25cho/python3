#2214 조예서
#1

def sum_odd(phon):
    tot = 0
    for n in phon:
        i = int(n)
        if i%2==1:
            tot += i;
    return tot

# result = sum_odd('01012345678')
# print(result)

#2
def encrypt(w):
    sList = 'aeiou'
    st = w.lower()
    for s in sList:
        st = st.replace(s,'*')
    st = st.upper()
    return st

#print(encrypt('ADiou'))

#3
def dec_to_bin(n):
    b = bin(n)
    s = str(b)
    s = s.replace('0b',"")
    return int(s)

#print(dec_to_bin(77))

#4
def abbreviate(c):
    c=c.upper()
    e = f'{c[0]}. '
    cot =0
    for s in c:
        if cot==1:
            e+=f'{s}. '
            cot = 0
        if s==' ':
            cot+=1
    return e

#print(abbreviate('Maverick l'))

#5
def fare_pc(minute):
    if minute%10!=0:
        minute//=10
        return (minute+1)*1000
    else:
        minute //= 10
        return minute*1000

# print(fare_pc(minute=3))
# print(fare_pc(minute=20))
# print(fare_pc(minute=34))

#6
def get_bmi(height,weigth):
    height /= 100
    bmi = round(weigth/(height*height),2)
    if bmi<18.5:
        return f'저체중 {bmi}'
    elif bmi<23:
        return f'정상 {bmi}'
    elif bmi<25:
        return f'과체중 {bmi}'
    else:
        return f'비만 {bmi}'

#print(get_bmi(height=170, weigth=60))

#7
#def

#8
def rgb_to_hex(r, g, b):
    rgb ='#'
    rgb += hex(r)
    rgb += hex(g)
    rgb += hex(b)
    return rgb.replace('0x','')

#print(rgb_to_hex(r=2, g=0, b=127))

#2214 조예서