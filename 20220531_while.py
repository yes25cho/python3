'''
JAVA
while(조건식){
    실행문;
    증감식;
}

python
while 조건식:
    실행문
    증감식
'''

x = 3
while x < 5:
    print(x)
    x+=1
    #무한 루프 멈추는 방법 ctrl+c    KeyboardInterrupt
print('-'*20)
# echo = input()
# while echo != 'exit':
#     print(echo)
#     echo = input()
print('-'*20)
echo = input()

while True:
    if echo == 'exit':
        break
    print(echo)
    echo = input()

