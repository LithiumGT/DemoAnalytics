import pandas as pd

df = pd.read_csv("sales.csv")

# Полноценный аналитический отчет за один шаг
report = df.groupby("country").agg({
    "price": ["sum", "mean"],  # По ценам хотим сумму и среднее
    "quantity": "sum",  # По количеству — только общую сумму
    "order_id": "count"  # Подсчет количества строк (заказов)
})

print(report)
print("-" * 60)

# Переименовываем колонки в красивые плоские названия
report.columns = ["total_revenue", "avg_price", "total_items", "orders_count"]

# Возвращаем 'country' из индекса обратно в обычную колонку
report = report.reset_index()

print(report)
