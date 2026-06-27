def calculate_max_power(N):
    """Вычисляет максимальную силу драконьей стаи."""
    if N <= 2:
        return N
    
    if N % 3 == 0:
        return 3 ** (N // 3)
    elif N % 3 == 1:
        return 4 * (3 ** ((N - 4) // 3))
    else:  # N % 3 == 2
        return 2 * (3 ** (N // 3))


if __name__ == "__main__":
    N = int(input("Введите N (0 < N < 100): "))
    result = calculate_max_power(N)
    print(f"Максимальная сила стаи: {result}")