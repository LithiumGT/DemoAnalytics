import pandas as pd
import plotly.express as px

# Создаем псевдоним типа для читаемости (Python 3.12+)
type SalesData = pd.DataFrame

data: SalesData = pd.DataFrame({
    "День": [1, 2, 3, 4],
    "Выручка": [100, 150, 120, 180]
})

# PX сам понимает структуру и подписывает оси
fig = px.line(data, x="День", y="Выручка", title="Продажи (Express)")
fig.show()
