#4. abbreviate
def addreviate(name):
    #한글자씩 꺼내기
        #첫 번째 대문자로 바꾸고 글자 저장
        #띄어 쓰기 -> 한칸 뒤에 있는 글자를 저장
    name = name.strip()
    for index, sp in enumerate(name):
        if index ==0:
            result = sp.upper()+'. '
        elif sp == ' ':
            result += name[index+1].upper()+'. '

    return result.strip()

def addreviate2(name):
    result = ': '.join([word[0] for word in name.split()])
    return result+': '


print(addreviate('Maverick'))
print(addreviate(' Ye seo Cho '))

print(addreviate2('Maverick'))
print(addreviate2(' Ye seo Cho '))
