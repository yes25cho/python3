# #교통수단 문제
# money = int(input('돈을 입력하시오 : '))
# if money >10000:
#     print('택시를 타라')
# elif money >= 720:
#     print('버스를 타라')
# else:
#     print('그냥 걸어가라')
# print()
# #문제 1
# num = int(input('정수를 입력하시오 : '))
# if num % 4 == 0:
#     print('4의 배수')
# elif num % 3 == 0:
#     print('3의 배수')
# elif num % 2 == 0:
#     print('2의 배수')
# print()
# print('다 비교')
# if num % 4 == 0:
#     print('4의 배수')
# #-----------------------
# if num % 3 == 0:
#     print('3의 배수')
# # -----------------------
# if num % 2 == 0:
#     print('2의 배수')
# #-----------------------
#
# #문제 2
# age = int(input('나이 입력 : '))
# if (10 <= age < 20):
#     print('10대')
# elif (30 <= age < 40):
#     print('30대')
# else:
#     print('10대, 30대가 모두 아님.')
#
# print('---------------------------')
# print(f'{(age//10)*10}대')
#
# print('---------------------------')

# #문제3
# x = int(input('정수입력 : '))
# if (x > 10) and (x % 2 == 0):
#     print('10초과 짝수')
# else:
#     print('기타')
#
# #문제4
# score = int(input('점수 입력 : '))
# if 90<= score <= 100:
#     print('A')
# elif 80 <= score:
#     print('B')
# elif 70 <= score:
#     print('C')
# elif 60 <= score:
#     print('D')
# else:
#     print('F')
#
# #문제5
# MBTI = input('타입 입력 : ')
#
# if (MBTI.upper() == "INTP"):
#     print('백엔드형')
# elif (MBTI.upper() == "ENTP"):
#     print('iOS형')
# else:
#     print('아직 개발중입니다.')
# #
# #문제6
# x = int(input('정수 입력 : '))
# if x > 10:
#     if x % 2 == 0:
#         print('10초과 짝수')
#     else:
#         print('10초과 홀수')
# else:
#     print('10이하')

#문제7
#아이디, 패스워드 검사 프로그램
name = 'yes25'
IPBa = 'yes25cho'
PasswordBa = "Varonica0106"
ip = input('ID입력 : ')
if IPBa == ip:
    password = input('비밀번호 입력 : ')
    if PasswordBa == password:
#        print(f'환영합니다 {name}님');
        print('환영합니다. {}님'.format(name));
    else:
        print('알수 없는 사용자 입니다.')
else:
    print('알수 없는 사용자 입니다.')