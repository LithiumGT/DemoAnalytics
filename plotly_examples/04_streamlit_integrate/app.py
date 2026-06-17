import pandas as pd
import plotly.express as px
import streamlit as st

# Объявляем псевдоним типа для данных
type SalesDataFrame = pd.DataFrame

# Настраиваем конфигурацию страницы Streamlit (делать это нужно в самом начале)
st.set_page_config(page_title="BI Dashboard", layout="wide")

@st.cache_data
def load_data() -> SalesDataFrame:
    """Функция загрузки данных с кэшированием, чтобы не читать диск при каждом клике"""
    return pd.read_excel("sales.xlsx", engine="openpyxl")

# 1. Загружаем данные
df: SalesDataFrame = load_data()

# 2. Создаем интерфейс дашборда
st.title("Аналитический дашборд компании 📊")
st.markdown("Учебный проект по интеграции Plotly и Streamlit")

# Выносим фильтры в боковую панель (Sidebar)
st.sidebar.header("Фильтрация данных")

# Создаем выпадающий список для выбора категории товаров
available_categories = ["Все категории"] + list(df["Категория"].unique())
selected_category = st.sidebar.selectbox("Выберите категорию:", available_categories)

# 3. Реализуем логику контекстного фильтра
if selected_category == "Все категории":
    filtered_df = df
else:
    filtered_df = df[df["Категория"] == selected_category]

# 4. Метрики (KPI-блоки) для верхней панели
st.subheader("Основные показатели")
col1, col2, col3 = st.columns(3)

with col1:
    total_revenue = filtered_df["Выручка"].sum()
    st.metric(label="Общая выручка", value=f"{total_revenue:,.0f} ₽")
with col2:
    total_quantity = filtered_df["Количество"].sum()
    st.metric(label="Продано штук", value=f"{total_quantity:,} шт.")
with col3:
    avg_check = filtered_df["Выручка"].mean() if not filtered_df.empty else 0
    st.metric(label="Средний чек", value=f"{avg_check:,.0f} ₽")

st.divider()

# 5. Построение графиков Plotly на основе ОТФИЛЬТРОВАННЫХ данных
st.subheader("Визуализация продаж")

# График 1: Столбчатая диаграмма по товарам
fig_bar = px.bar(
    filtered_df.groupby("Товар", as_index=False)["Выручка"].sum(),
    x="Товар",
    y="Выручка",
    title=f"Выручка по товарам ({selected_category})",
    template="plotly_dark"
)

# График 2: Линейный график динамики
fig_line = px.line(
    filtered_df.groupby("Дата", as_index=False)["Выручка"].sum(),
    x="Дата",
    y="Выручка",
    title="Динамика продаж по дням",
    template="plotly_dark"
)
fig_line.update_layout(hovermode="x unified")

# 6. Вывод графиков в колонки Streamlit
graph_col1, graph_col2 = st.columns(2)

with graph_col1:
    # use_container_width=True заставляет график подстраиваться под размер колонки
    st.plotly_chart(fig_bar, use_container_width=True)

with graph_col2:
    st.plotly_chart(fig_line, use_container_width=True)