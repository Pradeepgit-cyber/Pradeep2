import openpyxl

#will load the sheet/
book = openpyxl.load_workbook("/Users/pradeepbaraik/Downloads/QA TC.xlsx")
sheet = book.active

cell = sheet.cell(row=1, column=2)   #will extract the value from the sheet
print(cell.value)

sheet.cell(row=2, column=2).value = "Pradeep"   #if we need to add value in a cell
print(sheet.cell(row=2, column=2).value)

print(sheet.max_column)    #print all the maximum coloumns
print(sheet.max_row)       #print all the maximum rows
