# 세 정수를 입력받아 최댓값 구하기

print('Finding max value in 3 integers.')
a = int(input('Input a : '))
b = int(input('Input b : '))
c = int(input('Input c : '))

max = a
if b > max:
    max = b
if c > max:
    max = c

print(f'Max is {max}.')
