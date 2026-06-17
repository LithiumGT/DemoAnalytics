import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

type InteractiveFigure = go.Figure

st.title("Интерактивный анализ данных с Box/Lasso Select")

# 1. Создаем тестовый датасет
df = pd.DataFrame({
    "Идентификатор": [f"ID_{i}" for i in range(1, 7)],
    "Опыт работы (лет)": [1, 2, 3, 5, 8, 10],
    "Зарплата ($)": [800, 1200, 1500, 2500, 4000, 4800],
    "Стек": ["Python", "Python", "Java", "Python", "Java", "Python"]
})

# 2. Строим диаграмму рассеяния
fig: InteractiveFigure = px.scatter(
    df,
    x="Опыт работы (лет)",
    y="Зарплата ($)",
    color="Стек",
    hover_name="Идентификатор",
    title="Выделите точки с помощью Box или Lasso Select"
)

fig.update_layout(dragmode="select")

# 3. Выводим график в Streamlit
selection = st.plotly_chart(fig, on_select="rerun")

st.subheader("Данные выделенных специалистов:")

selected_points = selection.get("selection", {}).get("points", [])

if selected_points:
    # Извлекаем индексы строк
    selected_indices = [point["point_index"] for point in selected_points]

    # Фильтруем DataFrame
    filtered_df = df.iloc[selected_indices]

    # Выводим результат
    st.dataframe(filtered_df)
    st.metric(
        label="Средняя зарплата в выделенной группе",
        value=f"${filtered_df['Зарплата ($)'].mean():.0f}"
    )
else:
    st.info("Используйте рамку или лассо на графике выше, чтобы отфильтровать эту таблицу.")