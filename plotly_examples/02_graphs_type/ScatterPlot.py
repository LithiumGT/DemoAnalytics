import pandas as pd
import plotly.express as px

type SalesDataFrame = pd.DataFrame

def get_data(file_path: str) -> SalesDataFrame:
    # Явно указываем движок openpyxl, знакомый студентам
    return pd.read_excel(file_path, engine='openpyxl')

# Загружаем датасет
df: SalesDataFrame = get_data("sales.xlsx")

fig_scatter = px.scatter(
    df,
    x="Количество",    y="Выручка",
    color="Категория",       # Цвет точки зависит от категории
    size="Выручка",         # Размер точки масштабируется по объему продаж
    hover_name="Товар",     # При наведении в заголовок подсказки выводится имя товара
    title="Взаимосвязь объема продаж и выручки"
)
fig_scatter.show()