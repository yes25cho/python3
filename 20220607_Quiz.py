# 1. 휴대전화번호 입력하면 -, /, 띄어쓰기 없애고 숫자만 출력 하자
phone_number = '010-7240-4658'
#>> 01072404658
for str in phone_number:
    if str == '-'or str == '/' or str == ' ':
        continue
    else:
        print(str, end='')
print()
# 2. 학번 -> 학년, 반, 학과, 번호 출력하기
student_number = '2204'
#>> 2학년 1반 뉴미디어소프트웨어과 08번
print(f'{student_number[0]}학년 {student_number[1]}반 뉴미디어소프트웨어과{student_number[2:]}번')
#>> 2학년 1반 뉴미디어소프트웨어과 8번
if student_number[-2] =='0':
    print(f'{student_number[0]}학년 {student_number[1]}반 뉴미디어소프트웨어과{student_number[3:]}번')
else:
    print(f'{student_number[0]}학년 {student_number[1]}반 뉴미디어소프트웨어과{student_number[2:]}번')
#-> if문 안쓰고


#3. N-sum
number = 331
str_num = str(number)
for i in str_num:
    print(i)

#4. 1~100 396게임을 출력
# i=1
# for i in range(1, 101):
#     if
#     print(i, end=' ')

