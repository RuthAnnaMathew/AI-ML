import xlsxwriter

# Create a workbook and worksheet
workbook = xlsxwriter.Workbook('store_items.xlsx')
worksheet = workbook.add_worksheet()

# Write title
worksheet.write(0, 0, 'Item')
worksheet.write(0, 1, 'Quantity')

# Write rows of data
worksheet.write(1, 0, 'Pens')
worksheet.write(1, 1, 100)

worksheet.write(2, 0, 'Books')
worksheet.write(2, 1, 50)

worksheet.write(3, 0, 'Pencils')
worksheet.write(3, 1, 75)

# Close book
workbook.close()
