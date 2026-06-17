import plotly.graph_objects as go

# В GO мы передаем чистые списки/серии и вручную упаковываем их в "Trace"
trace = go.Scatter(
    x=[1, 2, 3, 4],
    y=[100, 150, 120, 180],
    mode="lines+markers",
    name="Выручка"
)

# Вручную создаем макет
layout = go.Layout(
    title="Продажи (Graph Objects)",
    xaxis={"title": "День"},
    yaxis={"title": "Выручка"}
)

# Собираем фигуру из двух частей
fig = go.Figure(data=[trace], layout=layout)
fig.show()
