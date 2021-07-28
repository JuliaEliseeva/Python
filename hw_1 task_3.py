# Задача_3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn

n = int(input('Введите число: '))
nn = int("%i%i" % (n, n))
nnn = int("%i%i%i" % (n, n, n))
print(n + nn + nnn)
