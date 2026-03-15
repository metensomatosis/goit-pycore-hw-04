def total_salary(path: str) -> tuple[int, int]:
    total: int = 0
    count: int = 0

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()

                if not line:
                    continue

                name, salary = line.split(",")
                total += int(salary)
                count += 1

        if count == 0:
            return 0, 0

        average: int = total // count
        return total, average

    except FileNotFoundError:
        print("Файл не знайдено.")
        return 0, 0
    except ValueError:
        print("Помилка в форматі даних у файлі.")
        return 0, 0


if __name__ == "__main__":
    total, average = total_salary("salary.txt")
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
