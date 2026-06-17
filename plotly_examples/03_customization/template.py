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

# Наводим полный лоск на график с помощью .update_layout() и .update_traces()
fig_line.update_layout(
    # 1. Меняем тему на профессиональную темную
    template="plotly_dark",

    # 2. Тонкая настройка заголовка
    title={
        'text': "Аналитика продаж за 2026 год",
        'y': 0.95,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'
    },

    # 3. Кастомизация осей
    xaxis_title="Временной период",
    yaxis_title="Общая выручка ($)",

    # 4. Управление легендой (переносим её вниз графика)
    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=-0.3,
        xanchor="center",
        x=0.5
    )
)

# Дополнительно: можно изменить стиль самих линий (сделать их сглаженными)
fig_line.update_traces(line_shape="spline", line_width=3)

fig_line.show()