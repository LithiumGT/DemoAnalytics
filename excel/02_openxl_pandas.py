import pandas as pd
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows

df = pd.DataFrame({"Товар": ["Яблоки", "Бананы"], "Продажи": [500, 700]})

wb = Workbook()
ws = wb.active

# dataframe_to_rows возвращает генератор, который нужно распаковать в цикле
# TODO: Измените аргументы index и header, посмотрите на результат
for row in dataframe_to_rows(df, index=False, header=True):
    ws.append(row)

wb.save("stream_report.xlsx")