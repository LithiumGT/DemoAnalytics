import datetime
import random
import pandas as pd

# PEP 695: Объявляем псевдонимы типов для структуры данных
type ProductPriceMap = dict[str, int]
type CategoryStructure = dict[str, ProductPriceMap]
type RawDataDict = dict[str, list[datetime.date | str | int]]

# 1. Справочник товаров и базовых цен для генерации реалистичных данных
DATA_STRUCTURE: CategoryStructure = {
    "Электроника": {
        "Смартфон": 45000,
        "Наушники": 7000,
        "Умные часы": 15000,
        "Повербанк": 2500
    },
    "Одежда": {
        "Худи": 4500,
        "Футболка": 1800,
        "Джинсы": 5000,
        "Кроссовки": 8500
    },
    "Канцелярия": {
        "Ежедневник": 1200,
        "Набор маркеров": 800,
        "Рюкзак": 3500
    }
}


def generate_sales_dataset(records_count: int = 50) -> pd.DataFrame:
    """Генерирует случайные, но логически связанные данные о продажах."""

    # Инициализируем пустые списки под будущие колонки таблицы
    dates: list[datetime.date] = []
    categories: list[str] = []
    products: list[str] = []
    revenues: list[int] = []
    quantities: list[int] = []

    # Начальная дата для генерации временного ряда (текущий 2026 год)
    start_date = datetime.date(2026, 1, 1)

    for i in range(records_count):
        # Случайная дата в пределах первых пяти месяцев 2026 года
        current_date = start_date + datetime.timedelta(days=random.randint(0, 150))

        # Случайный выбор категории и товара из нашего справочника
        category = random.choice(list(DATA_STRUCTURE.keys()))
        product = random.choice(list(DATA_STRUCTURE[category].keys()))

        # Логика количества: канцелярию берут чаще и больше, электронику — реже
        if category == "Электроника":
            quantity = random.choice([1, 1, 1, 2])  # Чаще 1 штука, редко 2
        elif category == "Одежда":
            quantity = random.randint(1, 3)
        else:
            quantity = random.randint(1, 10)  # Канцелярию берут оптом

        # Считаем выручку: базовая цена * количество
        base_price = DATA_STRUCTURE[category][product]
        revenue = base_price * quantity

        # Записываем данные
        dates.append(current_date)
        categories.append(category)
        products.append(product)
        quantities.append(quantity)
        revenues.append(revenue)

    # Собираем сырой словарь данных с явным указанием типов
    raw_data: RawDataDict = {
        "Дата": dates,
        "Категория": categories,
        "Товар": products,
        "Количество": quantities,
        "Выручка": revenues
    }

    # Создаем DataFrame и сортируем его по дате для красоты
    df = pd.DataFrame(raw_data)
    return df.sort_values(by="Дата").reset_index(drop=True)


def main() -> None:
    # Генерируем датасет
    df_sales = generate_sales_dataset(records_count=50)

    # Сохраняем в Excel, используя движок openpyxl
    output_filename = "sales.xlsx"
    df_sales.to_excel(output_filename, index=False, engine="openpyxl")
    print(f" Успешно сгенерирован файл '{output_filename}' с {len(df_sales)} записями!")


if __name__ == "__main__":
    main()