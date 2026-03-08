def get_cats_info(path):
    cats = []

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue

                cat_id, name, age = line.split(",")

                cats.append({
                    "id": cat_id,
                    "name": name,
                    "age": age
                })

    except FileNotFoundError:
        print("Файл не знайдено")
    except Exception as error:
        print(f"Сталася помилка: {error}")

    return cats


cats_info = get_cats_info("cats_file.txt")

for cat in cats_info:
    print(cat)