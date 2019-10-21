quantity_1 = int(input('Введите количество элементов: '))
list_1 = [int(input(f'Введите {x+1} число: ')) for x in range(quantity_1)]

quantity_2 = input('Введите любое количество чисел через запятую: ')
list_2 = (quantity_2.split(","))

result = set(list_1) - set(list_2)
print(result)

