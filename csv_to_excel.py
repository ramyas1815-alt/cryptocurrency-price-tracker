import csv
from openpyxl import Workbook

workbook = Workbook()
sheet = workbook.active
sheet.title = "Crypto Prices"

with open("crypto_prices.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)

    for row in reader:
        sheet.append(row)

workbook.save("crypto_prices.xlsx")

print("Excel file created successfully!")
print("Saved as: crypto_prices.xlsx")