import pandas as pd
import plotly.express as px

type SalesDataFrame = pd.DataFrame

# Предположим, данные уже загружены из нашего sales.xlsx
df: SalesDataFrame = pd.read_excel("sales.xlsx", engine="openpyxl")

# Строим линейный график динамики продаж по категориям
monthly_sales = df.groupby(["Дата", "Категория"], as_index=False)["Выручка"].sum()

fig_line = px.line(
    monthly_sales,
    x="Дата",
    y="Выручка",
    color="Категория",
    title="Динамика по категориям"
)

# Включаем "магический" режим подсказок через обновление Layout
fig_line.update_layout(
    hovermode="x unified"  # Объединяет подсказки всех линий по оси X
)
fig_line.show()