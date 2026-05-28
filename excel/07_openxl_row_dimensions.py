from openpyxl import Workbook

wb = Workbook()
ws = wb.active

data = [
    ["Департамент Разработки", "", ""],          # Строка 1
    ["", "Команда Backend", ""],                 # Строка 2
    ["", "", "Иванов И.И. (Python Developer)"],  # Строка 3
    ["", "", "Петров П.П. (DevOps Engineer)"],   # Строка 4
    ["Департамент Маркетинга", "", ""],          # Строка 5
]

for row in data:
    ws.append(row)

# --- ИСПРАВЛЕННЫЙ БЛОК ГРУППИРОВКИ ---

# 1. Группируем команду Backend (строки 2-4)
ws.row_dimensions.group(start=2, end=4)
for r in range(2, 5):
    ws.row_dimensions[r].outline_level = 1

# 2. Группируем сотрудников внутри команды Backend (строки 3-4)
ws.row_dimensions.group(start=3, end=4)
for r in range(3, 5):
    ws.row_dimensions[r].outline_level = 2

# Переносим кнопку [+] / [-] наверх, к родителю
ws.sheet_properties.outlinePr.summaryBelow = False

wb.save("grouped_report.xlsx")