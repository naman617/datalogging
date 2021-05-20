import xlsxwriter

# Workbook() takes one argument which is the filename of the workbook that we want to create,we take user input for the file name.
wb = input('enter the filename')
workbook = xlsxwriter.Workbook(f'{wb}.xlsx')

# The workbook object is then used to add new worksheet via the add method.
worksheet = workbook.add_worksheet()
r = 1

# Use the worksheet object to write
# data via the write() method
while(1):
    worksheet.write('A1', 'Name')
    worksheet.write('B1', 'Phone No')
    worksheet.write('C1', 'Place')
    worksheet.write('D1', 'Body Temp')
    # r,0 is used to tell the coordinates
    worksheet.write(r, 0, input('enter the name'))
    worksheet.write(r, 1, input('enter the phone no'))
    worksheet.write(r, 2, input('Place of origin'))
    worksheet.write(r, 3, float(input('Body Temp')))
    r = r+1
    e = input('c for continue e for exit')
    if e == 'e':
        break
# Finally, close the Excel file
# via the close() method.
workbook.close()
