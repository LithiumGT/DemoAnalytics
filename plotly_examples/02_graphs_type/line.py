import pandas as pd
import plotly.express as px

type SalesDataFrame = pd.DataFrame


def get_data(file_path: str) -> SalesDataFrame:
    # Явно указываем движок openpyxl, знакомый студентам
    return pd.read_excel(file_path, engine='openpyxl')


# Загружаем датасет
df: SalesDataFrame = get_data("sales.xlsx")

# Строим базовый линейный график
fig_line = px.line(
    df,
    x="Дата",
    y="Выручка",
    # TODO: измените названия для осей x и y. Попробуйте указать названия, которых нет в датасете.
    title="Динамика выручки компании"
)
fig_line.show()
