def sum_negative_between_min_max(arr):
    if not arr:
        return 0
    
    max_idx = max(range(len(arr)), key=lambda i: arr[i])
    min_idx = min(range(len(arr)), key=lambda i: arr[i])
    
    start, end = sorted([max_idx, min_idx])
    
    return sum(x for x in arr[start+1:end] if x < 0)


# Пример использования
if __name__ == "__main__":
    # Тест 1: обычный случай
    arr1 = [5, -2, 3, -4, 1, -6, 0]
    print(sum_negative_between_min_max(arr1))  # -6
    
    # Тест 2: max и min соседи
    arr2 = [10, -5, 3, 8]
    print(sum_negative_between_min_max(arr2))  # 0
    
    # Тест 3: min раньше max
    arr3 = [-10, 2, 8, -3, 4, 1]
    print(sum_negative_between_min_max(arr3))  # 0
    
    # Тест 4: все отрицательные
    arr4 = [-5, -1, -3, -2, -4]
    print(sum_negative_between_min_max(arr4))  # 0