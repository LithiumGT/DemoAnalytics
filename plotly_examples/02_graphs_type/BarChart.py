import pandas as pd
import plotly.express as px

type SalesDataFrame = pd.DataFrame

def get_data(file_path: str) -> SalesDataFrame:
    # Явно указываем движок openpyxl, знакомый студентам
    return pd.read_excel(file_path, engine='openpyxl')

# Загружаем датасет
df: SalesDataFrame = get_data("sales.xlsx")

# Агрегируем данные для наглядности (вспоминаем pandas)
category_df: SalesDataFrame = df.groupby(["Категория", "Товар"], as_index=False)["Выручка"].sum()

# Строим столбчатую диаграмму
fig_bar = px.bar(
    category_df,
    x="Категория", 
    y="Выручка",
    color="Товар",  # Разделяет столбцы по цветам внутри одной категории
    barmode="group", # Альтернатива: "stack" (один на одном)
    title="Сравнение выручки по категориям и товарам"
)
fig_bar.show()