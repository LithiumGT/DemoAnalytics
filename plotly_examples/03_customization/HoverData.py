import pandas as pd
import plotly.express as px

type SalesDataFrame = pd.DataFrame

# Предположим, данные уже загружены из нашего sales.xlsx
df: SalesDataFrame = pd.read_excel("sales.xlsx", engine="openpyxl")

# Агрегируем для примера
product_sales = df.groupby("Товар", as_index=False)[["Выручка", "Количество"]].sum()

fig = px.bar(
    product_sales,
    x="Товар",
    y="Выручка",
    title="Настройка подсказок (Hover)",

    # 1. Текст, который станет жирным заголовком подсказки
    hover_name="Товар",

    # 2. Настраиваем, какие данные показывать, а какие скрыть
    hover_data={
        "Выручка": ":,.0f",  # Форматируем число: добавляем разделители тысяч, убираем копейки
        "Количество": True,  # Просто показываем колонку
        "Товар": False  # Скрываем дублирующееся имя из тела подсказки, так как оно уже в заголовке
    }
)
fig.show()