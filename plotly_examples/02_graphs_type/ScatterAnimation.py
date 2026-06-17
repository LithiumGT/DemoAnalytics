import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# PEP 695: Объявляем псевдоним типа для фигуры
type AnimatedFigure = go.Figure

# 1. Генерируем тестовые данные: 3 товара на протяжении 6 месяцев 2026 года
months = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь"]
products = ["Смартфоны", "Ноутбуки", "Наушники"]

data_rows = []
for month_idx, month in enumerate(months):
    for prod in products:
        # Моделируем рост продаж к лету с небольшой случайностью
        base_multiplier = month_idx + 1
        quantity = int(np.random.randint(50, 100) * (base_multiplier * 0.5 + 1))
        revenue = quantity * np.random.randint(1500, 3000)

        data_rows.append({
            "Месяц": month,
            "Товар": prod,
            "Количество (шт)": quantity,
            "Выручка (₽)": revenue,
            "Доля рынка (%)": np.random.uniform(10, 40)
        })

df = pd.DataFrame(data_rows)

# 2. Строим анимированный график рассеяния
fig: AnimatedFigure = px.scatter(
    df,
    x="Количество (шт)",
    y="Выручка (₽)",
    animation_frame="Месяц",  # Кадр анимации меняется по месяцам
    animation_group="Товар",  # Указываем, за какими объектами следовать
    color="Товар",  # Каждый товар своего цвета
    size="Доля рынка (%)",  # Размер пузырька меняется динамически
    hover_name="Товар",

    # Жестко фиксируем диапазоны осей, чтобы сетка не «прыгала» при смене кадров
    range_x=[0, df["Количество (шт)"].max() + 50],
    range_y=[0, df["Выручка (₽)"].max() + 50000],
    title="Динамика популярности товаров (Январь - Июнь 2026)"
)

# 3. Настройка скорости анимации и внешнего вида
fig.update_layout(
    template="plotly_dark",
    width=900,
    height=600
)

# Увеличиваем скорость перехода между кадрами (в миллисекундах)
fig.layout.updatemenus[0].buttons[0].args[1]["frame"]["duration"] = 800

# Отображаем график
fig.show()