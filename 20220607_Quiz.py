# 1. 휴대전화번호 입력하면 -, /, 띄어쓰기 없애고 숫자만 출력 하자
phone_number = '010-7240-4658'
#>> 01072404658
for str1 in phone_number:
    if str == '-'or str == '/' or str == ' ':
        continue
    else:
        print(str1, end='')
print()
# 2. 학번 -> 학년, 반, 학과, 번호 출력하기
student_number = '2204'
#>> 2학년 1반 뉴미디어소프트웨어과 08번
majors = ['', '뉴미디어소프트웨어과', '뉴미디어소프트웨어과',
     '뉴미디어웹솔루션과', '뉴미디어웹솔루션과', '뉴미디어디자인과', '뉴미디어디자인과']
index = int(student_number[1])
g = majors[index]
#>> 2학년 1반 뉴미디어소프트웨어과 8번
if student_number[-2] =='0':
    print(f'{student_number[0]}학년 {student_number[1]}반 {g}{student_number[3:]}번')
else:
    print(f'{student_number[0]}학년 {student_number[1]}반 {g}{student_number[2:]}번')
#-> if문 안쓰고
print(f'{student_number[0]}학년 {student_number[1]}반 {g}{int(student_number[2:])}번')

#3. N-sum
number = 331
나머지 = 0
while number!=0:
    나머지 += number % 10
    number = number //10
print(나머지)

#문자 한자리씩 빼서 계산 하자
number = 52323
number_s = str(number)
sum_num =0
for n in number_s:
    sum_num += int(n)
print(sum_num)
#4. 1~100 396게임을 출력
# i=1
# for i in range(1, 101):
#     if
#     print(i, end=' ')

