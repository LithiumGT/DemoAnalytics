from openpyxl import Workbook

wb = Workbook()
ws = wb.active

# Заполняем данными разной длины
ws.append(["ID", "Название компании", "Выручка, ₽"])
ws.append([1, "ООО 'ТехноПромАвтоматизация'", 1500000])
ws.append([2, "АО 'Вектор'", 450000])

# Алгоритм Auto-fit
for col in ws.columns:
    max_len = 0
    # Получаем буквенное имя колонки (например, 'A', 'B', 'C')
    col_letter = col[0].column_letter

    for cell in col:
        if cell.value is not None:
            # Приводим к строке, чтобы корректно считать длину чисел и дат
            cell_len = len(str(cell.value))
            if cell_len > max_len:
                max_len = cell_len

    # Устанавливаем ширину с запасом в 4 символа
    ws.column_dimensions[col_letter].width = max(max_len + 4, 10)  # 10 — минимальная ширина

wb.save("autofit_report.xlsx")