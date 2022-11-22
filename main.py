numbers_string=input("Введите числа через пробел: ")
numbers_list=numbers_string.split()

print(f'Список введенных чисел:{numbers_list}')

def sort_up(lst):
    return sorted(lst)

def binary_search(array, element, left, right):
    middle = (left + right) // 2

    if array[left] == array[right] == element:
        return 'любым'
    if element >= array[right]:
        return '[' + str(right + 1) + '] после ' + str(array[right])
    if element <= array[left]:
        return '[' + str(left) + '] перед ' + str(array[left])

    if array[middle] == element:
        return '[' + str(middle + 1) + '] между ' + str(array[middle]) + ' и ' + str(array[middle + 1])
    elif element < array[middle]:
        return binary_search(array, element, left, middle - 1)
    elif element > array[middle]:
        return binary_search(array, element, middle + 1, right)

numbers=[]
for i, item in enumerate(numbers_list):
    numbers_list[i] = int(item)
    numbers.append(item)
numbers = (numbers_list)

print(f'Введенные числа в порядке возрастания: {numbers}')

some_num=int(input('Введите любое число: '))
pos = binary_search(numbers, some_num, 0, len(numbers) - 1)

print(f'Введенное число будет на позиции: {pos}')
numbers.append(some_num)
numbers=sort_up(numbers)

print(f' Обновленный список: {numbers}')