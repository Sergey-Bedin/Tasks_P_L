def circular_path(n, m):
    path = []
    current_value = 1
    while True:
        path.append(current_value)
        next_value = (current_value + m - 1) % n
        if next_pos == 0:
            next_pos = n
        if next_pos == 1:
            break
        current_value = next_value
    return ''.join(map(str, path))

if __name__ == "__main__":
    print("Введите n и m через пробел (например: '4 3'):")
    try:
        n, m = map(int, input().split())
        if n <= 0 or m <= 0:
            raise ValueError("n и m должны быть положительными числами")
        print("Результат:", circular_path(n, m))
    except ValueError as e:
        print("Ошибка ввода:", e)