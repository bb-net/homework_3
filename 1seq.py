quantity = int(input('Введите количество элементов: '))
list = [int(input(f'Введите {x+1} число: ')) for x in range(quantity)]
list.sort()
print(list)