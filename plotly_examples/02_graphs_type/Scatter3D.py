import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

type ThreeDimensionalFigure = go.Figure

# 1. Генерируем тестовые данные полета дрона по спирали вверх
t = np.linspace(0, 20, 100)
x = np.cos(t)  # Смещение по оси X
y = np.sin(t)  # Смещение по оси Y
z = t * 10     # Высота (ось Z) растет со временем
battery = np.linspace(100, 15, 100)  # Заряд батареи падает со 100% до 15%

df = pd.DataFrame({
    "Координата X": x,
    "Координата Y": y,
    "Высота (Z)": z,
    "Заряд батареи (%)": battery,
    "Секунда полета": range(1, 101)
})

# 2. Строим 3D диаграмму рассеяния (Scatter 3D)
fig: ThreeDimensionalFigure = px.scatter_3d(
    df,
    x="Координата X",
    y="Координата Y",
    z="Высота (Z)",
    color="Заряд батареи (%)",          # Цвет точки зависит от батареи
    size="Секунда полета",              # Размер точки увеличивается со временем
    color_continuous_scale="RdYlGn",    # Красно-желто-зеленая палитра (зеленый — полный заряд)
    title="3D Мониторинг полета квадрокоптера",
    hover_name="Секунда полета"
)

# 3. Настройка отображения (улучшаем визуальный стиль)
fig.update_layout(
    template="plotly_dark", # Темная тема отлично подчеркивает 3D-пространство
    scene=dict(
        xaxis_title="Ось X (Метры)",
        yaxis_title="Ось Y (Метры)",
        zaxis_title="Высота (Метры)"
    )
)

# Отображаем график в браузере
fig.show()