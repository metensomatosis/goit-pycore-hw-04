def total_salary(path: str) -> tuple:
    total = 0
    count = 0

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue  # пропускаємо порожні рядки

                name, salary = line.split(",")
                total += int(salary)
                count += 1

        if count == 0:
            return (0, 0)

        average = total / count
        return (total, average)

    except FileNotFoundError:
        print("Файл не знайдено.")
        return (0, 0)

    except ValueError:
        print("Помилка в форматі даних у файлі.")
        return (0, 0)

total, average = total_salary("salary.txt")
print(f"Загальна сума заробітної плати: {total}, \nСередня заробітна плата: {average}")