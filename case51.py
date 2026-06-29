def max_dragon_power(N):
    """Возвращает максимальную силу стаи и разбиение."""
    if N <= 2:
        return N, [N]
    
    if N % 3 == 0:
        count_3 = N // 3
        return 3 ** count_3, [3] * count_3
    elif N % 3 == 1:
        count_3 = (N - 4) // 3
        return 4 * (3 ** count_3), [4] + [3] * count_3
    else:  # N % 3 == 2
        count_3 = (N - 2) // 3
        return 2 * (3 ** count_3), [2] + [3] * count_3


# Пример использования
N = int(input("Введите N: "))
power, breakdown = max_dragon_power(N)
print(f"Сила: {power}")
print(f"Разбиение: {' × '.join(map(str, breakdown))} = {power}")