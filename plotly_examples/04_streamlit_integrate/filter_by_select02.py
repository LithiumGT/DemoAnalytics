import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

# Используем синтаксис Python 3.12 для псевдонима типа фигуры
type InteractiveFigure = go.Figure

st.title("Интерактивный BI-анализ со столбчатой диаграммой")
st.markdown("Выделите рамкой **один или несколько столбцов**, чтобы детализировать отчет.")

# 1. Тестовый датасет — продажи по магазинам и категориям
df = pd.DataFrame({
    "Магазин": ["Магазин А", "Магазин А", "Магазин Б", "Магазин Б", "Магазин В", "Магазин В"],
    "Категория": ["Электроника", "Одежда", "Электроника", "Одежда", "Электроника", "Одежда"],
    "Выручка (₽)": [250000, 120000, 450000, 90000, 180000, 210000],
    "Количество чеков": [120, 85, 310, 60, 95, 150]
})

# 2. Строим столбчатую диаграмму продаж по магазинам
# Параметр color разбивает каждый столбец на сегменты (категории)
fig: InteractiveFigure = px.bar(
    df,
    x="Магазин",
    y="Выручка (₽)",
    color="Категория",
    barmode="group",
    title="Выручка по магазинам и категориям",
    template="plotly_dark"
)

# Исправлено: используем корректный режим "select" для рамки выделения
fig.update_layout(dragmode="select")

# 3. Отображаем график в Streamlit и слушаем событие выделения
selection = st.plotly_chart(fig, on_select="rerun")

st.divider()
st.subheader("Детализация выделенных сегментов рынка:")

# 4. Безопасно извлекаем данные о выделенных столбцах
selected_points = selection.get("selection", {}).get("points", [])

if selected_points:
    # Собираем индексы строк из оригинального DataFrame, которые соответствуют выделенным столбцам
    selected_indices = [point["point_index"] for point in selected_points]

    # Фильтруем данные
    filtered_df = df.iloc[selected_indices]

    # Выводим динамические KPI и таблицу
    col1, col2 = st.columns(2)
    with col1:
        st.metric(
            label="Суммарная выручка выделенных баров",
            value=f"{filtered_df['Выручка (₽)'].sum():,} ₽"
        )
    with col2:
        st.metric(
            label="Всего чеков в выборке",
            value=f"{filtered_df['Количество чеков'].sum():,} шт."
        )

    st.dataframe(filtered_df, use_container_width=True)
else:
    st.info("Потяните мышку с зажатой левой кнопкой по графику (создайте рамку), чтобы выбрать интересующие магазины.")