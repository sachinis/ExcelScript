import xlsxwriter
workbook = xlsxwriter.Workbook('demo.xlsx')
worksheet = workbook.add_worksheet()
with open('./testfile') as f:
    textList = f.readlines()
for num, line in enumerate(textList):
    worksheet.write(num, 0, line.strip())
workbook.close()
