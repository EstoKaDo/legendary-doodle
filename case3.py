def sum_negative_between_min_max(arr):
    if not arr:
        return 0
    
    # Находим индексы через enumerate
    max_idx = max(range(len(arr)), key=lambda i: arr[i])
    min_idx = min(range(len(arr)), key=lambda i: arr[i])
    
    start, end = sorted([max_idx, min_idx])
    
    return sum(x for x in arr[start+1:end] if x < 0)


# Пример использования
if __name__ == "__main__":
    # Тест 1: обычный случай
    arr1 = [5, -2, 3, -4, 1, -6, 0]
    # max=5 (index0), min=-6 (index5)
    # Диапазон: index1..4 → [-2, 3, -4, 1]
    # Отрицательные: -2 + (-4) = -6
    print(sum_negative_between_min_max(arr1))  # -6
    
    # Тест 2: max и min соседи
    arr2 = [10, -5, 3, 8]
    # max=10 (index0), min=-5 (index1)
    # Диапазон: index1..0 → пусто
    print(sum_negative_between_min_max(arr2))  # 0
    
    # Тест 3: min раньше max
    arr3 = [-10, 2, 8, -3, 4, 1]
    # min=-10 (index0), max=8 (index2)
    # Диапазон: index1..1 → [2]
    print(sum_negative_between_min_max(arr3))  # 0
    
    # Тест 4: все отрицательные
    arr4 = [-5, -1, -3, -2, -4]
    # max=-1 (index1), min=-5 (index0)
    # Диапазон: index1..0 → пусто
    print(sum_negative_between_min_max(arr4))  # 0