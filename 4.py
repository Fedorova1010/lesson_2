# Напишіть програму, в якій користувач вводить фразу з клавіатури, яка складається з 10 символів. На екрані виведіть
# суму ASCII-кодів символів введеного рядка.

a = input('Введіть фразу з 10 символів: ')
print(ord(a[0]) + ord(a[1]) + ord(a[2]) + ord(a[3]) + ord(a[4]) + ord(a[5]) + ord(a[6]) + ord(a[7]) + ord(a[8]) + ord(a[9]))