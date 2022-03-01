# Sort the array reverse

from typing import Any, MutableSequence

def reverse_array(a: MutableSequence) -> None:
    """ Sort reverse of MutableSequence a's elements """
    n = len(a)
    for i in range(n // 2):
        a[i], a[n-i-1] = a[n-i-1], a[i]

if __name__ == '__main__':
    print('Make array reverse')
    nx = int(input('Input elements : '))
    x = [None] * nx

    for i in range(nx):
        x[i] = int(input(f'Input x[{i}] value : '))

    reverse_array(x)

    print('Sorting completed')
    for i in range(nx):
        print(f'x[{i}] = {x[i]}')