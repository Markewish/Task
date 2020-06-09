# максимальное число
# минимальное число
# медиану
# среднее арифметичесское
# наибольшую последовательность идущих подряд чисел, которая увеличивается 
# наибольшую последовательность идущих подряд чисел, которая уменьшается

import sys
import os
import time
import random
from datetime import timedelta

def main(args):

    if not count_args(args):
        print("invalid number of parameters, specify data file")
    else:
        array_value = get_array_from_file(args[1])
        
        print("\n\tВыполнение операций над данными...\n")

        min_valye, max_valye = find_min_and_max(array_value)
        median = find_median_in_array(array_value)
        average = demo_def_iter(array_value)
        increases = largest_sequence_increases(array_value)
        decreases = largest_sequence_decreases(array_value)

        print(f"Максимальное число: {max_valye}")
        print(f"Минимальное число: {min_valye}")
        print(f"Медиана: {median}")
        print(f"Cреднее арифметичесское: {average}")
        print(f"Наибольшую последовательность идущих подряд чисел, которая увеличивается : {increases}")
        print(f"Наибольшую последовательность идущих подряд чисел, которая уменьшается: {decreases}")

        print_end_time("Скрипт выполнил работу")

    input("\n\tВыход [press enter]: ")


"""
    чтение файла
"""
def get_array_from_file(filePath:str = None)->list:

    if not os.path.exists(filePath):
        print("!!!input file is not exists")
    else:

        print_start_time("\tНачало работы скрипта!")

        array_number = []

        print("\n\tЧтение файла...")

        with open(filePath, 'r') as file:
            for line in file:
                array_number.append(int(line))
                
        print("\n\tФайл прочитан...")
    
        return array_number


"""
    инициализация времени старта
"""
def print_start_time(message:str) -> None:
    print(message)
    global start_time
    start_time = time.time()


"""
    вывод времени выполнения скрипта
"""
def print_end_time(message:str) -> None:
    print(f"\n\t{message} ! ==> {timedelta(seconds = time.time() - start_time)} c.")

"""
    проверяем количестов передаваемых аргументов
"""
def count_args(args:list) -> bool:
    return len(args) == 2


"""
    поиск максимально и минимального значения
"""
def find_min_and_max(array:list) -> tuple:
    min_v = max_v = array[0]
    for i in range(len(array)):
        if min_v > array[i]:
            min_v = array[i]
        if max_v < array[i]:
            max_v = array[i]

    return min_v, max_v


"""
    поиск медианы в отсортированном списке
"""
def find_median_in_array(array:list) -> int:
    temp_array = sorted(array)
    if len(array) % 2 == 0:
        senter_array = int(len(temp_array) / 2)
        return (temp_array[senter_array] + temp_array[senter_array - 1])/2
    else:
        return temp_array[int(len(temp_array) / 2)]


"""
    подсчет среднего арифметичесского
"""
def demo_def_iter(array:list) -> float:
    avg = 0
    for i in range(len(array)):
        avg += array[i]

    return int(avg / len(array))


"""
    наибольшую последовательность идущих подряд чисел, которая увеличивается 
"""
def largest_sequence_increases(array:list) -> int:
    
    sequence_increases = []
    current_sequence_pos = 0
    skip_count_value = 0
    size = len(array) - 1

    for i in range(size):
        #смотрим сколько позиций надо пропустить
        if skip_count_value != 0:
            skip_count_value = skip_count_value - 1
            continue

        # определяем порядок сравнения для положительных 
        # и отрицательных чисел
        # поиск с учетом обоих знаков
            # для положительных
        if array[i] > 0 and array[i] < array[i + 1]:
            sequence_increases.insert(current_sequence_pos, 1)
            # внутренний проход
            for j in range (i, size):
                if array[j] < array[j + 1]:
                    sequence_increases[current_sequence_pos] = sequence_increases[current_sequence_pos] + 1
                    skip_count_value = skip_count_value + 1  
                else :
                    break
            current_sequence_pos = current_sequence_pos + 1
                

            # для отрицательных
        if array[i] < 0 and array[i] > array[i + 1]:
            sequence_increases.insert(current_sequence_pos, 1)
            # внутренний проход
            for j in range (i, size):
                if array[j] > array[j + 1]:
                    sequence_increases[current_sequence_pos] = sequence_increases[current_sequence_pos] + 1
                    skip_count_value = skip_count_value + 1  
                else :
                    break
            current_sequence_pos = current_sequence_pos + 1
    
        #результат выборки
    min_v, max_v = find_min_and_max(sequence_increases)
    return max_v


"""
    наибольшую последовательность идущих подряд чисел, которая уменьшается
"""
def largest_sequence_decreases(array:list) -> int:
    
    sequence_increases = []
    current_sequence_pos = 0
    skip_count_value = 0
    size = len(array) - 1

    for i in range(size):
        #смотрим сколько позиций надо пропустить
        if skip_count_value != 0:
            skip_count_value = skip_count_value - 1
            continue

        # определяем порядок сравнения для положительных 
        # и отрицательных чисел
        # поиск с учетом обох знаков
            # для положительных
        if array[i + 1] > 0 and array[i] > array[i + 1]:
            sequence_increases.insert(current_sequence_pos, 1)
            # внутренний проход
            for j in range (i, size):
                if array[j] > array[j + 1]:
                    sequence_increases[current_sequence_pos] = sequence_increases[current_sequence_pos] + 1
                    skip_count_value = skip_count_value + 1  
                else :
                    break
            current_sequence_pos = current_sequence_pos + 1
                

            # для отрицательных
        if array[i + 1] < 0 and array[i] < array[i + 1]:
            sequence_increases.insert(current_sequence_pos, 1)
            # внутренний проход
            for j in range (i, size):
                if array[j] < array[j + 1]:
                    sequence_increases[current_sequence_pos] = sequence_increases[current_sequence_pos] + 1
                    skip_count_value = skip_count_value + 1  
                else :
                    break
            current_sequence_pos = current_sequence_pos + 1
    
        #результат выборки
    min_v, max_v = find_min_and_max(sequence_increases)
    return max_v
    

# start input point
if __name__ == "__main__":
        main(sys.argv)